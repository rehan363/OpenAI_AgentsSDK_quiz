from hello_agent import run
from agents import Agent, Runner, set_tracing_disabled, function_tool, ModelSettings
from agents.agent import StopAtTools
from pydantic import BaseModel

class GreetingInput(BaseModel):
    name: str
    age: int

@function_tool
def greet(params: GreetingInput) ->str:
    """Greets the user by provided name and age."""
    print("greet function called with params:", params)
    return f"Hello {params.name}, you are {params.age} years old!"

# @function_tool
# def greet(name: str) -> str:
#     """Greats the user by provided name."""
#     print("greet function called with name:", name)
#     return name

@function_tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    print("addition tool called")
    return a + b

set_tracing_disabled(True)

tool_agent = Agent(
    name="personal_assistant",
    instructions="You are a personal assistant. always use provided tools",
    tools=[greet, add_numbers],
    # model_settings=ModelSettings(tool_choice="none")
    model_settings=ModelSettings(tool_choice="required"),
    reset_tool_choice=True,
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["add_numbers"]),
    
)

# print(tool_agent.tools)

result = Runner.run_sync(
    tool_agent,
    input=" hi i am ali and 40 years old",
    run_config=run,
    context=None,
    # max_turns=1,
)

print(result.final_output)