from strands import Agent, tool
from strands_tools import python_repl, file_write
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

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

