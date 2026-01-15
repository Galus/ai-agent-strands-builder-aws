from ai_agent_strands_builder_aws.core.agent import multi_agent_finance_orchestrator


def main():
    print("Hello from ai-agent-strands-builder-aws!")

    print(f"Running the multi agent finance orchestrator. Expecting it to fail.")
    multi_agent_finance_orchestrator()

    print("Done running.")


if __name__ == "__main__":
    main()
