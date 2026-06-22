def report_generator(state):            # receives the corrent state

    report = f"""
=================================
TRAVEL REPORT
=================================

Destination: {state['city']}
Days: {state['days']}
People: {state['people']}
Budget: ₹{state['budget']}

=================================
ITINERARY
=================================

{state['travel_plan']}

=================================
BUDGET ANALYSIS
=================================

{state['budget_analysis']}
"""

    return {
        "final_report": report                  # returns the field it want to update
    }