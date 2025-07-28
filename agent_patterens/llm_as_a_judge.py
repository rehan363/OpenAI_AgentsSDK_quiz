from hello_agent import run
from agents import Agent, Runner, set_tracing_disabled, handoff, RunContextWrapper
from pydantic import BaseModel
from typing import Literal
from dataclasses import dataclass

class GymUser(BaseModel):
    fitness_goal: str
    dietary_preferences: str

@dataclass
class PlanFeedback:
    feedback: str
    score: Literal["pass", "needs_improvement", "fail"]

gym_agent = Agent(
    name="GymAgent",
    instructions="You are a gym assistant. You will provide workout plans and fitness advice based on user's fitness goals.",
)

work_out_plan_generator = Agent(
    name="WorkoutPlanGenerator",
    instructions="Generate a personalized workout plan based on user's fitness goals and preferences.",
)

diet_plan_generator = Agent(
    name="DietPlanGenerator",
    instruction="Generate a personalized diet plan based on user's preferences and health goals.",
)


