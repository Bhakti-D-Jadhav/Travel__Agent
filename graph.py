from langgraph.graph import StateGraph, END         #used to create the workflow of graph

from state import TravelState                       # import structure used by all nodes
from nodes.travel_planner import travel_planner
from nodes.budget_analyzer import budget_analyzer
from nodes.report_generator import report_generator

builder = StateGraph(TravelState)                   # creates an empty workflow

builder.add_node("travel_planner", travel_planner)
builder.add_node("budget_analyzer", budget_analyzer)
builder.add_node("report_generator", report_generator)

builder.set_entry_point("travel_planner")               # defines where execution begins

builder.add_edge("travel_planner", "budget_analyzer")
builder.add_edge("budget_analyzer", "report_generator")
builder.add_edge("report_generator", END)

graph = builder.compile()                       # converts the graph into an executable workflow