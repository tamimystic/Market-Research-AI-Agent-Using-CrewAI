````md
# Market Research AI Agent Using CrewAI

A multi-agent AI-powered market research system built using CrewAI, Streamlit, and Groq LLM. The project is designed to automate market intelligence gathering, business analysis, and executive-level report generation through collaborative AI agents.

The application allows users to enter any market research topic and automatically generates structured business intelligence, including industry insights, growth analysis, competitor information, SWOT analysis, customer sentiment, regional intelligence, and strategic recommendations.

The objective of this project is to simplify the market research process by combining multiple specialized AI agents into a single workflow and presenting results through an interactive analytics dashboard.

## Source Code Repository

```text
https://github.com/tamimystic/Market-Research-AI-Agent-Using-CrewAI
````

---

## Live Application

Application URL:

```text
https://tamimystic-market-research-ai-agent-using-crewai.streamlit.app/
```

---

## Project Objective

Traditional market research often involves collecting information from multiple sources, analyzing industry trends, evaluating competitors, and manually preparing reports. This process can be time-consuming and difficult, especially when working with large amounts of market information.

This project addresses that challenge by automating the research pipeline using multiple AI agents.

The system performs:

* Topic-based market research
* Market intelligence gathering
* Growth and trend analysis
* SWOT analysis
* Competitor landscape evaluation
* Customer sentiment analysis
* Executive report generation
* Strategic business recommendation generation
* Interactive analytics visualization

The generated report is written in a professional business style and can be used for portfolio projects, business presentations, research discussions, strategic planning, and professional platforms such as LinkedIn.

---

## Key Features

### Topic-Based Research

The application accepts any market research topic from the user.

Example topics include:

* AI in Agriculture
* AI in Healthcare
* Electric Vehicle Market
* Cybersecurity Industry
* FinTech Ecosystem
* EdTech Industry
* Renewable Energy Market

Based on the selected topic, the system dynamically generates market intelligence and analytics.

---

### Multi-Agent Workflow

Instead of relying on a single LLM response, the system uses multiple specialized AI agents working sequentially.

#### Research Agent

Responsible for gathering market intelligence and identifying important information related to:

* Market size
* Growth trends
* CAGR
* Investment activities
* Customer behavior
* Regional market development
* Industry adoption patterns

#### Analysis Agent

Responsible for transforming collected information into actionable business insights through:

* SWOT analysis
* Risk evaluation
* Strategic opportunity identification
* Competitor analysis
* Market forecasting
* Customer intelligence

#### Report Writer Agent

Responsible for converting research findings into a professional executive report.

The generated report:

* Follows a professional business writing style
* Maintains a humanized tone
* Avoids robotic language
* Produces structured executive-level reporting
* Can be used for LinkedIn posts or business presentations

---

## Dashboard Features

The project includes a Streamlit-based interactive dashboard for visualizing market intelligence.

### Market Analytics Overview

Key indicators include:

* Market Size
* CAGR
* AI Adoption
* Investment Trend
* Risk Level

### Interactive Data Visualization

The system dynamically generates charts based on AI-generated analytics.

Visualizations include:

* Market growth trends
* Regional market comparison
* Competitor market distribution
* Customer sentiment analysis
* SWOT breakdown
* Market forecast analytics

### Executive Intelligence Section

The dashboard also provides:

* Executive insights
* Strategic recommendations
* Business opportunities
* Risk considerations
* Future outlook

### Downloadable Report

Users can download the generated executive market research report for documentation, presentations, or professional sharing.

---

## Technology Stack

| Purpose                   | Technology              |
| ------------------------- | ----------------------- |
| Frontend Interface        | Streamlit               |
| Multi-Agent Orchestration | CrewAI                  |
| Large Language Model      | Groq                    |
| Model                     | Llama 3.3 70B Versatile |
| Data Processing           | Pandas                  |
| Visualization             | Plotly                  |
| Environment Variables     | Python Dotenv           |
| Package Management        | uv                      |

---

## Project Architecture

The workflow of the system follows a sequential multi-agent pipeline.

```text
User Input
     ↓
Research Agent
     ↓
Analysis Agent
     ↓
Report Writer Agent
     ↓
Structured Analytics Output
     ↓
Interactive Dashboard
     ↓
Executive Market Report
```

Each agent is responsible for a specific task, which improves modularity and produces more structured results compared to a single-prompt approach.

---

## Project Structure

```text
Market-Research-AI-Agent-Using-CrewAI
│
├── knowledge/
│   └── user_preference.txt
│
├── src/
│   └── market_research/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   └── custom_tool.py
│       │
│       ├── app.py
│       ├── crew.py
│       └── main.py
│
├── tests/
├── .env
├── requirements.txt
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tamimystic/Market-Research-AI-Agent-Using-CrewAI.git
```

Move to the project directory:

```bash
cd Market-Research-AI-Agent-Using-CrewAI
```

### Using uv (Recommended)

This project was developed using `uv` for dependency and environment management.

Install `uv`:

```bash
pip install uv
```

Create virtual environment:

```bash
uv venv
```

Activate environment:

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Git Bash

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
uv sync
```

### Alternative Setup Using pip

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Git Bash

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
MODEL=groq/llama-3.3-70b-versatile
```

---

## Running the Application

Run locally using:

```bash
streamlit run src/market_research/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

---

## If you want to Create Project on your System

* Follow This Documentation `https://docs.crewai.com/en/installation`


### Virtual Environment Setup

```bash
crewai create crew your_project_name
````

Move into the project directory:

```bash
cd your_project_name
```

Deactivate Conda base environment (if active):

```bash
conda deactivate
```

Activate the project virtual environment.

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Git Bash

```bash
source .venv/Scripts/activate
```

Verify Python path:

### PowerShell

```powershell
where python
```

### Git Bash

```bash
which python
```

The output should point to:

```text
project_folder/.venv/Scripts/python.exe
```

---

## Deployment

### Streamlit Community Cloud

Main file path:

```text
src/market_research/app.py
```

Secrets configuration:

```toml
OPENAI_API_KEY="your_api_key"
GROQ_API_KEY="your_api_key"
MODEL="groq/llama-3.3-70b-versatile"
```

### Render Deployment

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
PYTHONPATH=src streamlit run src/market_research/app.py --server.port $PORT --server.address 0.0.0.0
```

---

## Example Workflow

Input:

```text
AI in Agriculture
```

Generated output includes:

* Market research findings
* Growth analysis
* SWOT analysis
* Competitor insights
* Customer behavior analysis
* Regional intelligence
* Strategic recommendations
* Executive-level report generation

---

## Possible Use Cases

This project can be useful for:

* Market research
* Business intelligence
* Startup analysis
* Industry trend analysis
* Strategic planning
* Competitor research
* Academic projects
* Portfolio demonstrations

---

## Future Improvements

Potential future improvements include:

* PDF export support
* Live web search integration
* Real-time market APIs
* Historical trend tracking
* Multi-language report generation
* RAG-based research enhancement

---

## Author

**Tamim Hossain**
B.Sc. in Computer Science and Engineering

Areas of Interest:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Natural Language Proecessing
* Generative AI
* Single/Multi-Agent Systems

```
```
