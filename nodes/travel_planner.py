from utils.llm import llm               #imports the llm object from llm.py

def travel_planner(state):              # lang graph automatically passes the current state to it

    prompt = f"""
Create a {state['days']}-day travel itinerary for {state['city']}.

Number of people: {state['people']}
Budget: ₹{state['budget']}

Include:
- Day-wise itinerary
- Places to visit
- Local food recommendations
"""

    response = llm.invoke(prompt)

    return {
        "travel_plan": response.content             # return only the state they want to update
    }