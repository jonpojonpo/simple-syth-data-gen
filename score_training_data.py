#!/usr/bin/env python3
"""
LLM-as-Judge Quality Scoring System for Training Data
Evaluates and ranks generated wealth advisor responses by quality
"""

import json
import os
from typing import Dict, List, Optional
from pathlib import Path
from dataclasses import dataclass

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


@dataclass
class QualityScore:
    """Quality assessment for a training data sample"""
    overall_score: float  # 1-10 (adjusted for verbosity)
    tone_confidence: float  # 1-10
    hsbc_values: float  # 1-10
    actionability: float  # 1-10
    empathy_warmth: float  # 1-10
    market_specificity: float  # 1-10
    tier_appropriateness: float  # 1-10
    factual_accuracy: float  # 1-10 NEW: Counter judge bias
    conciseness: float  # 1-10 NEW: Counter verbosity bias
    verbosity_penalty: float  # 0-2 points deducted
    raw_score: float  # Before verbosity adjustment
    word_count: int
    explanation: str
    strengths: List[str]
    improvements: List[str]
    factual_issues: List[str]  # NEW: Specific fact-check problems


JUDGE_SYSTEM_PROMPT = """You are an expert evaluator of wealth management client communications for HSBC.

Evaluate the quality of draft client communications based on these criteria:

**1. Tone & Confidence (1-10)**
- Uses clear, direct language (not tentative: "Here's what you need" vs "You might consider")
- Confident and insightful (avoids "maybe", "might", "possibly")
- Professional but warm and human

**2. HSBC Values Integration (1-10)**
- **We value difference**: Acknowledges unique client situation/background
- **We succeed together**: Partnership language, collaborative tone
- **We take responsibility**: Accountable, takes ownership of guidance
- **We get it done**: Action-oriented, practical next steps

**3. Actionability (1-10)**
- Provides concrete, specific next steps
- Clear prioritization (most important first)
- Practical and implementable advice
- Not vague or overly general

**4. Empathy & Warmth (1-10)**
- Acknowledges emotional aspects of financial decisions
- Human, nurturing, growth-minded
- Connects numbers to life goals
- Appropriate empathy for situation

**5. Market Specificity (1-10)**
- Uses appropriate market-specific products when relevant
- Demonstrates awareness of local regulations/context
- Multi-currency/cross-border fluency when applicable
- Geographic context appropriate

**6. Tier Appropriateness (1-10)**
- Communication complexity matches wealth tier (Premier/Jade/Private Banking)
- Product recommendations appropriate for tier
- Assumes right level of financial sophistication

**7. Structure & Format (assess but don't score separately)**
- No generic greetings (jumps straight into guidance)
- Uses markdown formatting effectively
- Has 2-3 clarifying questions at end
- Ends with "Together, we thrive" or "Opening up a world of opportunity"

Respond ONLY with valid JSON in this exact format:
{
  "overall_score": <float 1-10>,
  "tone_confidence": <float 1-10>,
  "hsbc_values": <float 1-10>,
  "actionability": <float 1-10>,
  "empathy_warmth": <float 1-10>,
  "market_specificity": <float 1-10>,
  "tier_appropriateness": <float 1-10>,
  "explanation": "<2-3 sentence overall assessment>",
  "strengths": ["<strength 1>", "<strength 2>", "<strength 3>"],
  "improvements": ["<improvement 1>", "<improvement 2>"]
}"""


