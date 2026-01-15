from ai_agent_strands_builder_aws.core.agent import mcp_agent


def main():
    print("Hello from ai-agent-strands-builder-aws!")

    print(f"Testing agent that uses MCPClient.")
    mcp_agent()

    print("Done running.")


if __name__ == "__main__":
    main()
