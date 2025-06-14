from pydantic import BaseModel, Field
from hello_agent import run
from agents import Agent, Runner, set_tracing_disabled
set_tracing_disabled(True)

class WeatherAnswer(BaseModel):
    location: str
    temperature_c: float
    summart: str

agent1 = Agent(
    name="WeatherAgent",
    instructions="You are a helpful weather assistant. Provide the current weather information for the specified location.",
    output_type=WeatherAnswer,)

result = Runner.run_sync(
    agent1,
    input="What is the current weather in New York?",
    context=None,
    run_config=run
)
print(result.final_output)
print(f"Location: {result.final_output.location}")
print(f"Temperature: {result.final_output.temperature_c}°C")