from market_research.crew import MarketResearchCrew


def run():

    inputs = {
        "topic": "AI in Healthcare"
    }

    result = MarketResearchCrew().crew().kickoff(
        inputs=inputs
    )

    return result


if __name__ == "__main__":
    run()