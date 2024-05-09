import os
import openai
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from src.prompts import instruction_str, new_prompt, context
from src.note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent.legacy.react.base import ReActAgent
from llama_index.llms.openai import OpenAI

# API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


data_path = os.path.join("data")
movies_df = pd.read_csv(os.path.join(data_path, "IMDBmovies.csv"))

movie_query_engine = PandasQueryEngine(
    df=movies_df, verbose=True, instruction_str=instruction_str
)

movie_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=movie_query_engine,
        metadata=ToolMetadata(
            name="movies_df",
            description="This gives information about movie data",
        ),
    ),
]


llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(llm=llm, tools=tools, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    response = agent.query(prompt)
    print(response)
