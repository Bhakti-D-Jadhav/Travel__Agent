from utils.llm import llm           # imports llm object

def budget_analyzer(state):         # lang graph automatically passes current state onto this function

    prompt = f"""
Analyze the trip below.

City: {state['city']}
Budget: ₹{state['budget']}
Days: {state['days']}
People: {state['people']}

Travel Plan:
{state['travel_plan']}

Provide budget allocation for:            
- Hotel
- Food
- Transport
- Sightseeing

Keep total within budget.
"""

    response = llm.invoke(prompt)               # calling the llm

    return {
        "budget_analysis": response.content
    }