#!/usr/bin/env python3
"""
Dataset Analysis Tool
Analyze and validate generated training data
"""

import json
import sys
from pathlib import Path
from collections import Counter
import re


def load_dataset(file_path: str):
    """Load JSONL dataset"""
    dataset = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dataset.append(json.loads(line))
    return dataset


def analyze_dataset(file_path: str):
    """Analyze dataset quality and statistics"""

    print(f"\n{'='*80}")
    print(f"DATASET ANALYSIS: {file_path}")
    print(f"{'='*80}\n")

    dataset = load_dataset(file_path)

    # Basic stats
    print(f"📊 Basic Statistics:")
    print(f"   Total samples: {len(dataset)}")
    print(f"   File size: {Path(file_path).stat().st_size / 1024:.2f} KB\n")

    # Instruction analysis
    instruction_lengths = [len(d['instruction']) for d in dataset]
    print(f"📝 Instruction Analysis:")
    print(f"   Average length: {sum(instruction_lengths)/len(instruction_lengths):.0f} characters")
    print(f"   Min length: {min(instruction_lengths)} characters")
    print(f"   Max length: {max(instruction_lengths)} characters\n")

    # Response analysis
    response_lengths = [len(d['response']) for d in dataset]
    print(f"💬 Response Analysis:")
    print(f"   Average length: {sum(response_lengths)/len(response_lengths):.0f} characters")
    print(f"   Min length: {min(response_lengths)} characters")
    print(f"   Max length: {max(response_lengths)} characters\n")

    # Context analysis
    has_context = sum(1 for d in dataset if d['context'].strip())
    print(f"📋 Context Field:")
    print(f"   Samples with context: {has_context}")
    print(f"   Samples without context: {len(dataset) - has_context}\n")

    # Age distribution
    ages = []
    for d in dataset:
        age_matches = re.findall(r'(\d+)(?:-year-old| years old)', d['instruction'])
        if age_matches:
            ages.extend([int(age) for age in age_matches])

    if ages:
        print(f"👥 Age Distribution (from instructions):")
        print(f"   Total ages mentioned: {len(ages)}")
        print(f"   Age range: {min(ages)} - {max(ages)}")
        print(f"   Average age: {sum(ages)/len(ages):.1f}\n")

    # Income distribution
    incomes = []
    for d in dataset:
        income_matches = re.findall(r'\$(\d+(?:,\d+)*)', d['instruction'])
        if income_matches:
            # Get the first income mention (usually annual income)
            income = int(income_matches[0].replace(',', ''))
            if 10000 < income < 500000:  # Filter reasonable income range
                incomes.append(income)

    if incomes:
        print(f"💰 Income Distribution (from instructions):")
        print(f"   Samples with income: {len(incomes)}")
        print(f"   Average income: ${sum(incomes)/len(incomes):,.0f}")
        print(f"   Income range: ${min(incomes):,} - ${max(incomes):,}\n")

    # Check for placeholder responses
    placeholder_responses = sum(1 for d in dataset if '[This would be generated' in d['response'])
    if placeholder_responses > 0:
        print(f"⚠️  Quality Check:")
        print(f"   Placeholder responses: {placeholder_responses}")
        print(f"   Complete responses: {len(dataset) - placeholder_responses}")
        print(f"   Completion rate: {((len(dataset) - placeholder_responses) / len(dataset) * 100):.1f}%\n")
    else:
        print(f"✅ Quality Check:")
        print(f"   All responses are complete (no placeholders)\n")

    # Keyword analysis
    all_instructions = ' '.join(d['instruction'].lower() for d in dataset)

    financial_keywords = {
        'retirement': all_instructions.count('retirement'),
        'savings': all_instructions.count('savings'),
        'investment': all_instructions.count('investment') + all_instructions.count('invest'),
        'debt': all_instructions.count('debt'),
        'college/education': all_instructions.count('college') + all_instructions.count('education'),
        'mortgage': all_instructions.count('mortgage'),
        'insurance': all_instructions.count('insurance'),
    }

    print(f"🔍 Keyword Frequency:")
    for keyword, count in sorted(financial_keywords.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"   {keyword}: {count}")

    print(f"\n{'='*80}\n")


def show_sample(file_path: str, index: int = 0):
    """Display a specific sample"""
    dataset = load_dataset(file_path)

    if index >= len(dataset):
        print(f"Error: Index {index} out of range (dataset has {len(dataset)} samples)")
        return

    sample = dataset[index]

    print(f"\n{'='*80}")
    print(f"SAMPLE #{index + 1}")
    print(f"{'='*80}\n")
    print(f"Instruction:\n{sample['instruction']}\n")
    print(f"Context:\n{sample['context'] if sample['context'] else '(empty)'}\n")
    print(f"Response:\n{sample['response']}\n")
    print(f"{'='*80}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Analyze training dataset")
    parser.add_argument('file', help='JSONL dataset file')
    parser.add_argument('--sample', type=int, help='Show specific sample (0-indexed)')

    args = parser.parse_args()

    if not Path(args.file).exists():
        print(f"Error: File '{args.file}' not found")
        sys.exit(1)

    if args.sample is not None:
        show_sample(args.file, args.sample)
    else:
        analyze_dataset(args.file)


if __name__ == "__main__":
    main()
