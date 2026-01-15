GALUS NOTE:
This kind of shows the danger of prompts.
We pass in 3 tools, not mentioned by the system prompt:

Code:

> def multi_agent_finance_orchestrator():
>     MAIN_SYSTEM_PROMPT = """
>     You are an assistant that routes queries to specialized agents:
>     - For research questions and factual information, Use the research_assistant tool
>     - For product recommendations and shopping advice, Use the product_recommendation_assistant tool
>     - For travel planning and itineraries, Use the trip_planning_assistant tool
>     - For simple questions not requiring specialized knowledge, Answer directly
>     Always select the most appropriate tool based on the user's query.
>     """
>     orchestrator = Agent(
>         system_prompt=MAIN_SYSTEM_PROMPT,
>         tools=[
>             investment_research_assistant,
>             budget_optimizer_assistant,
>             financial_planner_assistant,
>         ],
>     )
> 
>     resp = orchestrator(
>         """
>         I'm 30 years old, earning around $6,000 per month.
>         I have some student loans and moderate savings.
>         I want to understand how I can better manage my monthly budget,
>         explore investment options, and build a solid long-term financial plan
>         for buying a house and retiring early. Can you help?
>         """
>     )
>     print(resp)

System Prompt expects:

- research_assistant
- product_recommendation_assistant
- trip_planning_assistant

We provide Tools:

- investment_research_assistant
- budget_optimizer_assistant
- financial_planner_assistant

Still works out. But with an uneasy feeling.
Output seems to be heavily compressed or the LLM became stupid.
Output is truncated and grammatically unwell.

---

Actual output:

Hello from ai-agent-strands-builder-aws!
Running the multi agent finance orchestrator. Expecting it to fail.
I'll help you with your comprehensive financial planning needs by consulting our specialized financial assistants. Let me gather insights on budget management, investment options, and long-term financial planning for your goals.
Tool #1: budget_optimizer_assistant

Tool #2: investment_research_assistant

Tool #3: financial_planner_assistant
I'll help you create a structureI'll help you create a comprehensive financiald budgetI'll help you develop plan. a comprehensive Let plan that bal's breakances your current investment strategy base obligations with your long- this down into key areasterm goals and on your situationd create. Let's break a strategic roadmap. this down into several. Let's break this down:

First, let's follow the 50/30/20  key areas:

1rule as. Priority Financial Steps First a baseline

First:, let me gather some additional important
- details:: Emergency
1
-. How 50% for needs much do you have
- 30% Fund: Ensure you have  for wants
- in student loan debt an 20% for savings/3-6 months of expenses saved in a high-yield at what interest rate?
2. Whatdebt repayment

Base ared on your $d savings account
- Student Loan Management your current6,000  savings (emergencymonthly income:
- Needs: Review ( interest rates; if above fund, retirement accounts, other savings50%): $3,)?
3. What's000
- your current monthly expense Wants (30%): $1, 6%, prioritize paying these down
- 401(k) Match800 breakdown?
- Savings: If your employer offers matching/Debt (,20%): $1,200

