from dotenv import load_dotenv
from agents import set_tracing_disabled, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner
import os

load_dotenv()

set_tracing_disabled(True)
open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")
if not open_router_api_key:
    raise ValueError("OPEN_ROUTER_API_KEY is not set in the environment variables.")

Base_URL= "https://openrouter.ai/api/v1"

external_client= AsyncOpenAI(
    api_key=open_router_api_key,
    base_url=Base_URL,
)

external_model= OpenAIChatCompletionsModel(
    model="opengvlab/internvl3-2b:free",
    openai_client=external_client,
)

assistant_agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=external_model,
)

result = Runner.run_sync(
    assistant_agent,
    input="what were you last updated?",
)
print(result.final_output)