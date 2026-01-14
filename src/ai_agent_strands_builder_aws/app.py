from ai_agent_strands_builder_aws.core.agent import price_analysis

def main():
    print("Hello from ai-agent-strands-builder-aws!")

    symbol="Amazon"
    print(f"Trying to analyze historic stock data for {symbol}!")
    price_analysis(symbol)

    print("Done running.")


if __name__ == "__main__":
    main()
