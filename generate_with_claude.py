#!/usr/bin/env python3
"""
Advanced Synthetic Training Data Generator with Claude API Integration
Generates high-quality JSONL instruction datasets with full AI-generated responses
"""

import json
import os
import time
from typing import Dict, List, Optional
from pathlib import Path
from generate_training_data import WealthAdvisorDataGenerator

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


WEALTH_ADVISOR_SYSTEM_PROMPT = """You help wealth advisors craft personalized client communications that blend expertise with empathy.

After reading "Goals-Based Wealth Management" and "The Psychology of Money", you generate draft guidance that advisors can review and send to their clients.

Your drafts are:
- **Human & Empathetic**: Always empathetic, nurturing, with a growth mindset
- **Simplified**: Demystify financial jargon, break down complex products into simple terms (KISS principle)
- **Connected to Life Goals**: Connect financial products to real-life goals - tangible and relatable
- **ELI5 Approach**: Explain like giving boss-level financial guidance from a trusted mentor
- **Prioritized**: Start with the most important thing first, break it down systematically
- **Visual**: Use vivid markdown formatting to bring financial guidance to life
- **Confidence-Building**: Help clients see what they CAN control
- **Intelligent & Warm**: Offer wit where appropriate, keeping it human and accessible

Response structure:
1. **Empathetic acknowledgment** of their situation (2-3 sentences)
2. **Break down the situation** into clear, manageable pieces
3. **Explain relevant concepts** in simple, relatable terms (avoid jargon or explain it)
4. **Provide actionable steps** prioritized by importance, using clear formatting
5. **Visualize the opportunity** - help them see the positive outcome
6. **End with 2-3 clarifying questions** for the client

Important:
- DO NOT include greetings like "Dear [Client Name]" - jump straight into guidance
- Drafts are adaptable for email, meeting prep, or conversation guides
- Work with whatever client information is provided, infer goals from context
- Bridge the gap between numbers and real life. Keep it warm, human, empowering.
- End with: "Together, we will thrive."
- DO NOT use emojis"""


class ClaudeDataGenerator:
    """Generates complete training data using Claude API"""

    def __init__(self, api_key: Optional[str] = None):
        if not ANTHROPIC_AVAILABLE:
            raise ImportError(
                "anthropic package not installed. Install with: pip install anthropic"
            )

        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter"
            )

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.instruction_generator = WealthAdvisorDataGenerator()

    def generate_response(self, instruction: str, model: str = "claude-haiku-4-5-20251001") -> str:
        """Generate a full wealth advisor response using Claude"""

        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=2000,
                system=WEALTH_ADVISOR_SYSTEM_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": instruction
                    }
                ]
            )

            response_text = message.content[0].text
            return response_text

        except Exception as e:
            print(f"Error generating response: {e}")
            return f"[Error generating response: {e}]"

    def generate_responses_from_instructions(
        self,
        instructions_file: str = "instructions.jsonl",
        output_file: str = "training_data_full.jsonl",
        model: str = "claude-haiku-4-5-20251001",
        delay_seconds: float = 1.0,
        max_samples: Optional[int] = None
    ):
        """Generate responses for pre-generated instructions (Stage 2)"""

        # Load instructions
        instructions_path = Path(instructions_file)
        if not instructions_path.exists():
            raise FileNotFoundError(f"Instructions file not found: {instructions_file}")

        instructions = []
        with instructions_path.open('r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                instructions.append(data['instruction'])

        if max_samples:
            instructions = instructions[:max_samples]

        dataset = []
        output_path = Path(output_file)

        print(f"Generating responses for {len(instructions)} instructions with Claude API...")
        print(f"Model: {model}")
        print(f"Input: {instructions_file}")
        print(f"Output: {output_file}\n")

        for i, instruction in enumerate(instructions):
            print(f"[{i+1}/{len(instructions)}] Generating response...")
            print(f"  Instruction: {instruction[:80]}...")

            # Generate response with Claude
            response = self.generate_response(instruction, model=model)

            # Create dataset entry
            entry = {
                "instruction": instruction,
                "context": "",
                "response": response
            }

            dataset.append(entry)

            # Save incrementally (in case of interruption)
            with output_path.open('a', encoding='utf-8') as f:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

            print(f"  ✓ Response generated ({len(response)} chars)")

            # Rate limiting
            if i < len(instructions) - 1:
                time.sleep(delay_seconds)

        print(f"\n✓ Dataset complete!")
        print(f"  Total samples: {len(dataset)}")
        print(f"  Saved to: {output_file}")

        return dataset

    def preview_sample(self, instructions_file: str = "instructions.jsonl"):
        """Generate and display one complete sample from instructions file"""
        print("\n" + "="*80)
        print("PREVIEW SAMPLE WITH CLAUDE-GENERATED RESPONSE")
        print("="*80 + "\n")

        # Load first instruction
        instructions_path = Path(instructions_file)
        if not instructions_path.exists():
            print(f"Error: Instructions file not found: {instructions_file}")
            print("Run generate_training_data.py first to generate instructions.")
            return

        with instructions_path.open('r', encoding='utf-8') as f:
            first_line = f.readline()
            data = json.loads(first_line)
            instruction = data['instruction']

        print(f"Instruction (advisor brief):\n{instruction}\n")
        print("Generating draft client communication with Claude...\n")

        response = self.generate_response(instruction)

        print(f"Response (draft for client):\n{response}\n")
        print("="*80)


def main():
    """Main execution - Stage 2: Generate Responses"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Stage 2: Generate advisor-facing training data responses with Claude API"
    )
    parser.add_argument(
        "--instructions",
        type=str,
        default="instructions.jsonl",
        help="Input instructions file (default: instructions.jsonl)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="training_data_full.jsonl",
        help="Output file path (default: training_data_full.jsonl)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="claude-haiku-4-5-20251001",
        help="Claude model to use (default: claude-haiku-4-5-20251001)"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Generate and display one preview sample"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between API calls in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        help="Maximum number of samples to generate (default: all)"
    )

    args = parser.parse_args()

    try:
        generator = ClaudeDataGenerator(api_key=args.api_key)

        if args.preview:
            generator.preview_sample(instructions_file=args.instructions)
        else:
            generator.generate_responses_from_instructions(
                instructions_file=args.instructions,
                output_file=args.output,
                model=args.model,
                delay_seconds=args.delay,
                max_samples=args.max_samples
            )

    except ImportError as e:
        print(f"Error: {e}")
        print("\nInstall required package with:")
        print("  pip install anthropic")
    except ValueError as e:
        print(f"Error: {e}")
        print("\nSet your API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key'")
        print("Or pass it with --api-key flag")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nGenerate instructions first:")
        print("  python generate_training_data.py")


if __name__ == "__main__":
    main()
