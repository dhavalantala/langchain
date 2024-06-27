import os
from typing import TextIO
from dotenv import load_dotenv

import openai
import pandas as pd
import streamlit as st 
from langchain_experimental.agents.agent_toolkits import create_csv_agent, create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_answer_csv(file:TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """

    ## Load the CSV file as a pandas dataframe
    # df = pd.read_csv(file)
    # df = pd.read_csv("path-of-file")

    # Create an agent using OpenAI and the pandas DataFrame 
    agent = create_csv_agent(ChatOpenAI(temperature=0), file, verbose=False)
    #agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    # Run the agent on the given query and the return the answer
    # query = "whats the square root of the average age?"
    answer = agent.invoke(query)
    return answer