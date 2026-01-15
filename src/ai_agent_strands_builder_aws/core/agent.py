from strands import Agent, tool
from strands_tools import python_repl, file_write, use_aws, http_request
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

def weather(citydatetime: str):
    system_prompt = """
    You are a weather data agent. Your job is to fetch weather details for a given city and date/time by searching publicly available weather information on the web.
    [Instructions]
    - Use HTTP GET to query a public weather website or API (e.g. hgttps://wttr.in) with city and date parameters.
    - Extract weather details such as temperature, conditions, humidity, wind speed, and date/time from the response.
      - Save these weather details into an existing DynamoDB table named "CityWeatherData" in us-east-1
      - Use 'City' as the partition key and 'DateTime' as the sort key.
      - Store other extracted weather details as attributes.
    - If live data is unavailable or blocked, simulate realistic weather data for testing.
    """

    example_url = """
    Example: To get weather in San Francisco for today, query:
    https://wttr.in/San+Francisco?format=j1
    This returns JSON with weather details.
    """

    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
    agent = Agent(
        tools=[use_aws, http_request],
        system_prompt=system_prompt,
        model=model
    )
    resp = agent(f"Get the weather details for {citydatetime} and save to DynamoDB")
    print(resp)

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
    resp = agent(symbol)
    print(resp)

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

