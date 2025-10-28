# HSBC-Specific Improvements to Training Data Generator

## Overview
Updated the synthetic data generator to create more diverse, creative, and representative scenarios based on HSBC's actual wealth management business.

## Research Findings

### HSBC Wealth Segments
1. **HSBC Premier** - Mass Affluent ($250K-$1M assets)
2. **HSBC Jade** - Affluent ($1M-$5M assets)
3. **HSBC Private Banking** - HNW/UHNW ($5M+ assets)

### Key Business Focus Areas
- **Cross-border wealth management** (Hong Kong-Singapore, Asia-Middle East corridors)
- **Greater Bay Area Wealth Connect**
- **Sustainable/ESG investing** (founding member of One Planet Asset Manager Initiative)
- **International client base** (6.7M international clients, 12% YoY growth)
- **Business owners & entrepreneurs** (Private Wealth Entrepreneur programme)
- **Multi-generational wealth transfer**

## Major Updates to `generate_training_data.py`

### 1. Updated Client Personas (8 new segments)

**Before:** 5 generic life stages (Early Career, Mid Career, etc.)

**After:** 8 HSBC-specific wealth segments:
- Premier Mass Affluent (expats, international professionals)
- Jade Affluent (business owners, family office clients)
- Private Banking HNW/UHNW (sophisticated estate planning, impact investing)
- Emerging Wealth (tech workers with equity comp, startup founders)
- International Cross-Border (managing wealth across 3+ countries)
- Entrepreneurs (business exit planning, succession)
- Sustainable Wealth (ESG-focused, impact investors)
- Wealth Preservation (retirees with cross-border estates)

### 2. Enhanced Financial Products

**Added HSBC-specific products:**
- Cross-border: Greater Bay Area wealth connect, multi-currency accounts, currency hedging
- Sustainable: ESG funds, green/social bonds, SDG-aligned funds, climate solutions
- Alternative: Private equity, hedge funds, art financing
- Business: Stock option planning, RSU/ISO strategies, family office setup
- Tax: Multi-jurisdictional optimization, expatriate tax planning, FATCA compliance

### 3. New HSBC-Specific Scenario Generator

Added 25+ unique HSBC scenario templates across:

**Cross-Border Scenarios:**
- Hong Kong to Singapore relocations
- Managing wealth across UK-HKD-SGD currencies
- Greater Bay Area Wealth Connect participation
- Repatriation to mainland China after years abroad
- London to Dubai relocations

**Tier Progression:**
- Premier clients approaching Jade threshold
- Jade clients considering Private Banking transition

**ESG & Sustainable Investing:**
- Transitioning entire portfolio to ESG-aligned investments
- SDG-aligned emerging market bonds
- Donor-advised funds for systematic philanthropy
- Concerns about greenwashing

**Business Owner Scenarios:**
- Pre-exit liquidity planning
- Serial entrepreneurs with lumpy income
- Multi-sibling family business succession

**Equity Compensation:**
- RSU diversification and tax planning
- ISO exercise deadline decisions
- Concentrated employer stock positions

**International Education:**
- US/UK university funding with currency risk
- Education trusts for grandchildren across countries

**Alternative Investments:**
- Private equity allocation for Jade clients
- Art financing and collectibles for UHNW

**Multi-Generational Wealth:**
- Family governance frameworks
- Next-gen demanding ESG alignment
- Customized sub-portfolios for different risk tolerances

## Example Instructions Generated

### Before (Generic):
```
I'm 38 years old, single parent, earning $95,000 annually. I want to save for first home. Where should I start?
```

### After (HSBC-Specific):
```
37-year-old dual-income international professionals, $182,000 income. Participating in Greater Bay Area Wealth Connect. Wants to understand investment limits, eligible products, and cross-border tax treatment.
```

```
54-year-old expat in UAE or Singapore hub, managing $4,351,068 multi-generational family wealth. Three adult children with different risk tolerances and ESG preferences. Need family governance framework and customized sub-portfolios.
```

```
32-year-old tech professional, startup founder post-funding, $248,000 base salary plus $124,000 in RSUs vesting annually. 60% of net worth concentrated in employer stock. Need diversification strategy and tax planning.
```

## Impact on Training Data Quality

### Diversity Metrics
- **Personas:** 5 → 8 (+60%)
- **Product categories:** 7 → 10 (+43%)
- **Scenario templates:** ~12 → 37+ (+208%)
- **Geographic coverage:** US-only → Global (HK, SG, UAE, UK, CN, US)

### Realism Improvements
- Income ranges match HSBC wealth segments ($120K-$3M vs $40K-$200K)
- Asset levels reflect actual client tiers ($250K-$5M+ vs generic savings)
- Challenges reflect real HSBC client issues (cross-border tax, currency hedging, ESG alignment)
- Products align with HSBC's actual offerings (GBA Wealth Connect, private markets for Jade, etc.)

### Coverage of HSBC Strategic Priorities
✅ Cross-border wealth management
✅ Asia-Middle East corridors
✅ Sustainable/ESG investing
✅ Business owner/entrepreneur focus
✅ International education planning
✅ Multi-generational wealth transfer
✅ Alternative investments for HNW
✅ Tier progression strategy

## Sample Output Quality

**Instruction:**
```
59-year-old serial entrepreneur with multiple ventures, $805,000 annual income.
Wants to transition from working capital to invested capital.
```

**Response highlights:**
- No "Dear Client" greeting ✅
- Empathetic acknowledgment of entrepreneur mindset ✅
- Simplified complex concepts (concentration risk, tax shelters) ✅
- Specific action steps with timeline ✅
- Visualized outcome (5-10 year projection) ✅
- Ends with clarifying questions ✅
- Concludes with "Together, we will thrive." ✅

## Next Steps

1. Generate full dataset (100 instructions → responses)
2. Analyze distribution across personas and scenario types
3. Consider adding region-specific variations (Asia vs Middle East vs UK)
4. Potentially expand to 200-500 samples for better model coverage
