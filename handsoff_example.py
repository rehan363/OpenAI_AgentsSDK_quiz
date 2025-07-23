from hello_agent import run
from agents import Agent, Runner, function_tool, set_tracing_disabled,handoff, RunContextWrapper
set_tracing_disabled(True)
from agents.extensions import handoff_filters
import asyncio
from pydantic import BaseModel

class CurrentUser(BaseModel):
    is_logged_in: bool

async def can_customers_refund(local_context: RunContextWrapper, agent: Agent)-> bool:
    print(f"local_context: {local_context}")
    if local_context.context and local_context.context.is_logged_in:
        return True
    return False

refund_agent = Agent(
    name="refund_agent",
    
)

triage_agent = Agent(
    name="triage_agent",
    instructions="You are a triage assistant. handoff to refund agent if needed.",
    handoffs=[handoff(agent=refund_agent,
                      
                      is_enabled=True,              
                      )]
)

async def main():
    current_user = CurrentUser(is_logged_in=False)
    result = await Runner.run(
        triage_agent,
        input="i want to refund my order my id is 0038",
        run_config=run,
        context=current_user,
    )
    print(result.final_output)
    print("last_agent:", result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())