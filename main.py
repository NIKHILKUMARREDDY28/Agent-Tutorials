from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests

from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

import warnings

warnings.filterwarnings("ignore")

from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor

search_tool = DuckDuckGoSearchRun()

results = search_tool.run("What is the capital of France?")

print(results)