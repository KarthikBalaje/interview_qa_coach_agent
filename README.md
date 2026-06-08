# Interview Q&A Coach Agent

A LangChain-powered interview preparation agent that generates realistic interview questions and STAR-style model answers for a specific job role.

The project is structured so the core workflow can be tested without calling OpenAI, while the command-line app still runs as a LangChain tool-using agent.

## Features

- Validates user input before calling the model
- Generates 8 to 10 interview questions for a role
- Covers technical, behavioural, and role-specific questions
- Produces model answers using the STAR format where appropriate
- Uses environment variables for API keys and model settings
- Includes automated tests for configuration, validation, and workflow logic

## Project Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── coach.py              # Core testable Q&A workflow
│   ├── config.py             # Environment/config validation
│   ├── langchain_agent.py    # LangChain model, tools, and agent wiring
│   └── prompts.py            # Prompt templates
├── tests/
│   ├── test_coach.py
│   └── test_config.py
├── interview_qa_coach.py     # CLI entry point
├── requirements.txt
├── .env.example
├── architecture_diagram.drawio
├── architecture_diagram.html
└── langchain_tutorial.md
```

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```bash
cp .env.example .env
```

Then edit `.env`:

```text
OPENAI_API_KEY=sk-your-real-key-here
OPENAI_MODEL=gpt-4.1-mini
OPENAI_TEMPERATURE=0.7
```

## Run

```bash
python interview_qa_coach.py
```

Example input:

```text
Data Scientist at a Corporate Bank
```

The agent will generate likely interview questions and model answers.

## Test

```bash
python -m pytest
```

The tests use fake model responses, so they do not require an OpenAI API call.
Pytest is configured to show each test case name and status.

## Error Handling

The app handles:

- Missing or placeholder API keys
- Invalid model temperature values
- Empty or vague job-role input
- Empty LLM responses
- Model/API failures during generation

## Security Notes

- `.env` is ignored by Git and should contain real secrets only locally.
- `.env.example` contains placeholders only.
- The application does not print or log the API key.
