from hello_agent import run
from agents import Agent, Runner, set_tracing_disabled, function_tool, ModelSettings
from agents.agent import StopAtTools
from pydantic import BaseModel

# class GreetingInput(BaseModel):
#     name: str
#     age: int

# @function_tool
# def greet(params: GreetingInput) ->str:
#     """Greets the user by provided name and age."""
#     print("greet function called with params:", params)
#     return f"Hello {params.name}, you are {params.age} years old!"

# # @function_tool
# # def greet(name: str) -> str:
# #     """Greats the user by provided name."""
# #     print("greet function called with name:", name)
# #     return name

# @function_tool(strict_mode=True)
# def add_numbers(a: int, b: int) -> int:
#     """Adds two numbers."""
#     print("addition tool called")
#     return a + b

# set_tracing_disabled(True)

# tool_agent = Agent(
#     name="personal_assistant",
#     instructions="You are a personal assistant. always use provided tools",
#     tools=[greet, add_numbers],
#     # model_settings=ModelSettings(tool_choice="none")
#     model_settings=ModelSettings(tool_choice="required"),
#     reset_tool_choice=True,
#     # tool_use_behavior=StopAtTools(stop_at_tool_names=["add_numbers"]),
    
# )

# # print(tool_agent.tools)

# result = Runner.run_sync(
#     tool_agent,
#     input=" hi i am ali and 40 years old",
#     run_config=run,
#     context=None,
#     # max_turns=1,
# )

# print(result.final_output)

# ===============x===========================x========================x==========

def error_function(name: str, error=None) -> str:
    return f"Error while processing the request for {name}. Please try again later."


@function_tool(failure_error_function=error_function)
def greeting_user(name: str) -> str:
     if name =="ali":
          raise ValueError("Name 'ali' is not allowed.")
     else:
          return f"Hello {name}, welcome to our service!"
     """analyse the user name from input if name not provide route to error function"""

 


pa_agent = Agent(
    name="Personal Assistant",
    instructions="You are a personal assistant. Use the provided tools to answer questions.",
    tools=[greeting_user],
    # model_settings=ModelSettings(parallel_tool_calls=False),
    model_settings=ModelSettings(tool_choice="auto",)
    # tool_use_behavior="stop_on_first_tool")
)

result = Runner.run_sync(
    pa_agent,
    input= "hi ali here ",
    run_config=run,
    
)

print(result.final_output)

