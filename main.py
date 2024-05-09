import os
import openai
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import instruction_str, new_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")


data_path = os.path.join("data")
movies_df = pd.read_csv(os.path.join(data_path, "IMDBmovies.csv"))

movie_query_engine = PandasQueryEngine(
    df=movies_df, verbose=True, instruction_str=instruction_str
)

movie_query_engine.update_prompts({"pandas_prompt": new_prompt})

movie_query_engine.query("What are the top 10 movies?")
