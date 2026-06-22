# ✈️ AI Travel Agent

An AI-powered command-line travel assistant that generates personalized travel plans and budget analyses using a **graph-based workflow architecture**. The application takes user inputs such as destination, budget, trip duration, and number of travelers, then creates a structured travel report and saves it as JSON.

---

## ✨ Features

* 🌍 Generate personalized travel itineraries
* 📅 Create day-wise travel plans
* 💰 Analyze and allocate travel budgets
* 👥 Plan trips for individuals or groups
* 🗺️ Recommend attractions and activities
* 🍽️ Suggest local food experiences
* 📄 Generate structured travel reports
* 💾 Save reports in JSON format
* 🔄 Graph-based workflow execution using nodes

---

## 🛠️ Tech Stack

* Python
* Groq API / LLM
* python-dotenv
* JSON
* File Handling
* Visual Studio Code (VS Code)
* Git & GitHub

---

## 📁 Project Structure

```text
TRAVEL_AGENT/
│
├── main.py                 # Entry point of the application
├── graph.py                # Defines workflow graph
├── workflow_nodes.py       # Connects workflow nodes
├── state.py                # Maintains application state
├── requirements.txt
├── .env
├── .gitignore
├── travel_report.json      # Generated report
│
├── nodes/
│   ├── travel_planner.py      # Generates itinerary
│   ├── budget_analyzer.py     # Performs budget analysis
│   └── report_generator.py    # Creates final report
│
├── utils/
└── __pycache__/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/TRAVEL_AGENT.git
cd TRAVEL_AGENT
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📖 Example Usage

```text
Enter city: Pune
Enter budget (INR): 250000
Enter days: 15
Enter people: 6
```

The application generates:

* Destination Details
* Day-wise Itinerary
* Budget Analysis
* Accommodation Suggestions
* Food Recommendations
* Final Travel Report

---

## 🔄 Workflow

```text
User Input
      ↓
Travel Planner Node
      ↓
Budget Analyzer Node
      ↓
Report Generator Node
      ↓
travel_report.json
```

---

## 🎯 Learning Outcomes

Through this project, I explored:

* Graph-based workflow design
* Modular Python programming
* State management
* Prompt engineering with LLMs
* JSON report generation
* Building AI-powered CLI applications
* Project structuring and code organization

---

## 👩‍💻 Author

**Bhakti Jadhav**

Aspiring Python Developer | Data Analytics Enthusiast | AI & ML Learner

⭐ Feel free to explore the project and share your feedback!


