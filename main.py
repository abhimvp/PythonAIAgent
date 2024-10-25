import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine

load_dotenv()
population_path = os.path.join("data","population.csv")
population_df = pd.read_csv(population_path)
# print(population_df.head(5)) tetsing purposes

population_query_engine = PandasQueryEngine(df=population_df, verbose=True) 
# gives all of the thoughts & detailed output when we use this query engine
# all this is doing is wrapping on top of dataframe we have provided & giving us an interface to 
# ask questions about this data using this kind of retrieval augmented generation system
