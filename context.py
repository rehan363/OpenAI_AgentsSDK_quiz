from hello_agent import run
from agents import Agent, Runner, function_tool, set_tracing_disabled, RunContextWrapper
set_tracing_disabled(True)

# def get_system_prompt(ctx: RunContextWrapper, agent):
#     print(f"Context: {ctx.context}")
#     print(f"Agent: {agent}")
#     return f"you are a helpful assistant."

# agent1 = Agent(
#     name= "assistant",
#     instructions=get_system_prompt
# )

# result= Runner.run_sync(
#     agent1,
#     input="hi whats the user name and password?",
#     run_config=run,
#     context= "user name is ali and its password is 007"
# )

# print(result.final_output)

#==========================x=======================================================x==============

from dataclasses import dataclass
@dataclass
class User:
    name: str
    id: str

def get_user_info(self):
    return f"User Name: {self.name}, User ID: {self.id}"

def update_user_info(self, name: str, id: str):
    self.name = name
    self.id = id
    return f"User info updated to Name: {self.name}, ID: {self.id}"


ctx.context.update_user_info(f"User Name: {ctx.context.name}, User ID: {ctx.context.id}")

agent= Agent(
    name="user_agent",
    instructions="You are a user information agent. You can provide user details and update them.",
)

user1 =User(name="Ali", id="007")

result = Runner.run_sync(
    agent,
    input="hi do you have any context?",
    run_config=run,
    context=user1
)
print(result.final_output)
