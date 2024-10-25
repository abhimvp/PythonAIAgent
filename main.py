import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.llms.gemini import Gemini
from prompts import new_prompt, instruction_str

# from llama_index.core import Settings


load_dotenv()
population_path = os.path.join("data","population.csv")
population_df = pd.read_csv(population_path)
# print(population_df.head(5)) tetsing purposes

llm = Gemini(model="models/gemini-1.0-pro")

population_query_engine = PandasQueryEngine(df=population_df, verbose=True,instruction_str=instruction_str,llm=llm) 
population_query_engine.update_prompts({
    "pandas_prompt": new_prompt
})
# gives all of the thoughts & detailed output when we use this query engine
# all this is doing is wrapping on top of dataframe we have provided & giving us an interface to 
# ask questions about this data using this kind of retrieval augmented generation system

population_query_engine.query("What is the population of India?")