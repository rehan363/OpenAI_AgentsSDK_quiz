from hello_agent import run
from agents import Agent, Runner, function_tool, set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent

# enable_verbose_stdout_logging()  # Commented out to disable verbose logging
import asyncio
set_tracing_disabled(True)

@function_tool
def user_status(id: str) -> str:
    """gets the user id form input and returns the user status if its a basic or premium user"""
    if id == "007":
        return "you are a premium user and you can access all features."
    else:
        return "you are a basic user and you can access only basic features."


travel_agent = Agent(
    name="travel_agent",
    instructions="you are a helpful travel assistant that gives the travel plan and also tells the current user status",
    tools=[user_status],
)
async def stream():
    result = Runner.run_streamed(
        travel_agent,
        input="heloo who are you?",
        run_config=run)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
           
            print(event.data,end="", flush=True)
    
asyncio.run(stream())

# from agents import agent.clone