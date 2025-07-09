from hello_agent import run
from typing import Any
from pydantic import BaseModel, ConfigDict
from agents import Agent, Runner, set_tracing_disabled, function_tool, FunctionTool, RunContextWrapper
set_tracing_disabled(True)

# @function_tool(name_override="greet_tool", description_override="a greeting tool that greets user")
# def greeting (name: str, age:int) -> str:
#     """Greets the user by provided name and age."""
#     print("greeting tool called.......")
#     return f"Hello {name}, you are {age} years old!"

@function_tool

class Student(BaseModel):
    name: str
    roll_no: int
    model_config = ConfigDict(extra="forbid")

async def greet_student(ctx: RunContextWrapper[Any], args: str ) -> str:
    print("greet_student tool called.......")
    parsed = Student.model_validate_json(args)
    return f"Hello {parsed.name}, your roll number is {parsed.roll_no}."


custom_tool= FunctionTool(
    name="process_srudent",
    description="A tool to process student information",
    params_json_schema=Student.model_json_schema(),
    on_invoke_tool=greet_student
)

pa_agent = Agent(
    name="pa agent",
    instructions="You are a student personal assistant. that helps students",
    tools=[custom_tool]
)

# print(pa_agent.tools).......

result = Runner.run_sync(
    pa_agent,
    input="proocess student info with name john and roll_no 123",
    run_config=run
    )
print(result.final_output)