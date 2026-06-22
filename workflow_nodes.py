from utils.llm import llm           # imports the AI model objects

def travel_planner(state):          # creates a lamg graph node called travel planner

    prompt = f"""
You are a travel planner.

Create a detailed {state['days']}-day itinerary for {state['city']}.

Number of people: {state['people']}
Budget: ₹{state['budget']}

Include:

- Day-wise itinerary
- Places to visit
- Famous attractions
- Suggested timings
- Local food recommendations
"""

    response = llm.invoke(prompt)

    return {
        "travel_plan": response.content     
    }