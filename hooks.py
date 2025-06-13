from agents import Runner, RunHooks, RunContextWrapper, Agent, AgentHooks 
from dataclasses import dataclass
from typing import TypeVar, Generic
from pydantic import BaseModel
#Run lifecycle hooks
# ================================================================

class MyTest(BaseModel):
    name: str
    age: int

#Run hook
class MyCustomRunHooks(RunHooks):
    def on_run_start(self, agent, ctx: RunContextWrapper[MyTest]):
        print(f"Run started for agent: {ctx.context.name}")
    
    def on_run_end(self, agent):
        print(f"Run ended for agent: {agent.name}")

# Agent hooks
class MyCustomAgentHooks(AgentHooks):
    def on_agent_start(self, agent: Agent):
        print(f"Agent started: {agent.name}")
    
    def on_agent_end(self, agent: Agent):
        print(f"Agent ended: {agent.name}")

agent1 = Agent(name="TestAgent", instructions="helpfull assistant",hooks=MyCustomRunHooks())

test_data = MyTest(name="John", age=30)

result = Runner.run_sync(agent1, input="hello", context=test_data, hooks = MyCustomRunHooks())
print(result)
# ================================================================
# T = TypeVar('T')

# class MyTest(BaseModel):
#     id: int
#     name: str

# @dataclass
# class Testing(Generic[T]):
#     mydata: T

# output = Testing[MyTest](mydata=MyTest(id=1, name="ali"))
# print(output.mydata.id)
# print(output.mydata.name)


#============================================
# @dataclass
# class Testing[T]():
#     id: T
#     name: T

# output = Testing[int](id="r", name="ali")
# print(output.id)
# print(output.name)


