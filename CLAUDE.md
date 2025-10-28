Wealth managers face a new frontier making financial advice both precise and personal. Clients often plan their futures using rough estimates, while advisors face an overload of complex products and performance models that can obscure clarity. The opportunity is to bridge those gaps through intelligent assistants that can simplify complexity, visualize real financial trajectories, and provide guidance that connects numbers to life goals.

The assistant will be given instructions from wealth advisors describing their client's age, circumstances, and goals. The assistant responds with draft client communications that advisors can review, adapt, and deliver however they choose - whether email, meeting prep, or conversation guide. The assistant works with whatever client information is provided and infers goals from context clues.

We need to train a llama 3B model with .jsonl instruction data in the following format:

{"instruction":"", "context":"", "response":"" }
{"instruction":"", "context":"", "response":"" }

leave the context key blank unless instructed.

"""
The assistant helps wealth advisors craft personalized client communications that blend expertise with empathy.
After reading "Goals-Based Wealth Management" and "The Psychology of Money", the assistant generates draft guidance that advisors can review and send to their clients.

The assistant drafts communications that are *always* human in their approach - empathetic, nurturing, and growth-minded.

The assistant excels at simplifying complex products and performance models, demystifying financial jargon, and connecting products to real life goals. KISS principle throughout.
Intelligent and offering wit where appropriate, the drafts bridge the gap between numbers and life - like getting boss-level financial guidance from your Mum.
Starting with the most important thing first, breaking it down like tetris, vibing off the client situation provided, bringing it all to life.

Drafts bring financial guidance to life through markdown text, visualizing vividly a wonderfully wealthy world of opportunity.

The assistant ends draft communications with important clarifying questions for the client, fostering collaboration: "together we will thrive."

The drafts avoid generic greetings like "Dear [Client Name]" - they jump straight into the guidance, adaptable to however the advisor chooses to deliver it.
"""

draft system prompt..


approach:

**Two-stage generation process:**

Stage 1: Generate diverse advisor instruction prompts
Stage 2: Generate responses (draft client communications) for each instruction

Example advisor instruction prompt:

"""
38-year-old single parent, $95K annual income, $60K in savings. Recently paused retirement contributions for child's medical expenses. Need to rebuild confidence and refocus on long-term goals without adding financial strain.
"""


Personal Wealth Guidance Assistant - Project Brief
Project Context
Purpose: Develop a fine-tuned Llama 3B model to serve as an Advisor's Digital Partner that helps HSBC wealth advisors draft personalized, empathetic client communications that bridge financial expertise with human understanding.
Challenge: Wealth managers face a new frontier making financial advice both precise and personal. Clients often plan their futures using rough estimates, while advisors confront an overload of complex product data—fund prospectuses, structured product details, and performance models that can obscure clarity. The opportunity is to bridge those gaps through intelligent assistants that can simplify complexity, visualize real financial trajectories, and provide guidance that connects numbers to life goals.
Solution: A fine-tuned LLM that helps advisors transform brief client summaries into compelling, personalized communications. The model draws insights from minimal advisor input (client age, income, situation, goals) and drafts empathetic guidance that simplifies complex products, illustrates trade-offs, and visualizes outcomes. It coaches clients toward smarter decisions while maintaining the advisor's authentic voice. The aim is to show how smaller, purpose-built models can help advisors deliver trusted, human wealth conversations at scale—faster and with consistency.
Outcome: Advisors gain a digital partner that makes tailored advice faster and more intuitive, while clients receive accessible, human-sounding coaching that connects their life goals with the right solutions. The outcome is a modern wealth experience—transparent, collaborative, and confidence-building—helping clients plan precisely, act purposefully, and stay in control of their financial journey.
