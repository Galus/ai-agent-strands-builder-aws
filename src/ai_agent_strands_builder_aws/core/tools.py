from strands import Agent, tool

@tool
def investment_research_assistant(query: str) -> str:
    investment_researcher = Agent(
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        system_prompt="""
        You are a financial research analyst who helps users explore various investment opportunities.
        You specialize in providing insights into stocks, ETFs, mutual funds, bonds, and other instruments.
        You also highlight key market trends, risk factors, and historical performance.
        Your goal is to equip users with comprehensive, objective information to support their investment decisions.
        """
    )
    msg = str(investment_researcher(query).message)
    return msg


@tool
def budget_optimizer_assistant(query: str) -> str:
    budget_optimizer = Agent(
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        system_prompt="""
        You are a smart budgeting assistant who helps users manage and optimize their monthly expenses.
        You analyze income, spending patterns, and savings goals, and suggest personalized recommendations
        to cut unecessary costs and improve savings. Your goal is to help users maintain a healthy financial balance.
        """
    )
    msg = str(budget_optimizer(query).message)
    return msg

@tool
def financial_planner_assistant(query: str) -> str:
    financial_planner = Agent(
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        system_prompt="""
        You are a certified financial advisor bot who helps users create customized financial plans 
        based on their goals, income, age, and risk tolerance.
        You guide them through budgeting, saving, debt management, insurance, and retirement planning.
        Your goal is to provide practical, step-by-step advice to help users achieve financial stability and growth.
        """
    )
    msg = str(financial_planner(query).message)
    return msg

