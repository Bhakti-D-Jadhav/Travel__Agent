from typing import TypedDict

class TravelState(TypedDict):
    city: str
    budget: int
    days: int
    people: int

    travel_plan: str
    budget_analysis: str
    final_report: str