While waiting for those contribute enough to get the full match ( details, here's

Recommendeit an initial framework's free money)d monthly allocation for:

Immediate NEEDS ($3,000):
-

2. Suggested Asset Allocation (Given your Rent/Housing Priority Actions (Next age an 6: $1,d goals500-12 months):
1. Emergency):
- 80-1,800
- Fund Utilities: $200
- Target:--85 % Stocks (higher growth potential3003-6 months of expenses
- Groceries: $
-400-500 Alloc
- Student Loan for long-term goalsate 20% Payment: $400-500
- Insurance of monthly income ($1,200) until reached

2. Student)
- 15-20% Bonds (for stability)
- Consider: $200
- Transportation: $200-300 reducing stock exposure

Strategies Loan Strategy
- Review refinancing options if interest to optimize your budget: rate is high

1. as you get closer to your house purchase goal

3. Debt Management
- Implement debt aval: Specific Investment Vehicles:

For Retirement
- Prioritize paying off highanche or snowball method
- Allocate ~-interest student loans
- Consider refin:
- 401(k): Maximize employer match
- Roth25ancing for% of monthly income to debt repayment

Mi IRA: Considerd-Term Goals ( better rates
- Alloc2-5 years)ate any win - opening one ($6,000 annual limit)
- Targetdfalls (tax returns House Purchase: date, bonuses) funds to debt reduction like

2. V Saving for Houseanguard Target
- Recommende Down Payment:
- Opend down payment: 20% a high Retirement 2055 (-yield savings account
- Aim of target house price
- Start house fun to save at least $VFFVX) for hands-off management

For House Downd with 15% of monthly income Payment (5-7500/month specifically for house down payment
- ($900)
- Timeline dependent Consider cutting some on target house price and market year "wants" temporarily horizon):
- More conservative allocation

Long-Term Planning to
- Short (5+ years) accelerate savings

3. Early-term bond funds (e Retirement Planning: - Early Retirement:
- Maximize
-.g., VBIR retirement accounts (401 Maximize( employer k), IRA401(k))X)
- High-yield savings accounts match
- Aim if available for 15-20% of income towar
- CD ladders

Core Portfolio Components
- Open a Roth IRA
- Aim for 15%d retirement
- Consider of income towar additional:
1. Low-cost index funds investmentd retirement

Cost vehicles-

WoulCutting Tips:d you please:
- Total US Market
1 ( provide thosee.g., V. Review subscriptions and cancelT unnecessary ones additional details soI or I can create a more tailored plan F
2. with Meal prep to specificSKAX)
- International reduce food costs
3. Use cash numbers Exposure (e.g., VX and timelines?back credit cards strategically
4.US)
- Bond Index Consider (e.g a., B roomND)

4mate to reduce housing costs. Suggested Monthly
5. Shop for better insurance rates annually

Woul Investment Strategy:
- Emergency Fund: d you like me20 to dive deeper into any of these areas% until fully funded
- 401(k): At or help you create a more detaile least enoughd budget base ford on your specific expenses full employer match
- Roth IRA: Try to max out annually? ($500/month)
- House Down Payment Fund: Separate account with more conservative investments

5. Risk Management:
- Diversify across asset classes
- Regular rebalancing
- Increase bond allocation as you near your house purchase goal

Would you like me to elaborate on any of these areas or provide more specific fund recommendations?Based on the comprehensive analysis from our financial specialists, here's your personalized roadmap for better financial management:

## **Budget Optimization Strategy**

**Monthly Income Allocation ($6,000):**
- **Needs (50%)**: $3,000 - Housing, utilities, groceries, student loans, insurance, transportation
- **Wants (30%)**: $1,800 - Entertainment, dining out, hobbies, discretionary spending
- **Savings/Debt (20%)**: $1,200 - Emergency fund, debt repayment, and goal-specific savings

**Key Budget Optimization Tips:**
- Review and cancel unnecessary subscriptions
- Meal prep to reduce food costs
- Consider a roommate to lower housing expenses
- Use cashback credit cards strategically

## **Investment Strategy**

**Recommended Asset Allocation:**
- **80-85% Stocks** (for long-term growth)
- **15-20% Bonds** (for stability)

**Investment Vehicles:**
1. **401(k)** - Maximize employer match first
2. **Roth IRA** - Up to $6,000 annually ($500/month)
3. **Index Funds** - VTI (Total US Market), VXUS (International), BND (Bonds)
4. **House Fund** - More conservative investments in high-yield savings or short-term bonds

## **Long-Term Financial Plan**

**Phase 1 (Next 6-12 months) - Foundation Building:**
- Build emergency fund (3-6 months expenses)
- Optimize student loan payments
- Establish investment accounts

**Phase 2 (2-5 years) - House Purchase Preparation:**
- Dedicate $900/month to house down payment fund
- Target 20% down payment
- Maintain credit score optimization

**Phase 3 (5+ years) - Early Retirement Acceleration:**
- Aim for 15-20% income toward retirement
- Maximize tax-advantaged accounts
- Consider additional investment vehicles

## **Next Steps**

To create a more specific plan, it would be helpful to know:
1. Your exact student loan balance and interest rates
2. Current savings amounts
3. Target home price range
4. Desired early retirement age

This framework gives you a solid foundation to work with. Would you like me to dive deeper into any specific area or help you refine the plan based on additional details about your situation?Based on the comprehensive analysis from our financial specialists, here's your personalized roadmap for better financial management:

## **Budget Optimization Strategy**

**Monthly Income Allocation ($6,000):**
- **Needs (50%)**: $3,000 - Housing, utilities, groceries, student loans, insurance, transportation
- **Wants (30%)**: $1,800 - Entertainment, dining out, hobbies, discretionary spending
- **Savings/Debt (20%)**: $1,200 - Emergency fund, debt repayment, and goal-specific savings

**Key Budget Optimization Tips:**
- Review and cancel unnecessary subscriptions
- Meal prep to reduce food costs
- Consider a roommate to lower housing expenses
- Use cashback credit cards strategically

## **Investment Strategy**

**Recommended Asset Allocation:**
- **80-85% Stocks** (for long-term growth)
- **15-20% Bonds** (for stability)

**Investment Vehicles:**
1. **401(k)** - Maximize employer match first
2. **Roth IRA** - Up to $6,000 annually ($500/month)
3. **Index Funds** - VTI (Total US Market), VXUS (International), BND (Bonds)
4. **House Fund** - More conservative investments in high-yield savings or short-term bonds

## **Long-Term Financial Plan**

**Phase 1 (Next 6-12 months) - Foundation Building:**
- Build emergency fund (3-6 months expenses)
- Optimize student loan payments
- Establish investment accounts

**Phase 2 (2-5 years) - House Purchase Preparation:**
- Dedicate $900/month to house down payment fund
- Target 20% down payment
- Maintain credit score optimization

**Phase 3 (5+ years) - Early Retirement Acceleration:**
- Aim for 15-20% income toward retirement
- Maximize tax-advantaged accounts
- Consider additional investment vehicles

## **Next Steps**

To create a more specific plan, it would be helpful to know:
1. Your exact student loan balance and interest rates
2. Current savings amounts
3. Target home price range
4. Desired early retirement age

This framework gives you a solid foundation to work with. Would you like me to dive deeper into any specific area or help you refine the plan based on additional details about your situation?

Done running.

