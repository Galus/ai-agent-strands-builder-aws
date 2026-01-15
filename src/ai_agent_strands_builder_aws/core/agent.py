from strands import Agent, tool
from strands_tools import python_repl, file_write, use_aws, http_request
from ai_agent_strands_builder_aws.core.tools import (
    investment_research_assistant,
    budget_optimizer_assistant,
    financial_planner_assistant,
    galus_custom_riddle_tool,
)
from ai_agent_strands_builder_aws.core.clients import aws_diag_client
import os
from IPython.display import Image, display


os.environ["BYPASS_TOOL_CONSENT"] = "true"

diagram_dir = "./aigen/diagrams"
os.makedirs(diagram_dir, exist_ok=True)


def mcp_agent():
    SYSTEM_PROMPT = """
    You are an expert AWS Certified Solutions Architect. Your role is to help customers understand best practices on building on AWS.
    You can query the AWS Documentation and generate diagrams. When you generate a diagram,
    you MUST tell the customer the full file path of the diagram in the format "The diagram is saved at: <filepath>".
    """
    with aws_diag_client:
        all_tools = aws_diag_client.list_tools_sync()
        agent = Agent(tools=all_tools, system_prompt=SYSTEM_PROMPT)
        query = "Create a diagram of a website that uses AWS Lambda for a static website hosted on S3"
        print(f"Sending query to agent: {query}")

        agent_result = agent(query)

        # Extract textual content from agent_result
        final_agent_response_text = ""
        if hasattr(agent_result, "response") and isinstance(agent_result.response, str):
            final_agent_response_text = agent_result.response
        elif hasattr(agent_result, "content") and isinstance(agent_result.content, str):
            final_agent_response_text = agent_result.content
        elif hasattr(agent_result, "output") and isinstance(agent_result.output, str):
            final_agent_response_text = agent_result.output
        elif isinstance(agent_result, str):
            final_agent_response_text = agent_result
        else:
            try:
                final_agent_response_text = str(agent_result)
                print("DEBUG: Converted agent_result to string.")
            except Exception as e:
                print(f"ERROR: Could not extract text from AgentResult. Error: {e}")
                print(
                    "Please inspect the 'agent_result' object to determine the correct attribute."
                )

        # Print agent response
        print("\n--- Agent's Full Response Text ---")
        print(final_agent_response_text)
        print("--- End of Agent's Full Response Text ---\n")

        # Try to extract diagram path from response
        diagram_path = None
        if final_agent_response_text:
            path_marker = "The diagram is saved at: "
            if path_marker in final_agent_response_text:
                start_index = final_agent_response_text.find(path_marker) + len(
                    path_marker
                )
                end_index = final_agent_response_text.find("\n", start_index)
                end_index = (
                    end_index if end_index != -1 else len(final_agent_response_text)
                )

                diagram_path_raw = final_agent_response_text[
                    start_index:end_index
                ].strip()
                diagram_path = diagram_path_raw.strip("`'\"")

                print(f"\nExtracted diagram path: '{diagram_path}'")

                if diagram_path and os.path.exists(diagram_path):
                    print(f"Displaying diagram from: {diagram_path}")
                    display(Image(filename=diagram_path))
                elif diagram_path:
                    print(f"Diagram file not found at: {diagram_path}")
                    print(f"Current working directory: {os.getcwd()}")
                    expected_dir = os.path.dirname(diagram_path)
                    if os.path.exists(expected_dir):
                        print(
                            f"Directory '{expected_dir}' exists with files: {os.listdir(expected_dir)}"
                        )
                    else:
                        print(f"Directory '{expected_dir}' does NOT exist.")
            else:
                print(
                    "Agent response did not include a diagram path in the expected format."
                )
        else:
            print("No textual response extracted from the agent's result.")


def galus_test_custom_tool(query):
    PROMPT = """
    You are a scientist that likes to formulate experiements.
    - To get example riddles, use the galus_custom_riddle_tool you have access to.
    - When a user asks you about science, respond with a riddle format based on the output of the riddle tool.
    - For simple questions, refuse to answer unless the user asks a scientific question.
    - If the question relates to science try your best to convert the answer into a riddle.
    - The response MUST be formatted the same way the riddle from the galus_custom_riddle_riddle tool format is.
    Make sure that you always answer with a riddle or tell the user that they are not scientific enough.
    """
    agent = Agent(system_prompt=PROMPT, tools=[galus_custom_riddle_tool])
    resp = agent(query)


# Galus Note: looks like someone wrote a bad builder.aws.com article.
#             Or maybe they are about to show tool hallucinations or guardrails.
def multi_agent_finance_orchestrator():
    MAIN_SYSTEM_PROMPT = """
    You are an assistant that routes queries to specialized agents:
    - For research questions and factual information, Use the research_assistant tool
    - For product recommendations and shopping advice, Use the product_recommendation_assistant tool
    - For travel planning and itineraries, Use the trip_planning_assistant tool
    - For simple questions not requiring specialized knowledge, Answer directly
    Always select the most appropriate tool based on the user's query.
    """
    orchestrator = Agent(
        system_prompt=MAIN_SYSTEM_PROMPT,
        tools=[
            investment_research_assistant,
            budget_optimizer_assistant,
            financial_planner_assistant,
        ],
    )

    resp = orchestrator(
        """
        I'm 30 years old, earning around $6,000 per month.
        I have some student loans and moderate savings.
        I want to understand how I can better manage my monthly budget,
        explore investment options, and build a solid long-term financial plan
        for buying a house and retiring early. Can you help?
        """
    )
    print(resp)


def dataframe_manipulation():
    prompt = """
    Write a Python script using the pandas library that performs the following tasks:
    - Create a sample DataFrame with the columns: 'Name', 'Age', and 'Salary'.
    - Add a new column named 'Bonus' that is 10% of the corresponding 'Salary' value.
    - Filter the DataFrame to include only rows where the 'Age' is greater than 30.
    - Group the data by age brackets (e.g. 20s, 30s, 40s) and calculate the average Salary and Bonus for each group.
    Execute the python script and show the output.
    Requirements:
    - Include clear inline comments to explain the logic.
    - Add a docstring for the function.
    - List any external libraries that need to be installed with 'uv add' if any.
    - Include brief documentations describing how the code works and how to run it.
    """
    model = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
    agent = Agent(model=model)
    resp = agent(prompt)
    print(resp)


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

    model = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
    agent = Agent(
        tools=[use_aws, http_request], system_prompt=system_prompt, model=model
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
    model = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"
    agent = Agent(
        tools=[python_repl, file_write], system_prompt=system_prompt, model=model
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
