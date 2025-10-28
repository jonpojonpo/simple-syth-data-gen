# Advisor-Facing Training Data Generation Workflow

## Overview
This project generates synthetic training data for a **wealth advisor digital partner** that helps advisors craft personalized client communications.

The model is **advisor-facing** - advisors input client situations, and the model outputs draft client communications.

## Two-Stage Process

### Stage 1: Generate Instructions (Advisor Briefs)
```bash
python generate_training_data.py
```

**What it does:**
- Generates 100 advisor-facing instruction prompts
- Each prompt describes a client situation (age, income, savings, goals, challenges)
- Outputs to `instructions.jsonl`

**Example instruction:**
```
38-year-old single parent, $95,000 annual income, $60,000 in savings. Recently paused retirement contributions for child's medical expenses. Need to rebuild confidence and refocus on long-term goals without adding financial strain.
```

### Stage 2: Generate Responses (Draft Client Communications)
```bash
# Preview one sample first
python generate_with_claude.py --preview

# Generate responses for all instructions
python generate_with_claude.py --max-samples 10

# Full dataset (uses all instructions from instructions.jsonl)
python generate_with_claude.py
```

**What it does:**
- Reads advisor instructions from `instructions.jsonl`
- Uses Claude API to generate empathetic, actionable draft client communications
- Outputs to `training_data_full.jsonl`

**Key features of responses:**
- No greetings like "Dear [Client Name]" - jumps straight into guidance
- Empathetic acknowledgment of situation
- Simplifies financial jargon (ELI5 approach)
- Visualizes opportunities with markdown
- Provides prioritized actionable steps
- Ends with clarifying questions for the client
- Always concludes with "Together, we will thrive."
- **NO emojis**

## Configuration

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY='your-api-key'
```

### Configuration File: `config.json`
```json
{
  "generation": {
    "default_samples": 100,
    "seed": 42,
    "delay_seconds": 1.0,
    "model": "claude-haiku-4-5-20251001"
  }
}
```

## Output Format

Training data is in JSONL format (one JSON object per line):

```json
{"instruction": "advisor brief here", "context": "", "response": "draft client communication here"}
```

## Complete Workflow Example

```bash
# 1. Generate instructions (Stage 1)
python generate_training_data.py
# Output: instructions.jsonl (100 advisor briefs)

# 2. Preview a sample response
python generate_with_claude.py --preview

# 3. Generate first 10 responses (test)
python generate_with_claude.py --max-samples 10 --output test_output.jsonl

# 4. Generate full dataset (all 100)
python generate_with_claude.py --output training_data_full.jsonl
```

## Use Case

**The trained model will:**
1. Receive advisor input describing a client situation
2. Generate draft client communication that advisors can review and adapt
3. Support multiple delivery formats: email, meeting prep, conversation guides

**Not client-facing directly** - advisors remain in the loop to review, personalize, and deliver guidance to their clients.
