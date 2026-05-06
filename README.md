# Interview Q&A Coach Agent - LangChain Single Agent Project

A beginner-friendly project that teaches you how to build a **single agent** using **LangChain + OpenAI**. The agent acts as a career coach, preparing candidates to ace job interviews by generating realistic interview questions and providing model answers using the STAR format.

## What You'll Learn

- How LangChain works (LLMs, prompts, tools, agents)
- How to create tools using the `@tool` decorator
- How an agent decides which tools to call and in what order
- How `PromptTemplate` shapes LLM output
- How the agent's tool-calling loop works (think -> act -> observe -> repeat)

## How It Works

```
User provides job role (e.g., "Data Analyst at fintech startup")
       |
       v
  [Agent thinks: "I need to generate interview questions first"]
       |
       v
  [Tool: generate_interview_questions] --> generates 8-10 realistic questions
                                            (technical, behavioral, role-specific)
       |
       v
  [Agent thinks: "Now I should provide model answers for these questions"]
       |
       v
  [Tool: generate_model_answers] --> writes impressive answers using STAR format
                                      (Situation, Task, Action, Result)
       |
       v
  Complete Q&A preparation package returned to candidate
```

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/interview_qa_coach_agent.git
cd interview_qa_coach_agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your real key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run

```bash
python interview_qa_coach.py
```

You'll see an interactive prompt:

```
============================================================
  INTERVIEW Q&A COACH AGENT
  Powered by LangChain + OpenAI
============================================================

Describe the job role you're interviewing for, and the agent will
generate interview questions and model answers to help you prepare.

Type 'quit' to exit.

Your job role:
```

Enter a job role (e.g., `Data Analyst at a fintech startup`) and the agent will generate interview questions and model answers. You'll also see detailed logs showing the agent's reasoning and tool calls.

## Example

**Input:**
```
Data Analyst at a fintech startup
```

**Output:**
```
============================================================
INTERVIEW QUESTIONS & MODEL ANSWERS
Job Role: Data Analyst at a fintech startup
============================================================

TECHNICAL QUESTIONS:

Q1: How would you approach analyzing a large dataset to identify payment fraud patterns?
A1: [STAR Format Answer]
Situation: At my previous company, we had growing fraud issues impacting customer trust.
Task: I needed to develop a data-driven approach to identify suspicious transaction patterns early.
Action: I used SQL to extract transaction data, then applied clustering algorithms in Python 
to identify outliers. I created a dashboard in Tableau to monitor key metrics in real-time.
Result: The fraud detection model improved by 35%, saving the company $500K annually.

Q2: Tell me about your experience with SQL and databases.
A2: I have 3+ years of SQL experience, writing complex queries with joins, aggregations, 
and window functions. I'm proficient with both PostgreSQL and MySQL, and I've optimized 
slow queries that improved performance by 40%. I also understand database normalization 
and indexing strategies.

BEHAVIORAL QUESTIONS:

Q3: Describe a time when you had to work with stakeholders who didn't understand data.
A3: [STAR Format Answer]
Situation: A marketing director was skeptical about data-driven campaign decisions.
Task: I had to communicate complex statistical findings in an understandable way.
Action: I created simple visualizations and presented findings using business metrics 
rather than technical jargon. I also scheduled regular sync meetings to build trust.
Result: The stakeholder became our biggest data champion, and we increased campaign 
ROI by 25% using data-driven insights.

Q4: How do you handle tight deadlines and competing priorities?
A4: I prioritize based on business impact and set realistic timelines. When facing 
tight deadlines, I break projects into smaller milestones and communicate progress 
clearly. I'm not afraid to ask for help or escalate blockers early.

ROLE-SPECIFIC QUESTIONS:

Q5: Why are you interested in working in fintech?
A5: I'm drawn to fintech because of the high-stakes environment where data decisions 
directly impact customer financial health. I'm excited about solving complex problems 
in payments, fraud detection, and risk management. Your company's mission aligns with 
my interest in building secure, scalable financial solutions.

============================================================
Good luck with your interview!
============================================================
```

## Project Structure

```
.
├── interview_qa_coach.py      # Main agent code (fully commented)
├── requirements.txt           # Python dependencies
├── .env.example               # API key template
├── .gitignore                 # Keeps secrets and venv out of git
├── architecture_diagram.drawio # Visual diagram of the agent flow
└── README.md                  # This file
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - Framework for building LLM applications
- [OpenAI GPT-4o-mini](https://platform.openai.com/) - The LLM powering the agent
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

