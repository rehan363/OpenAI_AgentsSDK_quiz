from hello_agent import run
from agents import Agent, Runner, function_tool, set_tracing_disabled, handoff, RunContextWrapper
set_tracing_disabled(True)
from pydantic import BaseModel


@function_tool
async def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    print("addition tool called")
    return a + b

@function_tool
async def multiply_sum(a: int, b: int) -> int:
    """Multiplies the sum of two numbers by 2."""
    print("multiply_sum tool called")
    return (a + b) * 2



maths_agent = Agent(
    name="maths_agent",
    instructions="You are a maths assistant.take two numbers a, b from user and return results by using tools.",
    tools=[add_numbers, multiply_sum],
    reset_tool_choice=True,

)
async def main():
    result = await Runner.run(
        maths_agent,
        input="a = 5, b = 1",
        run_config=run,
        max_turns=1,
    )

    print(result.final_output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())