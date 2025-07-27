from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from settings import settings
from prompts import SUMMARISATION_PROMPT
from utils import search_arxiv

openai_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=settings.OPENAI_API_KEY
)


query_context_agent = AssistantAgent(
    name="query_context_agent",
    model_client=openai_client,
    system_message="You are an expert in understanding and extracting context from queries.",
    tools=[search_arxiv]
)


paper_summariser_agent = AssistantAgent(
    name="paper_summariser_agent",
    model_client=openai_client,
    system_message=SUMMARISATION_PROMPT,
)

agents = [query_context_agent, paper_summariser_agent]

research_helper_team = RoundRobinGroupChat(
    agents,
    max_turns=2
)


if __name__ == '__main__':
    import asyncio
    async def main():
        query = "machine learning in healthcare"
        print(f"Query: {query}")

        # Run the team with the query
        results = await research_helper_team.run(task=query)

        # Print the results
        print(results)

    asyncio.run(main())