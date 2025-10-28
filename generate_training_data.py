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
        self.markets = self._initialize_markets()
        self.wealth_tiers = self._initialize_wealth_tiers()

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

    def _initialize_markets(self) -> Dict[str, Dict]:
        """Market-specific contexts based on HSBC global operations"""
        return {
            "China": {
                "currencies": ["CNY", "HKD", "USD"],
                "products": ["QDII quota investments", "Greater Bay Area Wealth Connect", "A-share funds",
                           "RMB structured products", "cross-border estate planning"],
                "challenges": ["capital controls and outflow restrictions", "QDII quota limitations",
                             "A-share vs H-share allocation", "onshore vs offshore RMB",
                             "dual-currency (CNY/HKD) management"],
                "goals": ["overseas education funding (US/UK)", "property investment abroad",
                         "foreign currency diversification", "family immigration planning",
                         "accessing offshore investment products"],
                "scenarios": ["mainland Chinese professional in Shenzhen accessing Greater Bay Area Wealth Connect",
                            "Shanghai entrepreneur preparing for business IPO with cross-border wealth planning",
                            "Beijing tech executive with RSUs in US company navigating QDII quotas",
                            "Guangzhou family funding child's education at UK university"]
            },
            "Indonesia": {
                "currencies": ["IDR", "USD", "SGD"],
                "products": ["offshore investment accounts", "foreign currency deposits", "Jakarta property financing",
                           "international education trusts", "Indonesian government bonds"],
                "challenges": ["IDR currency volatility", "local market depth limitations",
                             "accessing international investment platforms", "cross-border wealth transfer"],
                "goals": ["diversify away from IDR concentration", "fund children's education in Singapore/Australia",
                         "build USD/SGD reserves", "manage business sale proceeds internationally"],
                "scenarios": ["Jakarta business owner diversifying wealth outside Indonesia after company sale",
                            "Indonesian family in Surabaya planning for children's university in Australia",
                            "Bali property investor managing multi-currency rental income streams",
                            "Indonesian expat returning home after years in Singapore"]
            },
            "Singapore": {
                "currencies": ["SGD", "USD", "CNY", "MYR"],
                "products": ["Premier Elite services", "international investment platforms", "SRS retirement planning",
                           "CPF optimization", "Singapore property financing"],
                "challenges": ["high cost of living and property prices", "CPF withdrawal restrictions",
                             "permanent residency vs citizenship wealth implications", "regional wealth hub competition"],
                "goals": ["optimize CPF and SRS for retirement", "manage international portfolio across ASEAN",
                         "leverage Singapore as wealth booking center", "access Swiss-based Asia desk services"],
                "scenarios": ["Singapore expat managing wealth across Southeast Asia and India corridors",
                            "tech professional in Singapore with employer stock options and CPF optimization needs",
                            "Indian national in Singapore leveraging international wealth hub for cross-border investments",
                            "Chinese family relocated to Singapore establishing offshore wealth structure"]
            },
            "Australia": {
                "currencies": ["AUD", "USD", "NZD"],
                "products": ["superannuation optimization", "property investment loans", "Australian equity funds",
                           "self-managed super funds (SMSF)", "franking credit strategies"],
                "challenges": ["superannuation access restrictions", "Australian property market cycles",
                             "capital gains tax on foreign investments", "pension phase planning"],
                "goals": ["maximize superannuation contributions", "build property portfolio",
                         "plan for Australian retirement", "manage currency risk on overseas assets"],
                "scenarios": ["Sydney professional optimizing concessional super contributions and SMSF setup",
                            "Melbourne family balancing property investment with superannuation growth",
                            "Brisbane retiree transitioning to pension phase with tax-efficient income planning",
                            "Perth mining executive managing lumpy bonus income and super contributions"]
            },
            "Mexico": {
                "currencies": ["MXN", "USD"],
                "products": ["HSBC Premier Mexico", "USD accounts", "Mexican government bonds (CETES)",
                           "cross-border mortgages", "education savings accounts"],
                "challenges": ["MXN volatility", "cross-border US-Mexico wealth coordination",
                             "accessing international investment products", "US tax implications for dual nationals"],
                "goals": ["hedge against peso volatility with USD holdings", "fund children's US education",
                         "manage wealth across US-Mexico border", "build retirement savings in stable currencies"],
                "scenarios": ["Mexico City executive managing USD and MXN portfolios with cross-border property",
                            "Guadalajara entrepreneur preparing for business expansion to US market",
                            "Monterrey family with dual US-Mexico citizenship optimizing tax and wealth structure",
                            "Mexican professional relocating to US for career with wealth repatriation planning"]
            },
            "Canada": {
                "currencies": ["CAD", "USD"],
                "products": ["RRSP optimization", "TFSA maximization", "Canadian equity income portfolios",
                           "tripod wealth management model", "cross-border US-Canada planning"],
                "challenges": ["RRSP vs TFSA allocation decisions", "Canadian income tax rates",
                             "US estate tax for Canadians with US assets", "currency hedging CAD/USD"],
                "goals": ["maximize RRSP and TFSA contributions", "plan for Canadian retirement",
                         "manage cross-border US assets tax-efficiently", "build dividend income portfolio"],
                "scenarios": ["Toronto professional optimizing RRSP/TFSA strategy with employer matching",
                            "Vancouver family managing property wealth and retirement savings simultaneously",
                            "Calgary business owner with lumpy oil-sector income and wealth smoothing needs",
                            "Montreal investor with US real estate navigating cross-border estate tax implications"]
            },
            "Hong_Kong": {
                "currencies": ["HKD", "USD", "CNY", "GBP"],
                "products": ["Premier Elite HKD 7.8M+ tier", "Lombard lending via mobile app", "unit trusts via HSBC HK App",
                           "MPF optimization", "Greater Bay Area property financing"],
                "challenges": ["HKD peg to USD concentration", "property market affordability",
                             "MPF withdrawal restrictions", "managing mainland China family wealth connections"],
                "goals": ["reach Jade/Premier Elite tier from Premier", "diversify beyond HKD/HK property",
                         "leverage Greater Bay Area opportunities", "optimize MPF and offshore investments"],
                "scenarios": ["Hong Kong professional commuting to Shenzhen managing dual-jurisdiction wealth",
                            "HK family reaching Premier Elite tier accessing private banking-level solutions",
                            "Hong Kong entrepreneur with mainland China business coordinating cross-border wealth",
                            "HK expat preparing for repatriation to UK with multi-currency estate planning"]
            },
            "UAE": {
                "currencies": ["AED", "USD", "GBP", "EUR"],
                "products": ["HSBC Amanah Islamic banking", "sukuk investments", "offshore wealth structures",
                           "Dubai property financing", "Sharia-compliant portfolios"],
                "challenges": ["navigating Islamic finance vs conventional products", "residency visa wealth requirements",
                             "managing wealth for eventual repatriation", "Sharia compliance verification"],
                "goals": ["build Sharia-compliant investment portfolio", "leverage UAE tax advantages",
                         "manage international wealth flows through Dubai hub", "plan for post-expat repatriation"],
                "scenarios": ["Dubai expat leveraging UAE wealth center for cross-border EMEA-Asia investments",
                            "Abu Dhabi professional building 100% Sharia-compliant ESG portfolio",
                            "Emirati family establishing multi-generational trust with Islamic finance principles",
                            "Indian expat in UAE coordinating wealth across UAE-India-UK corridors"]
            },
            "UK": {
                "currencies": ["GBP", "USD", "EUR"],
                "products": ["Premier \u00a3100K+ threshold", "Jade integrated into Premier", "ISA (Stocks & Shares)",
                           "HSBC Onshore Investment Bond", "Future Planner tool", "UK pension drawdown"],
                "challenges": ["high Premier threshold (\u00a3100K income)", "inheritance tax planning",
                             "pension lifetime allowance considerations", "ISA contribution limits"],
                "goals": ["maximize ISA allowances tax-efficiently", "reach \u00a3100B AUM wealth manager target",
                         "optimize pension drawdown in retirement", "plan cross-border estate for children abroad"],
                "scenarios": ["London professional at St James's Wealth Centre accessing enhanced Premier benefits",
                            "Leeds family optimizing ISA contributions and pension planning for retirement",
                            "UK retiree with Spanish property planning cross-border estate and currency exposure",
                            "British expat returning from Hong Kong coordinating GBP/HKD wealth transfer"]
            },
            "Switzerland": {
                "currencies": ["CHF", "EUR", "USD", "GBP"],
                "products": ["Swiss Private Banking \u20ac5M minimum", "structured products platform",
                           "offshore wealth structures", "Swiss-based Asia desk", "Aladdin Wealth technology"],
                "challenges": ["FINMA regulatory compliance", "high minimum thresholds for private banking",
                             "navigating Swiss banking secrecy reforms", "wealth tax optimization across cantons"],
                "goals": ["access institutional-grade portfolio analytics", "leverage Switzerland as EMEA booking center",
                         "manage multi-currency European wealth", "establish Swiss-based family office structure"],
                "scenarios": ["Geneva private banking client with \u20ac15M AUM accessing Aladdin Wealth analytics",
                            "Zurich entrepreneur managing CHF/EUR exposure with cross-border business in Germany",
                            "Swiss family office consolidating assets through HSBC's 130-year heritage",
                            "International client using Swiss-based Asia desk to bridge EMEA and Asian portfolios"]
            },
            "Saudi_Arabia": {
                "currencies": ["SAR", "USD"],
                "products": ["HSBC Amanah Islamic banking", "sukuk issuance", "Sharia-compliant structured products",
                           "Saudi government bonds", "GCC project finance"],
                "challenges": ["100% Sharia compliance requirements", "Saudi capital market access for foreigners",
                             "Vision 2030 investment opportunities evaluation", "SAR/USD peg stability"],
                "goals": ["build entirely Sharia-compliant portfolio", "access Vision 2030 infrastructure projects",
                         "leverage Saudi market growth with Islamic principles", "manage Hajj/Umrah related wealth"],
                "scenarios": ["Riyadh businessman investing in Vision 2030 projects with sukuk allocations",
                            "Saudi family establishing Sharia-compliant multi-generational wealth structure",
                            "Jeddah entrepreneur balancing local SAR investments with USD diversification",
                            "Saudi professional accessing GCC sukuk markets through HSBC's 40% market share"]
            },
            "Qatar": {
                "currencies": ["QAR", "USD"],
                "products": ["HSBC Amanah products", "Qatar government bonds", "GCC sukuk",
                           "offshore banking unit services", "Sharia-compliant equity funds"],
                "challenges": ["Sharia compliance verification", "limited diversification in local market",
                             "QAR currency peg management", "regional GCC political considerations"],
                "goals": ["diversify beyond Qatar domestic market", "access international Islamic investments",
                         "manage wealth through largest foreign bank in Qatar", "plan for children's education abroad"],
                "scenarios": ["Doha professional accessing HSBC's three branches for cross-border Islamic banking",
                            "Qatar family diversifying QAR concentration with international sukuk portfolio",
                            "Qatari entrepreneur investing in GCC regional projects with Islamic finance",
                            "Expatriate in Qatar building Sharia-compliant retirement portfolio"]
            },
            "Bahrain": {
                "currencies": ["BHD", "USD", "SAR"],
                "products": ["offshore banking unit", "HSBC Amanah Islamic banking", "GCC sukuk",
                           "regional wealth management services", "Bahrain government bonds"],
                "challenges": ["small domestic market requiring regional diversification", "Sharia compliance standards",
                             "GCC market integration complexities", "BHD currency considerations"],
                "goals": ["access GCC regional investment opportunities", "leverage Bahrain's financial hub status",
                         "build diversified Islamic portfolio across GCC", "manage cross-border Gulf wealth"],
                "scenarios": ["Manama banker leveraging HSBC as largest foreign bank for regional investments",
                            "Bahraini family accessing GCC sukuk markets through three HSBC locations",
                            "Expat in Bahrain offshore banking unit managing international Sharia-compliant wealth",
                            "Bahraini investor diversifying across GCC markets with Islamic finance principles"]
            },
            "Malaysia": {
                "currencies": ["MYR", "USD", "SGD"],
                "products": ["HSBC Amanah Islamic banking hub", "Malaysian sukuk", "Bursa Malaysia equity funds",
                           "EPF (Employees Provident Fund) planning", "Islamic wealth management"],
                "challenges": ["MYR volatility", "Bumiputera policies and wealth implications",
                             "EPF withdrawal restrictions", "balancing Islamic and conventional products"],
                "goals": ["optimize EPF contributions", "build Sharia-compliant portfolio from Malaysia hub",
                         "manage MYR/SGD/USD currency exposure", "access HSBC Amanah 40% GCC sukuk market share"],
                "scenarios": ["Kuala Lumpur professional optimizing EPF and Islamic investment portfolio",
                            "Malaysian entrepreneur managing business sukuk issuance through HSBC Amanah",
                            "Penang family diversifying MYR concentration with SGD and USD Islamic investments",
                            "Malaysian expat in Singapore coordinating cross-border Islamic wealth management"]
            },
            "India": {
                "currencies": ["INR", "USD"],
                "products": ["HSBC Mutual Fund (14th largest)", "NRI banking services", "Indian equity funds",
                           "cross-border remittance services", "offshore investment for NRIs"],
                "challenges": ["INR volatility and capital controls", "NRI tax implications (FEMA regulations)",
                             "limited offshore investment options for residents", "navigating Indian inheritance laws"],
                "goals": ["optimize NRI tax status and investments", "access HSBC's 20 new branches expansion",
                         "manage India-Singapore-UK wealth corridors", "build diversified INR and USD portfolio"],
                "scenarios": ["Mumbai professional investing in HSBC Mutual Fund post-L&T acquisition",
                            "NRI in Singapore managing cross-border India property and investment portfolio",
                            "Bangalore tech worker with US employer stock options and INR/USD planning",
                            "Indian entrepreneur accessing HSBC's top foreign bank position for non-resident Indians"]
            },
            "USA": {
                "currencies": ["USD", "EUR", "GBP"],
                "products": ["US Private Banking $1.5M+ minimum", "Premier $100K minimum", "HSBC Wealth Track robo-advisor",
                           "401(k) and IRA accounts", "Addepar wealth platform", "managed accounts $250K minimum"],
                "challenges": ["US estate tax planning", "FATCA compliance for international clients",
                             "state tax variations", "required minimum distributions (RMD) at age 73"],
                "goals": ["optimize 401(k) and IRA contributions", "access Hudson Yards flagship wealth center",
                         "manage cross-border US-international wealth", "leverage Addepar institutional analytics"],
                "scenarios": ["New York professional at Hudson Yards accessing $65B private banking platform",
                            "California tech executive with RSU compensation and international portfolio needs",
                            "Florida retiree managing RMD strategy and cross-border estate planning",
                            "Washington DC family optimizing Premier relationship savings rates up to 3.40% APY"]
            }
        }

    def _initialize_wealth_tiers(self) -> Dict[str, Dict]:
        """Define HSBC's three wealth tiers with appropriate complexity and products"""
        return {
            "Premier": {
                "weight": 60,  # Largest customer base (54M globally in Wealth & Personal Banking)
                "asset_range": (75000, 1000000),
                "income_range": (75000, 300000),
                "complexity": "moderate",
                "description": "Mass affluent - internationally mobile professionals, expats",
                "products": [
                    "Premier savings accounts", "multi-currency accounts", "international transfers",
                    "mutual funds and ETFs", "target-date funds", "online investment platforms",
                    "mortgage products", "Premier credit cards", "travel benefits (LoungeKey)",
                    "basic investment advisory", "retirement accounts (401k/IRA/ISA/CPF)",
                    "education savings (529/RESP)", "currency exchange", "Premier relationship manager"
                ],
                "typical_needs": [
                    "building wealth from salary", "first-time international investing",
                    "mortgage for property purchase", "children's education planning",
                    "understanding tax-advantaged accounts", "basic diversification",
                    "currency management across 2-3 countries", "career relocation support",
                    "aspiring to reach Jade/Premier Elite tier"
                ],
                "communication_style": "educational, encouraging, building confidence, simplifying concepts"
            },
            "Jade_Premier_Elite": {
                "weight": 30,  # HNW segment (~150K Jade globally)
                "asset_range": (1000000, 5000000),
                "income_range": (250000, 1000000),
                "complexity": "sophisticated",
                "description": "High net worth - business owners, established professionals, multi-gen wealth",
                "products": [
                    "Premier Elite services (HK HKD 7.8M+ tier)", "alternative investments access",
                    "private equity funds", "hedge fund access", "structured products",
                    "Lombard lending (securities-based)", "trust structures", "estate planning",
                    "family trust services", "concentrated stock position management",
                    "tax optimization strategies", "philanthropic vehicles", "business succession planning",
                    "international property financing", "art/collectibles financing",
                    "dedicated wealth teams (avg 16+ years experience)", "Elite Health Advantage"
                ],
                "typical_needs": [
                    "accessing alternative investments", "managing business sale proceeds",
                    "trust and estate planning", "multi-generational wealth transfer",
                    "ESG portfolio alignment", "concentrated position diversification",
                    "family governance structures", "philanthropic strategy",
                    "international tax optimization", "succession planning for family business",
                    "evaluating private equity/hedge funds", "considering Private Banking tier"
                ],
                "communication_style": "sophisticated but accessible, strategic, partnership-oriented, nuanced"
            },
            "Global_Private_Banking": {
                "weight": 10,  # UHNW (~60% of Private Banking revenue globally)
                "asset_range": (5000000, 100000000),
                "income_range": (500000, 10000000),
                "complexity": "highly_complex",
                "description": "Ultra-high net worth - family offices, entrepreneurs, complex cross-border",
                "products": [
                    "Global Private Banking ($5M+ minimum, $2M+ in select markets)",
                    "family office advisory", "multi-skilled wealth teams",
                    "institutional-grade analytics (Aladdin Wealth)", "bespoke lending solutions",
                    "art and trophy asset financing", "private market investments",
                    "complex trust structures (generation-skipping, charitable remainder)",
                    "offshore wealth structures", "multi-jurisdictional estate planning",
                    "private equity co-investments", "direct infrastructure investments",
                    "hedge fund platforms", "derivatives and sophisticated hedging",
                    "concierge services", "global citizenship/residency planning",
                    "impact investing mandates", "family governance frameworks",
                    "succession and legacy planning", "philanthropic foundations"
                ],
                "typical_needs": [
                    "managing post-exit liquidity ($50M+ events)", "family office setup/transition",
                    "complex multi-jurisdictional tax structures", "protecting wealth across generations",
                    "sophisticated alternative allocations (30-50%)", "private market investments",
                    "regulatory change protection", "next-gen wealth education",
                    "impact/sustainable investing at scale", "art as asset class",
                    "global citizenship optimization", "managing illiquid private equity positions",
                    "coordinating with external advisors (lawyers, accountants, family office staff)"
                ],
                "communication_style": "highly sophisticated, concise, assumes knowledge, collaborative with other advisors"
            }
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
            self._generate_hsbc_specific_scenario,  # HSBC-specific scenarios
            self._generate_market_specific_scenario,  # Geographic market scenarios
            self._generate_market_specific_scenario,  # Double weight for geographic diversity
            self._generate_tier_specific_scenario,    # Wealth tier scenarios
            self._generate_tier_specific_scenario,    # Double weight for tier diversity
            self._generate_tier_specific_scenario     # Triple weight for tier diversity
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

    def _generate_market_specific_scenario(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate geographically-specific scenarios across HSBC's key markets"""
        family = random.choice(persona.family_situations)
        savings = random.randint(max(income // 2, 50000), income * 4)

        # Revenue-based weighting for market selection
        # Based on HSBC's business revenue, strategic importance, and AUM
        market_weights = {
            "Hong_Kong": 25,      # $9.1B PBT, 28% of group profit, #1 position
            "UK": 15,             # 15M customers, £100B AUM target, home market
            "Singapore": 12,      # International wealth hub, 76% YoY growth
            "China": 10,          # 61% growth, mainland expansion priority
            "Switzerland": 8,     # $153B booking center, largest foreign private bank
            "UAE": 8,             # $1B annual profit, top-5 market, 24k sqft wealth center
            "USA": 6,             # $65B private banking AUM
            "Canada": 5,          # "Jewel in crown", doubling private client base
            "Australia": 4,       # APAC presence
            "India": 3,           # 20 new branches, 14th largest fund house
            "Mexico": 3,          # MXN 811.9B assets, 3 new wealth centers
            "Malaysia": 3,        # HSBC Amanah hub, Islamic banking center
            "Indonesia": 2,       # Best Wealth Manager 7 consecutive years
            "Saudi_Arabia": 2,    # GCC sukuk leader, Vision 2030 opportunity
            "Qatar": 1,           # Largest foreign bank, 3 branches
            "Bahrain": 1,         # Largest foreign bank, offshore unit
        }

        # Weighted random selection
        markets = list(market_weights.keys())
        weights = list(market_weights.values())
        market_name = random.choices(markets, weights=weights, k=1)[0]
        market = self.markets[market_name]

        # Get market-specific elements
        currencies = ", ".join(random.sample(market["currencies"], min(2, len(market["currencies"]))))
        product = random.choice(market["products"])
        challenge = random.choice(market["challenges"])
        goal = random.choice(market["goals"])
        scenario_base = random.choice(market["scenarios"])

        # Format market name for display
        market_display = market_name.replace("_", " ")

        templates = [
            f"{age}-year-old in {market_display}, {family}, {currencies} currency exposure. {income:,} annual income, {savings:,} in assets. {scenario_base}. Need help with {challenge}.",
            f"{age} years old, based in {market_display}, {family}. Managing {currencies} portfolios, ${income:,} income. Goal: {goal}. Considering {product} but needs simple explanation.",
            f"{age}-year-old {market_display}-based client, {family}, ${income:,} income, ${savings:,} saved. Wants to {goal} using {product}. Challenge: {challenge}.",
            f"{age} years old in {market_display}, {family}. ${income:,} annual income, ${savings:,} portfolio across {currencies}. Struggling with {challenge}, wants to {goal}.",
            f"{age}-year-old client in {market_display}, {family}, ${income:,} income. {scenario_base}. Interested in {product} to {goal}.",
        ]

        return random.choice(templates)

    def _generate_tier_specific_scenario(self, persona: ClientPersona, age: int, income: int) -> str:
        """Generate scenarios with appropriate complexity based on wealth tier"""

        # Select wealth tier with weighted distribution
        tier_names = list(self.wealth_tiers.keys())
        tier_weights = [self.wealth_tiers[t]["weight"] for t in tier_names]
        tier_name = random.choices(tier_names, weights=tier_weights, k=1)[0]
        tier = self.wealth_tiers[tier_name]

        # Adjust income/assets to tier
        tier_income = random.randint(*tier["income_range"])
        tier_assets = random.randint(*tier["asset_range"])

        # Select tier-appropriate products and needs
        product = random.choice(tier["products"])
        need = random.choice(tier["typical_needs"])

        # Format tier name for display
        tier_display = tier_name.replace("_", " ")

        family = random.choice(persona.family_situations)

        # Adjust scenario complexity based on tier
        if tier["complexity"] == "moderate":
            # Premier: Educational, straightforward
            templates = [
                f"{age}-year-old {tier_display} client, {family}, ${tier_income:,} income, ${tier_assets:,} in assets. {need}. Needs help understanding {product}.",
                f"{age} years old, {family}, {tier_display} tier (${tier_assets:,} portfolio). ${tier_income:,} annual income. Goal: {need}. Confused about {product}.",
                f"{age}-year-old {family}, earning ${tier_income:,}, ${tier_assets:,} saved. Currently {tier_display} client. Wants to {need} using {product}. Needs simple explanation.",
            ]
        elif tier["complexity"] == "sophisticated":
            # Jade/Premier Elite: More complex, strategic
            templates = [
                f"{age}-year-old {tier_display} client, {family}, ${tier_income:,} income, ${tier_assets:,} AUM. {need}. Evaluating {product} - need strategic guidance on implementation.",
                f"{age} years old, {family}, {tier_display} tier with ${tier_assets:,} portfolio. ${tier_income:,} annual income. Working on {need}. Considering {product} - want to understand optimal structure.",
                f"{age}-year-old {family}, ${tier_income:,} income, ${tier_assets:,} in assets. {tier_display} client. {need}. Exploring {product} - need sophisticated analysis of trade-offs.",
            ]
        else:  # highly_complex
            # Private Banking: Highly sophisticated, assumes knowledge
            templates = [
                f"{age}-year-old {tier_display} client, {family}, ${tier_income:,} annual income, ${tier_assets:,} AUM. {need}. Require guidance on {product} integration with existing structure. Coordinating with external tax counsel.",
                f"{age} years old, {family}, ${tier_assets:,} AUM across {tier_display}. ${tier_income:,} income. {need}. {product} being evaluated - need analysis of tax implications and liquidity considerations.",
                f"{age}-year-old UHNW {family}, ${tier_income:,} income, ${tier_assets:,} AUM. {tier_display} client. {need}. {product} under consideration - seeking institutional-grade analytics and multi-jurisdictional perspective.",
            ]

        return random.choice(templates)

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
