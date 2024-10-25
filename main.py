import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import (
    QueryEngineTool,
    ToolMetadata,
)  # A tool making use of a query engine.
from llama_index.core.agent.react import (
    ReActAgent,
)  # Subclasses AgentRunner with a ReActAgentWorker
from llama_index.llms.gemini import Gemini
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine

# from llama_index.core import Settings


load_dotenv()
population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)
# print(population_df.head(5)) tetsing purposes

llm = Gemini(model="models/gemini-1.0-pro")

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str, llm=llm
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})
# gives all of the thoughts & detailed output when we use this query engine
# all this is doing is wrapping on top of dataframe we have provided & giving us an interface to
# ask questions about this data using this kind of retrieval augmented generation system

# population_query_engine.query("What is the population of India?")

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
]

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
# verbose = true to get detailed infromation on the thoughts of llm so we know what type of tool it's going to be using
# context can tell the agent before hand what it's supposed to be doing  - so it has some more information and more context about what it should do
# agent.query("What is the population of India?")
# new in python 3.9
while (prompt := input("Enter a prompt (or 'exit' to quit): ")) != "exit":
    result = agent.query(prompt)
    print(result)

# while True:
#     query = input("Enter your query (or 'exit' to quit): ")
#     if query.lower() == "exit":
#         break
#     response = agent.query(query)
#     print(response)