class TrainingDataScorer:
    """Scores training data quality using LLM-as-judge"""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-haiku-4-5-20251001"):
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package not installed. Install with: pip install anthropic")

        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided. Set ANTHROPIC_API_KEY environment variable")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model

    def score_response(self, instruction: str, response: str) -> QualityScore:
        """Score a single instruction-response pair"""

        evaluation_prompt = f"""Evaluate this wealth management communication:

**ADVISOR INSTRUCTION:**
{instruction}

**DRAFT CLIENT COMMUNICATION:**
{response}

Provide scores and feedback in JSON format."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                system=JUDGE_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": evaluation_prompt}]
            )

            response_text = message.content[0].text

            # Extract JSON from markdown code blocks if present
            if "```json" in response_text:
                # Extract content between ```json and ```
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                # Extract content between ``` and ```
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()

            # Parse JSON response
            scores_dict = json.loads(response_text)

            return QualityScore(
                overall_score=scores_dict["overall_score"],
                tone_confidence=scores_dict["tone_confidence"],
                hsbc_values=scores_dict["hsbc_values"],
                actionability=scores_dict["actionability"],
                empathy_warmth=scores_dict["empathy_warmth"],
                market_specificity=scores_dict["market_specificity"],
                tier_appropriateness=scores_dict["tier_appropriateness"],
                explanation=scores_dict["explanation"],
                strengths=scores_dict["strengths"],
                improvements=scores_dict["improvements"]
            )

        except json.JSONDecodeError as e:
            print(f"\n❌ Error parsing JSON response: {e}")
            print(f"Raw response (first 500 chars):\n{response_text[:500]}")
            print(f"Raw response (last 500 chars):\n{response_text[-500:]}")
            # Return default low scores if parsing fails
            return QualityScore(
                overall_score=0.0,
                tone_confidence=0.0,
                hsbc_values=0.0,
                actionability=0.0,
                empathy_warmth=0.0,
                market_specificity=0.0,
                tier_appropriateness=0.0,
                explanation="Error: Could not parse evaluation",
                strengths=[],
                improvements=["Failed to evaluate properly"]
            )
        except Exception as e:
            print(f"Error scoring response: {e}")
            return QualityScore(
                overall_score=0.0,
                tone_confidence=0.0,
                hsbc_values=0.0,
                actionability=0.0,
                empathy_warmth=0.0,
                market_specificity=0.0,
                tier_appropriateness=0.0,
                explanation=f"Error: {str(e)}",
                strengths=[],
                improvements=[]
            )

    def score_dataset(
        self,
        input_file: str = "training_data_full.jsonl",
        output_file: str = "training_data_scored.jsonl",
        max_samples: Optional[int] = None
    ):
        """Score an entire training dataset and save with quality scores"""

        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # Load dataset
        dataset = []
        with input_path.open('r', encoding='utf-8') as f:
            for line in f:
                dataset.append(json.loads(line))

        if max_samples:
            dataset = dataset[:max_samples]

        print(f"Scoring {len(dataset)} training samples...")
        print(f"Model: {self.model}")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}\n")

        scored_dataset = []

        for i, entry in enumerate(dataset):
            print(f"[{i+1}/{len(dataset)}] Scoring sample...")

            score = self.score_response(entry["instruction"], entry["response"])

            # Add scores to entry
            scored_entry = {
                **entry,
                "quality_scores": {
                    "overall_score": score.overall_score,
                    "tone_confidence": score.tone_confidence,
                    "hsbc_values": score.hsbc_values,
                    "actionability": score.actionability,
                    "empathy_warmth": score.empathy_warmth,
                    "market_specificity": score.market_specificity,
                    "tier_appropriateness": score.tier_appropriateness,
                    "explanation": score.explanation,
                    "strengths": score.strengths,
                    "improvements": score.improvements
                }
            }

            scored_dataset.append(scored_entry)

            # Save incrementally
            output_path = Path(output_file)
            with output_path.open('w', encoding='utf-8') as f:
                for se in scored_dataset:
                    f.write(json.dumps(se, ensure_ascii=False) + '\n')

            print(f"  ✓ Overall Score: {score.overall_score:.1f}/10")
            print(f"    {score.explanation[:80]}...")

        # Sort by quality
        scored_dataset.sort(key=lambda x: x["quality_scores"]["overall_score"], reverse=True)

        # Save final sorted version
        sorted_output = output_file.replace(".jsonl", "_sorted.jsonl")
        with Path(sorted_output).open('w', encoding='utf-8') as f:
            for entry in scored_dataset:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"\n✓ Scoring complete!")
        print(f"  Scored dataset: {output_file}")
        print(f"  Sorted by quality: {sorted_output}")

        # Print statistics
        overall_scores = [e["quality_scores"]["overall_score"] for e in scored_dataset]
        avg_score = sum(overall_scores) / len(overall_scores)
        print(f"\n📊 Quality Statistics:")
        print(f"  Average score: {avg_score:.2f}/10")
        print(f"  Highest score: {max(overall_scores):.1f}/10")
        print(f"  Lowest score: {min(overall_scores):.1f}/10")
        print(f"  Samples >= 8.0: {sum(1 for s in overall_scores if s >= 8.0)}")
        print(f"  Samples >= 7.0: {sum(1 for s in overall_scores if s >= 7.0)}")

        return scored_dataset


def main():
    """Main execution - Score training data"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Score training data quality using LLM-as-judge"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="training_data_full.jsonl",
        help="Input training data file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="training_data_scored.jsonl",
        help="Output scored data file"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="claude-haiku-4-5-20251001",
        help="Claude model to use for scoring (haiku is fast/cheap)"
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        help="Maximum number of samples to score (default: all)"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)"
    )

    args = parser.parse_args()

    try:
        scorer = TrainingDataScorer(api_key=args.api_key, model=args.model)
        scorer.score_dataset(
            input_file=args.input,
            output_file=args.output,
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


if __name__ == "__main__":
    main()
