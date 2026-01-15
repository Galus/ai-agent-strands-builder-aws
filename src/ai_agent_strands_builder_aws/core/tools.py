from strands import Agent, tool


@tool
def galus_custom_riddle_tool() -> str:
    import random

    riddles = [
        {
            "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "answer": "An echo",
        },
        {
            "question": "The more of this there is, the less you see. What is it?",
            "answer": "Darkness",
        },
        {
            "question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
            "answer": "A map",
        },
        {
            "question": "What can travel around the world while staying in a corner?",
            "answer": "A stamp",
        },
        {
            "question": "I'm tall when I'm young, and I'm short when I'm old. What am I?",
            "answer": "A candle",
        },
        {
            "question": "What has keys but no locks, space but no room, and you can enter but can't go inside?",
            "answer": "A keyboard",
        },
        {"question": "What gets wet while drying?", "answer": "A towel"},
        {
            "question": "I have branches, but no fruit, trunk, or leaves. What am I?",
            "answer": "A bank",
        },
        {
            "question": "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?",
            "answer": "A river",
        },
        {
            "question": "The more you take, the more you leave behind. What are they?",
            "answer": "Footsteps",
        },
    ]
    riddle = random.choice(riddles)
    print(f"Chose random riddle: {riddle}")
    msg: str = f"question: {riddle['question']} answer: {riddle['answer']}"
    return msg


@tool
def investment_research_assistant(query: str) -> str:
    investment_researcher = Agent(
        model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        system_prompt="""
        You are a financial research analyst who helps users explore various investment opportunities.
        You specialize in providing insights into stocks, ETFs, mutual funds, bonds, and other instruments.
        You also highlight key market trends, risk factors, and historical performance.
        Your goal is to equip users with comprehensive, objective information to support their investment decisions.
        """,
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
        """,
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
        """,
    )
    msg = str(financial_planner(query).message)
    return msg
