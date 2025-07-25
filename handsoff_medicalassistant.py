from agents import Agent, Runner, function_tool, set_tracing_disabled, handoff, RunContextWrapper
from hello_agent import run
set_tracing_disabled(True)
from pydantic import BaseModel

class CurrentMedicalUser(BaseModel):
    country: str
    subscription_tier: str

primary_doctor_agent = Agent(
    name="PrimaryDoctorAgent",
    instructions="you are a primary care assistant. You will assist users with general medical queries and provide basic health advice.",
)

cardiology_specialist = Agent(
    name="CardiologySpecialist",
    instructions="you are a cardiology specialist assistant . You will assist users with cardiology-related queries and provide detailed health advice.",
)

brain_surgeon_specialist = Agent(
    name="BrainSurgeonSpecialist",
    instructions="you are a brain surgeon specialist assistant. You will assist users with brain surgery-related queries and provide detailed health advice.",
)

async def can_access_brain_surgeon_specialist(local_context: RunContextWrapper[CurrentMedicalUser], agent: Agent[CurrentMedicalUser])-> bool:
    print(f"local_context: {local_context}")
    user= local_context.context
    if user.country == "USA" and user.subscription_tier == "Enterprise":
        return True
    else:return False

async def can_access_cardiology_specialist(local_context:RunContextWrapper[CurrentMedicalUser], agent: Agent):
    print(f"local_context: {local_context}")
    user = local_context.context
    if user.country == "USA" or user.country == "canada" and user.subscription_tier == "Premium":
        return True
    else:
        print(f"Agent {agent.name} cannot process cardiology queries as user does not have Premium subscription.")
        return False

medical_assistant = Agent(
    name="medical_assistant",
    instructions="""
    You are a medical assistant. Follow these guidelines:
    - If the user mentions heart-related issues (e.g., "heart", "chest pain", "cardiac"), and the 'transfer_to_cardiac_surgeon' tool is available, use it to hand off to the cardiac surgeon.
    - If the user mentions brain-related issues (e.g., "brain", "headache", "neurological"), and the 'transfer_to_brain_specialist' tool is available, use it to hand off to the brain specialist.
    - For all other inquiries, provide general medical advice.
    - If the user requests a specialist but the corresponding tool is not available, inform them that they need to upgrade their subscription: Premium for cardiac surgeon, Enterprise for brain specialist.
    """,
    handoffs=[
        handoff(agent=cardiology_specialist, 
                 is_enabled=can_access_cardiology_specialist),
        handoff(agent=brain_surgeon_specialist, 
                 is_enabled=can_access_brain_surgeon_specialist),
    ]
)

# Example usage
async def main():
    run_config = {}  # Placeholder for actual run configuration
    
    # Basic user with heart-related inquiry
    basic_user = CurrentMedicalUser(subscription_tier="Enterprise", country="USA")
    
    result = await Runner.run(
        medical_assistant,
        input="I have a severe headache, what should I do?",
        run_config=run,
        context=basic_user,
    )
    print("Basic User (Chest Pain):", result.final_output)
    print("Last Agent:", result.last_agent.name)  


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())