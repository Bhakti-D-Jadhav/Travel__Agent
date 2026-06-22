
from graph import graph             # import langGraph workflow from graph
import json
import os

city = input("Enter city: ")
budget = int(input("Enter budget (INR): "))
days = int(input("Enter days: "))
people = int(input("Enter people: "))

result = graph.invoke(              # starts langGraph workflow
    {
        "city": city,
        "budget": budget,
        "days": days,
        "people": people
    }
)

print("\n")
print(result["final_report"])               # Displays final report


# Save report history
filename = "travel_report.json"

# Load existing reports
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        try:
            reports = json.load(f)
        except:
            reports = []
else:
    reports = []

# Add new report
reports.append(result)

# Save all reports
with open(filename, "w", encoding="utf-8") as f:
    json.dump(reports, f, indent=4)

print("\nReport saved successfully!")