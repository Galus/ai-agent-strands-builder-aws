from ai_agent_strands_builder_aws.core.agent import weather

def main():
    print("Hello from ai-agent-strands-builder-aws!")

    citydatetime="New York at 2026/01/01 12:00PM"
    print(f"Getting weather for {citydatetime}.")
    weather(citydatetime)

    print("Done running.")


if __name__ == "__main__":
    main()
