# Wealth Management Advisor - Training Data Generator

Generate high-quality synthetic instruction datasets for fine-tuning Llama 3B to become an empathetic, human-centered wealth management advisor.

## Overview

This tool generates JSONL training data in the format:
```json
{"instruction":"...", "context":"", "response":"..."}
```

The assistant is trained to:
- Approach wealth management with empathy and a nurturing growth mindset
- Simplify complex financial products and demystify jargon
- Connect products to real-life goals (KISS principle)
- Explain everything in ELI5 terms with warmth
- Visualize opportunities through vivid markdown formatting
- Build confidence and focus on what clients CAN control

Inspired by "Goals-Based Wealth Management" and "The Psychology of Money".

## Features

✨ **5 Diverse Client Personas**
- Early Career (25-35)
- Mid Career (35-50)
- Pre-Retirement (50-65)
- Retirement (65-80)
- Life Transition (28-45)

🎯 **4 Scenario Types**
- Goal-based inquiries
- Challenge-focused situations
- Product education questions
- Complex multi-factor scenarios

🤖 **Two Generation Modes**
1. **Template mode**: Generate instructions with placeholder responses (fast, no API needed)
2. **Claude mode**: Generate full responses using Claude API (high quality, production-ready)

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key (for Claude mode)
export ANTHROPIC_API_KEY='your-api-key-here'
```

## Quick Start

### 1. Preview Samples (No API Required)

```bash
python generate_training_data.py
```

This generates 50 samples with instruction prompts and response templates.

### 2. Generate Full Dataset with Claude

```bash
# Generate 50 samples (default)
python generate_with_claude.py

# Generate custom number of samples
python generate_with_claude.py --samples 200

# Preview one complete sample
python generate_with_claude.py --preview

# Customize output file
python generate_with_claude.py --samples 100 --output my_dataset.jsonl
```

## Usage Examples

### Basic Generation
```bash
python generate_with_claude.py --samples 100
```

### Advanced Options
```bash
python generate_with_claude.py \
  --samples 500 \
  --output wealth_advisor_v1.jsonl \
  --model claude-haiku-4-5-20251001 \
  --delay 1.5
```

### Preview Before Generation
```bash
# See what a complete sample looks like
python generate_with_claude.py --preview
```

## Command Line Options

```
--samples N         Number of training samples to generate (default: 50)
--output FILE       Output JSONL file path (default: training_data_full.jsonl)
--model MODEL       Claude model to use (default: claude-haiku-4-5-20251001)
--preview           Generate and display one complete sample
--api-key KEY       Anthropic API key (or set ANTHROPIC_API_KEY env var)
--delay SECONDS     Delay between API calls (default: 1.0)
```

## Output Format

Each line in the JSONL file contains:

```json
{
  "instruction": "I'm 42, married with two kids, earning $95,000 annually. I want to save for my children's college education while also building retirement savings. How can I balance both priorities?",
  "context": "",
  "response": "I hear you, and what you're feeling is completely natural - wanting to secure both your children's future AND your own retirement shows real financial wisdom...\n\n[Full empathetic, detailed response with markdown formatting, actionable steps, and clarifying questions]"
}
```

## Example Instructions Generated

- "A 38-year-old single parent earns $95,000 a year and has $60,000 in savings but recently had to pause retirement contributions to help pay for their child's medical expenses. How would you help them rebuild confidence and refocus on long term goals without creating added financial strain?"

- "I'm 28, recently divorced, making $75,000 with $15,000 saved. I want to start investing but I'm also dealing with rebuilding my emergency fund. I feel overwhelmed. Where do I even begin?"

- "At 55 years old, empty nester, I earn $120,000 and have managed to save $180,000, but I'm behind on retirement savings. What should I prioritize?"

## Customization

Edit `config.json` to customize:
- Number of samples
- Scenario type weights
- Enabled personas
- Response style preferences
- Model selection

## Response Quality

Responses follow the wealth advisor persona:
- ✅ Empathetic acknowledgment
- ✅ Break down into manageable pieces
- ✅ ELI5 explanations
- ✅ Actionable prioritized steps
- ✅ Vivid markdown visualization
- ✅ Clarifying questions
- ✅ Warm, nurturing tone

## Project Structure

```
.
├── generate_training_data.py    # Core generator (template mode)
├── generate_with_claude.py      # Claude API integration
├── config.json                  # Configuration settings
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Project instructions
└── README.md                    # This file
```

## Cost Estimation

Claude API costs (approximate):
- Claude Haiku 4.5: ~$0.0001 per response (ultra-fast & economical!)
- 100 samples: ~$0.01
- 1000 samples: ~$0.10
- 10,000 samples: ~$1.00

Use `--delay` to control rate limiting.

## Tips for Best Results

1. **Start Small**: Generate 10-20 samples first to verify quality
2. **Review & Iterate**: Check the responses align with your persona
3. **Customize Personas**: Edit the persona templates in `generate_training_data.py`
4. **Add Scenarios**: Extend scenario types for more variety
5. **Fine-tune Prompt**: Adjust `WEALTH_ADVISOR_SYSTEM_PROMPT` in `generate_with_claude.py`

## Training Your Model

Once you have your JSONL dataset:

```bash
# Example with Llama 3B fine-tuning
# (specific commands depend on your training framework)
python train.py \
  --model meta-llama/Llama-3.2-3B \
  --dataset training_data_full.jsonl \
  --epochs 3 \
  --batch-size 4
```

## Troubleshooting

**"No API key provided"**
```bash
export ANTHROPIC_API_KEY='your-key'
```

**"anthropic package not installed"**
```bash
pip install anthropic
```

**Rate limit errors**
```bash
# Increase delay between requests
python generate_with_claude.py --delay 2.0
```

## Contributing

Ideas for enhancement:
- [ ] Add more diverse personas (entrepreneurs, freelancers, etc.)
- [ ] Include international scenarios (different currencies, tax systems)
- [ ] Add data validation and quality checks
- [ ] Support other LLM providers (OpenAI, etc.)
- [ ] Implement resume capability for interrupted runs
- [ ] Add sentiment analysis for response quality

## License

MIT License - feel free to use and modify for your projects!

## Acknowledgments

Inspired by:
- "Goals-Based Wealth Management"
- "The Psychology of Money" by Morgan Housel
- HSBC's vision for empathetic, accessible wealth guidance

---

**Together, we will thrive!** 🌟
