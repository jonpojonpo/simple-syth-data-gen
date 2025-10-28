#!/usr/bin/env python3
"""
Synthetic Training Data Generator for Wealth Management Advisor
Generates JSONL instruction datasets for fine-tuning Llama 3B
"""

import json
import random
from typing import Dict, List, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClientPersona:
    """Represents a client archetype for generating realistic scenarios"""
    age_range: Tuple[int, int]
    income_range: Tuple[int, int]
    life_stage: str
    common_goals: List[str]
    common_challenges: List[str]
    family_situations: List[str]


class WealthAdvisorDataGenerator:
    """Generates synthetic instruction data for wealth management training"""

    def __init__(self, seed: int = 42):
        random.seed(seed)
        self.persona_templates = self._initialize_personas()
        self.financial_products = self._initialize_products()
        self.goal_types = self._initialize_goals()

    def _initialize_personas(self) -> List[ClientPersona]:
        """Define diverse client personas based on HSBC wealth segments"""
        return [
            # HSBC Premier - Mass Affluent ($250k-$1M assets)
            ClientPersona(
                age_range=(28, 42),
                income_range=(120000, 250000),
                life_stage="Premier Mass Affluent",
                common_goals=["grow investment portfolio to reach Jade tier", "international property investment",
                             "children's overseas education planning", "build diversified portfolio",
                             "maximize tax-advantaged retirement accounts"],
                common_challenges=["managing wealth across multiple countries", "understanding cross-border tax implications",
                                 "balancing growth vs stability", "optimizing international banking relationships"],
                family_situations=["expat family with children", "dual-income international professionals",
                                 "returning to home country after abroad", "relocating family for career"]
            ),

            # HSBC Jade - Affluent ($1M-$5M assets)
            ClientPersona(
                age_range=(38, 58),
                income_range=(300000, 800000),
                life_stage="Jade Affluent",
                common_goals=["access alternative investments", "multi-generational wealth planning",
                             "establish family trust structures", "philanthropic giving strategy",
                             "succession planning for family business"],
                common_challenges=["coordinating wealth across Hong Kong-Singapore-UK", "ESG investing alignment",
                                 "managing concentrated stock positions", "structuring cross-border inheritance"],
                family_situations=["business owner with adult children", "family office consideration",
                                 "first-generation wealth creator", "managing inherited family assets"]
            ),

            # HSBC Private Banking - HNW/UHNW ($5M+ assets)
            ClientPersona(
                age_range=(45, 70),
                income_range=(500000, 3000000),
                life_stage="Private Banking HNW",
                common_goals=["sophisticated trust and estate planning", "impact investing and sustainable portfolios",
                             "art and alternative asset diversification", "next-generation wealth education",
                             "global citizenship and residency planning"],
                common_challenges=["complex multi-jurisdictional tax planning", "managing private equity illiquidity",
                                 "family governance and wealth transfer", "protecting wealth from regulatory changes"],
                family_situations=["entrepreneur preparing for business exit", "multi-generational family wealth",
                                 "philanthropist establishing foundation", "managing family office transition"]
            ),

            # Young Professionals & Tech Workers
            ClientPersona(
                age_range=(25, 38),
                income_range=(90000, 300000),
                life_stage="Emerging Wealth",
                common_goals=["stock option exercise strategy", "first-time international property purchase",
                             "startup equity portfolio management", "build sustainable investment portfolio",
                             "leverage digital wealth tools"],
                common_challenges=["concentrated position in employer stock", "understanding RSU/ISO tax treatment",
                                 "navigating crypto and digital assets", "balancing FOMO with prudent investing"],
                family_situations=["tech worker with equity compensation", "startup founder post-funding",
                                 "single professional in tier-1 city", "young couple expecting first child"]
            ),

            # Cross-Border & International Clients
            ClientPersona(
                age_range=(35, 60),
                income_range=(200000, 900000),
                life_stage="International Cross-Border",
                common_goals=["optimize multi-currency portfolio", "coordinate wealth across Asia-Middle East corridor",
                             "international school funding strategy", "repatriation and retirement planning",
                             "Greater Bay Area wealth management"],
                common_challenges=["currency hedging across USD-GBP-HKD-SGD", "regulatory compliance across jurisdictions",
                                 "managing banking relationships in 3+ countries", "understanding wealth connect schemes"],
                family_situations=["expat in UAE or Singapore hub", "split family across multiple countries",
                                 "returning to mainland China", "commuting between Hong Kong and Shenzhen"]
            ),

            # Entrepreneurs & Business Owners
            ClientPersona(
                age_range=(40, 65),
                income_range=(250000, 2000000),
                life_stage="Entrepreneur",
                common_goals=["business exit and liquidity planning", "separate business and personal wealth",
                             "key person insurance strategy", "funding next generation's entrepreneurship",
                             "transition from working capital to invested capital"],
                common_challenges=["business valuation and sale readiness", "protecting family from business risk",
                                 "managing lumpy irregular income", "choosing between dividends vs reinvestment"],
                family_situations=["family business with multiple siblings", "solo founder considering partners",
                                 "second-generation taking over business", "serial entrepreneur with multiple ventures"]
            ),

            # Sustainable & Impact Investors
            ClientPersona(
                age_range=(30, 55),
                income_range=(150000, 600000),
                life_stage="Sustainable Wealth",
                common_goals=["build 100% ESG-aligned portfolio", "measure social impact of investments",
                             "establish charitable giving vehicle", "align wealth with UN SDG goals",
                             "invest in climate solutions and green bonds"],
                common_challenges=["understanding ESG ratings and greenwashing", "balancing impact with returns",
                                 "finding authentic sustainable investment opportunities", "measuring real-world impact"],
                family_situations=["socially conscious millennial couple", "impact-focused entrepreneur",
                                 "family transitioning to sustainable investing", "next-gen demanding ESG alignment"]
            ),

            # Retirees & Wealth Preservation
            ClientPersona(
                age_range=(60, 80),
                income_range=(80000, 400000),
                life_stage="Wealth Preservation",
                common_goals=["generate sustainable retirement income", "healthcare and longevity planning",
                             "minimize estate taxes and probate", "support grandchildren's education globally",
                             "maintain lifestyle across multiple residences"],
                common_challenges=["sequence of returns risk", "required minimum distributions strategy",
                                 "long-term care insurance evaluation", "managing property across countries"],
                family_situations=["recently retired executive", "widowed with adult children abroad",
                                 "snowbird between two countries", "grandparents funding education trusts"]
            )
        ]

    def _initialize_products(self) -> Dict[str, List[str]]:
        """HSBC-specific financial products and services"""
        return {
            "investment": ["equity mutual funds", "fixed income funds", "ETFs", "target-date funds",
                          "money market funds", "alternative investments", "structured products",
                          "private market investments (Jade)", "discretionary portfolio management"],
            "sustainable": ["ESG equity funds", "green bonds", "social bonds", "sustainability-linked bonds",
                           "SDG-aligned emerging market funds", "impact investing mandates",
                           "climate solutions portfolio", "biodiversity funds"],
            "cross_border": ["multi-currency account", "international payment solutions",
                            "Greater Bay Area wealth connect", "cross-border mortgage",
                            "global property portfolio financing", "currency hedging strategies"],
            "trust_estate": ["revocable living trust", "irrevocable trust", "family trust structures",
                            "charitable remainder trust", "generation-skipping trust",
                            "cross-border estate planning", "succession planning services"],
            "insurance": ["term life insurance", "whole life insurance", "universal life",
                         "key person insurance", "directors & officers insurance",
                         "umbrella liability policy", "international health insurance"],
            "retirement": ["401(k)", "Roth IRA", "Traditional IRA", "SEP IRA", "pension rollover",
                          "annuities with guaranteed income", "retirement income planning",
                          "required minimum distribution strategy"],
            "alternative": ["private equity funds", "hedge funds", "real estate investment trusts",
                           "art and collectibles financing", "commodities", "venture capital funds"],
            "education": ["529 plan", "Coverdell ESA", "UGMA/UTMA accounts",
                         "international school funding", "overseas university planning",
                         "education trusts for grandchildren"],
            "business": ["business succession planning", "buy-sell agreements",
                        "stock option exercise planning", "RSU/ISO tax strategies",
                        "family office setup", "business exit liquidity planning"],
            "tax": ["tax-loss harvesting", "charitable giving strategies", "donor-advised funds",
                   "multi-jurisdictional tax optimization", "expatriate tax planning",
                   "FATCA compliance strategies"]
        }

    def _initialize_goals(self) -> Dict[str, List[str]]:
        """Common financial goals by category"""
        return {
            "short_term": ["build 3-6 month emergency fund", "save for vacation", "pay off credit card debt",
                          "save for car down payment", "create a budget that works"],
            "medium_term": ["save for home down payment", "fund children's education", "start a business",
                           "pay off student loans", "build investment portfolio"],
            "long_term": ["retire comfortably by age X", "achieve financial independence",
                         "leave legacy for children", "fund dream retirement lifestyle",
                         "create passive income streams"]
        }

    def generate_instruction(self, persona: ClientPersona) -> str:
        """Generate a realistic client instruction/question"""
        age = random.randint(*persona.age_range)
        income = random.randint(*persona.income_range)
        income = round(income / 1000) * 1000  # Round to nearest thousand

        # Choose scenario type with weighted distribution
        scenario_types = [
            self._generate_goal_based_instruction,
            self._generate_challenge_based_instruction,
            self._generate_product_question_instruction,
            self._generate_complex_scenario_instruction,
            self._generate_hsbc_specific_scenario  # New HSBC-specific scenarios
        ]

        scenario_func = random.choice(scenario_types)
        return scenario_func(persona, age, income)

    def _generate_goal_based_instruction(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate advisor-facing instruction focused on client goal"""
        family = random.choice(persona.family_situations)
        goal = random.choice(persona.common_goals)

        templates = [
            f"{age}-year-old {family}, ${income:,} annual income. Wants to {goal}.",
            f"{age} years old, {family}, earning ${income:,} annually. Goal: {goal}.",
            f"{age}-year-old {family} making ${income:,}/year. Looking to {goal}.",
        ]
        return random.choice(templates)

    def _generate_challenge_based_instruction(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate advisor-facing instruction focused on client challenge"""
        family = random.choice(persona.family_situations)
        challenge = random.choice(persona.common_challenges)
        savings = random.randint(income // 4, income * 2)

        templates = [
            f"{age}-year-old {family}, ${income:,} annual income, ${savings:,} in savings. Struggling with {challenge}.",
            f"{age} years old, {family}, ${income:,}/year. Challenge: {challenge}. ${savings:,} saved.",
            f"{age}-year-old {family} earning ${income:,} with ${savings:,} saved. Difficulty with {challenge}.",
        ]
        return random.choice(templates)

    def _generate_product_question_instruction(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate advisor-facing instruction about financial products"""
        family = random.choice(persona.family_situations)
        category = random.choice(list(self.financial_products.keys()))
        product = random.choice(self.financial_products[category])
        goal = random.choice(persona.common_goals)

        templates = [
            f"{age}-year-old {family}, ${income:,} income. Confused about {product}. Needs simple explanation.",
            f"{age} years old, {family}, earning ${income:,}. Considering {product} to {goal}. Explain benefits.",
            f"{age}-year-old {family} making ${income:,}. Heard about {product}, wants it demystified.",
        ]
        return random.choice(templates)

    def _generate_complex_scenario_instruction(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate complex multi-factor advisor-facing scenarios"""
        family = random.choice(persona.family_situations)
        challenge = random.choice(persona.common_challenges)
        goal = random.choice(persona.common_goals)

        # Add specific financial details
        savings = random.randint(max(0, income // 10), income * 3)
        debt = random.randint(0, income)

        templates = [
            f"{age}-year-old {family}, ${income:,} annual income, ${savings:,} in savings. Recently paused retirement contributions due to {challenge}. Need to rebuild confidence and refocus on long-term goals without adding financial strain.",
            f"{age} years old, {family}, ${income:,} income, ${savings:,} saved, ${debt:,} in debt. Wants to {goal} while dealing with {challenge}. Feeling overwhelmed.",
            f"{age}-year-old {family} earning ${income:,}, ${savings:,} saved. Challenge: {challenge}. Goal: {goal}. Needs help prioritizing and balancing everything.",
        ]
        return random.choice(templates)

    def _generate_hsbc_specific_scenario(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate HSBC-specific scenarios based on their wealth segments and products"""
        family = random.choice(persona.family_situations)
        goal = random.choice(persona.common_goals)
        challenge = random.choice(persona.common_challenges)
        savings = random.randint(max(income // 2, 100000), income * 5)

        # HSBC-specific scenario templates
        hsbc_scenarios = [
            # Cross-border scenarios
            f"{age}-year-old {family} moving from Hong Kong to Singapore, ${income:,} income, ${savings:,} in assets. Need help with cross-border wealth transfer, tax implications, and setting up banking in new jurisdiction.",
            f"{age} years old, {family}, managing wealth across UK-HKD-SGD currencies. ${income:,} annual income, ${savings:,} portfolio. Looking to optimize currency exposure and reduce FX risk.",
            f"{age}-year-old {family}, ${income:,} income. Participating in Greater Bay Area Wealth Connect. Wants to understand investment limits, eligible products, and cross-border tax treatment.",

            # Tier progression scenarios
            f"{age} years old, {family}, currently HSBC Premier with ${savings:,} in assets. ${income:,} annual income. Close to Jade tier threshold - want strategy to reach $1.2M and access alternative investments.",
            f"{age}-year-old {family}, Jade client with ${savings:,}, ${income:,} income. Considering transition to Private Banking. What additional services and investment opportunities become available at $5M+ level?",

            # ESG and sustainable investing
            f"{age}-year-old {family}, ${income:,} income, ${savings:,} portfolio. Want to transition entire portfolio to ESG-aligned investments. Concerned about greenwashing and measuring real impact.",
            f"{age} years old, {family}, ${income:,} annual income. Interested in SDG-aligned emerging market bonds and climate solutions funds. Need education on sustainable investing options and performance expectations.",
            f"{age}-year-old {family} with ${savings:,} portfolio. Want to establish donor-advised fund for systematic philanthropy while maintaining ESG investment approach. Looking for tax-efficient structure.",

            # Business owner scenarios
            f"{age}-year-old entrepreneur, {family}, preparing to sell family business. Expecting ${savings * 2:,} liquidity event within 12 months. Need comprehensive tax planning, investment strategy, and wealth structure before exit.",
            f"{age} years old, {family}, serial entrepreneur with ${income:,} annual income but lumpy. ${savings:,} saved. Need strategy to smooth income, separate business risk from family wealth, and plan for next venture.",
            f"{age}-year-old family business owner, second generation, ${income:,} income. Managing succession planning with three siblings. Need governance structure and fair distribution strategy.",

            # Equity compensation scenarios
            f"{age}-year-old tech professional, {family}, ${income:,} base salary plus ${income // 2:,} in RSUs vesting annually. 60% of net worth concentrated in employer stock. Need diversification strategy and tax planning.",
            f"{age} years old, startup founder post-Series B, {family}. Sitting on ${savings:,} in illiquid equity. ${income:,} salary. ISO exercise deadline approaching - need to evaluate tax implications and liquidity options.",

            # International education scenarios
            f"{age}-year-old expat couple, {family}, ${income:,} income. Two children heading to US/UK universities in 2-4 years. Need international education funding strategy accounting for currency risk and tax optimization.",
            f"{age} years old, {family}, ${income:,} annual income, ${savings:,} saved. Grandchildren attending international schools in three different countries. Want to establish education trusts with cross-border efficiency.",

            # Repatriation and relocation
            f"{age}-year-old {family}, returning to mainland China after 15 years in Singapore. ${income:,} income, ${savings:,} in assets. Need repatriation strategy, understand investment restrictions, and optimize tax position.",
            f"{age} years old, {family}, relocating from London to Dubai for career. ${income:,} income, ${savings:,} portfolio. Need to understand UAE wealth management landscape, tax advantages, and maintain UK property investments.",

            # Retirement and legacy
            f"{age}-year-old {family}, ${income:,} pension income, ${savings:,} portfolio. Properties in Hong Kong and Vancouver. Need cross-border estate plan to minimize taxes and ensure smooth transfer to children in different countries.",
            f"{age} years old, {family}, recently retired with ${savings:,} portfolio generating ${income:,} annually. Concerned about sequence of returns risk and making portfolio last 30+ years across multiple currencies.",

            # Alternative investments
            f"{age}-year-old Jade client, {family}, ${income:,} income, ${savings:,} portfolio currently 80% public equities. Want exposure to private equity and alternative investments. Need education on illiquidity, fees, and allocation strategy.",
            f"{age} years old, UHNW client, {family}, ${income:,} annual income, ${savings:,} AUM. Interested in art financing and collectibles as part of portfolio. Want to understand lending ratios and integration with overall wealth strategy.",

            # Multi-generational wealth
            f"{age}-year-old {family}, managing ${savings:,} multi-generational family wealth. Three adult children with different risk tolerances and ESG preferences. Need family governance framework and customized sub-portfolios.",
            f"{age} years old, {family}, inherited ${savings:,} from parents. ${income:,} own income. Next generation (millennials) demanding 100% sustainable investing while preserving family wealth. Need transition strategy.",
        ]

        return random.choice(hsbc_scenarios)

    def generate_instructions_only(self, num_samples: int, output_file: str = "instructions.jsonl"):
        """Generate advisor instructions only (Stage 1)"""
        instructions = []

        print(f"Generating {num_samples} advisor instruction prompts...")

        for i in range(num_samples):
            # Randomly select a persona
            persona = random.choice(self.persona_templates)

            # Generate instruction
            instruction = self.generate_instruction(persona)

            instructions.append(instruction)

            if (i + 1) % 10 == 0:
                print(f"  Generated {i + 1}/{num_samples} instructions...")

        # Save to JSONL (one instruction per line)
        output_path = Path(output_file)
        with output_path.open('w', encoding='utf-8') as f:
            for instruction in instructions:
                f.write(json.dumps({"instruction": instruction}, ensure_ascii=False) + '\n')

        print(f"\n✓ Instructions saved to {output_file}")
        print(f"  Total instructions: {len(instructions)}")
        return instructions

    def preview_samples(self, num_samples: int = 3):
        """Generate and display preview samples"""
        print("\n" + "="*80)
        print("PREVIEW SAMPLES")
        print("="*80 + "\n")

        for i in range(num_samples):
            persona = random.choice(self.persona_templates)
            instruction = self.generate_instruction(persona)

            print(f"Sample {i+1}:")
            print(f"Persona: {persona.life_stage}")
            print(f"Instruction: {instruction}")
            print("-" * 80 + "\n")


def main():
    """Main execution - Stage 1: Generate Instructions Only"""
    generator = WealthAdvisorDataGenerator(seed=42)

    # Preview some samples
    print("Previewing sample advisor instructions...")
    generator.preview_samples(num_samples=5)

    # Generate instructions only (Stage 1)
    print("\n" + "="*80)
    print("STAGE 1: Generating Advisor Instructions")
    print("="*80)
    print("\nThis generates advisor-facing prompts describing client situations.")
    print("Stage 2 (response generation) will use Claude API to create client communications.\n")

    num_samples = 100  # Generate 100 instruction prompts
    generator.generate_instructions_only(num_samples=num_samples, output_file="instructions.jsonl")


if __name__ == "__main__":
    main()
