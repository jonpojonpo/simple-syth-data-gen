# OpenAI API Support

The training data generator now supports both Claude and OpenAI APIs.

## Installation

```bash
# For Claude support
pip install anthropic

# For OpenAI support  
pip install openai

# Install both
pip install anthropic openai
```

## Usage

### Using Claude (default)

```bash
# Set API key
export ANTHROPIC_API_KEY='your-key'

# Generate with default Claude Haiku model
python generate_with_claude.py --instructions instructions.jsonl --output training_data.jsonl

# Or specify Claude Sonnet
python generate_with_claude.py --provider claude --model claude-sonnet-4-5-20250929
```

### Using OpenAI

```bash
# Set API key
export OPENAI_API_KEY='your-key'

# Generate with gpt-4o-mini (default, cost-effective)
python generate_with_claude.py --provider openai --instructions instructions.jsonl --output training_data_openai.jsonl

# Or specify gpt-4o for higher quality
python generate_with_claude.py --provider openai --model gpt-4o

# Or gpt-4-turbo
python generate_with_claude.py --provider openai --model gpt-4-turbo
```

### Preview Mode

```bash
# Preview with OpenAI
python generate_with_claude.py --provider openai --preview

# Preview with Claude
python generate_with_claude.py --provider claude --preview
```

### Advanced Options

```bash
# Generate limited samples with custom delay
python generate_with_claude.py \
  --provider openai \
  --model gpt-4o-mini \
  --max-samples 10 \
  --delay 0.5 \
  --output test_data.jsonl
```

## Model Recommendations

### Claude Models
- **claude-haiku-4-5-20251001** (default): Fast, cost-effective, good quality
- **claude-sonnet-4-5-20250929**: Higher quality, more expensive

### OpenAI Models
- **gpt-4o-mini** (default): Most cost-effective (~15x cheaper than GPT-4), good for bulk generation
- **gpt-4o**: Latest GPT-4 Optimized model, high quality
- **gpt-4-turbo**: High quality, faster than base GPT-4

## Cost Comparison

Approximate costs for 1000 instructions with ~2000 token responses:

| Provider | Model | Input Cost | Output Cost | Total (1000 samples) |
|----------|-------|------------|-------------|---------------------|
| Claude | Haiku | $0.25/MTok | $1.25/MTok | ~$3-5 |
| Claude | Sonnet | $3/MTok | $15/MTok | ~$35-45 |
| OpenAI | gpt-4o-mini | $0.15/MTok | $0.60/MTok | ~$1.50-2 |
| OpenAI | gpt-4o | $2.50/MTok | $10/MTok | ~$22-28 |

**Recommendation**: Use `gpt-4o-mini` with `--provider openai` for cost-effective bulk generation.

## Example Workflow

```bash
# Step 1: Generate instructions (same for both)
python generate_training_data.py

# Step 2: Generate responses with OpenAI (cost-effective)
export OPENAI_API_KEY='your-key'
python generate_with_claude.py \
  --provider openai \
  --model gpt-4o-mini \
  --instructions instructions.jsonl \
  --output training_data_openai.jsonl

# Step 3: Score the data (optional)
python score_training_data.py \
  --input training_data_openai.jsonl \
  --output training_data_scored.jsonl
```
