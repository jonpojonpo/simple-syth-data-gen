#!/bin/bash

# Example usage script for the Wealth Management Training Data Generator

echo "==================================================================="
echo "Wealth Management Advisor - Training Data Generator Examples"
echo "==================================================================="
echo ""

# Example 1: Preview without API
echo "1. Preview sample instructions (no API required)"
echo "   Command: python generate_training_data.py"
echo ""

# Example 2: Preview one complete sample with Claude
echo "2. Preview one complete sample with Claude-generated response"
echo "   Command: python generate_with_claude.py --preview"
echo ""

# Example 3: Generate small dataset
echo "3. Generate 10 samples for testing"
echo "   Command: python generate_with_claude.py --samples 10 --output test_data.jsonl"
echo ""

# Example 4: Generate production dataset
echo "4. Generate 200 samples for training"
echo "   Command: python generate_with_claude.py --samples 200 --output wealth_advisor_training.jsonl --delay 1.5"
echo ""

# Example 5: Use different model
echo "5. Use Claude Sonnet for even higher quality (costs more)"
echo "   Command: python generate_with_claude.py --samples 50 --model claude-3-5-sonnet-20241022"
echo ""

echo "==================================================================="
echo "Setup Instructions:"
echo "==================================================================="
echo ""
echo "1. Install dependencies:"
echo "   pip install -r requirements.txt"
echo ""
echo "2. Set your API key:"
echo "   export ANTHROPIC_API_KEY='your-api-key-here'"
echo ""
echo "3. Start generating!"
echo ""
