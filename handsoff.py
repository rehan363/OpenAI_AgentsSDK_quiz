from hello_agent import run
from agents import Agent, Runner, function_tool, set_tracing_disabled,handoff
set_tracing_disabled(True)
from agents.extensions import handoff_filters
import asyncio

@function_tool
def refund_request(order_id: str) -> str:
    """Request a refund for the given order ID."""
    print("Processing refund request for order ID:", order_id)
    return f"Refund requested for order ID: {order_id}"


refund_agent = Agent(
    name="refund_agent",
    instructions="You are a refund assistant. Confirm refund requests if order ID is provided.",
    tools=[refund_request],
)

triage_agent = Agent(
    name="triage_agent",
    instructions="You are a triage assistant. handoff to refund agent if needed.",
    handoffs=[handoff(agent=refund_agent,
                      tool_name_override="refund_request",
                      tool_description_override="Request a refund for the user",)]
                    #   input_filter=handoff_filters.remove_all_tools
)

async def main():
    result = await Runner.run(
        triage_agent,
        input="i want to refund my order my id is 0038",
        run_config=run
    )
    print(result.final_output)
    print("last_agent:", result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())