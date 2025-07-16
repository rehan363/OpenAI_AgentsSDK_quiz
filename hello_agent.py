from dotenv import load_dotenv
import os
from agents import Agent, Runner, set_tracing_disabled, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel

set_tracing_disabled(True)

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)
run = RunConfig(
    model=external_model,
    model_provider=external_client,
)


def greeting (name:str) ->str:
    """greet the user by name"""
    return f"asalam o Alaikum! {name}!"

    

# agent1 = Agent(
#     name="assistant",
#     instructions="You are a helpful assistant. Use the provided tools to answer questions.",
#     model=external_model,
# )

# result = Runner.run_sync(
#     agent1,
#     input="hi",
#     run_config=run,
#     context=None,)

# print(result.final_output)