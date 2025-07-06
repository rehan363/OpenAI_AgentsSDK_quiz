from hello_agent import run
from agents import Agent, Runner, set_tracing_disabled, function_tool
set_tracing_disabled(True)

@function_tool(name_override="greet_tool", description_override="a greeting tool that greets user")
def greeting (name: str, age:int) -> str:
    """Greets the user by provided name and age."""
    print("greeting tool called.......")
    return f"Hello {name}, you are {age} years old!"



pa_agent = Agent(
    name="pa agent",
    instructions="You are a personal assistant. greet the user first by provided tools",
    tools=[greeting]
)

print(pa_agent.tools)

# result = Runner.run_sync(
#     pa_agent,
#     input="hi, I am Ali ",
#     run_config=run
#     )
# print(result.final_output)