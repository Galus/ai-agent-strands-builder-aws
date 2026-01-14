from strands import Agent, tool
from strands_tools import python_repl, file_write
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

def price_analysis(symbol: str):
    system_prompt = """
    You are a financial analyst. Provide following charts:
    - Plot 20-days moving average of closing prices for the past one year.
    - Plot daily return rate comparison against S&P500 for the same period.
    Also, compute following two metrics of the stock:
      - Volatility of the return rates
    Use `yfinance` module to retrive the historical data.
    Save the plots as image files {symbol}_{date}_{plot_name}.jpg
    """
    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
    agent = Agent(
        tools=[python_repl, file_write],
        system_prompt=system_prompt,
        model=model
    )
    response = agent(symbol)

def scrape():
    agent = Agent(tools=[python_repl, file_write])
    prompt = """
    Where N = 5
    Get the titles and links of N articles listen in https://news.ycombinator.com/news.
    When you execute a python script, make sure to run it in non-iteractive mode.
    Write the results as CSV file names news_{date}.csv.
    """
    resp = agent(prompt)
    print(resp)

def test():
    agent = Agent()
    resp = agent("Explain Amazon Bedrock Agents")
    print(resp)

