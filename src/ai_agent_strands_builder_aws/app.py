from ai_agent_strands_builder_aws.core.agent import galus_test_custom_tool


def main():
    print("Hello from ai-agent-strands-builder-aws!")

    print(f"Testing if tools actually work.")
    galus_test_custom_tool("What is the boiling point of Sodium NA?")

    print("Done running.")


if __name__ == "__main__":
    main()
