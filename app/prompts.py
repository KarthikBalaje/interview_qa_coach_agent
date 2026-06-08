"""Prompt templates used by the Interview Q&A Coach."""

from __future__ import annotations

QUESTION_PROMPT = """You are an interview preparation expert.
Given the following job role, generate 8 to 10 realistic interview questions.

The questions must cover:
- Technical skills
- Behavioural situations
- Role-specific scenarios

Job Role: {job_role}

Return only a numbered list of interview questions. Include the question type in brackets."""

ANSWER_PROMPT = """You are an interview preparation expert.
Given the job role and interview questions below, write concise, impressive model answers.

Use the STAR format (Situation, Task, Action, Result) where it naturally applies.

Job Role: {job_role}

Interview Questions:
{questions}

Formatting rules:
- Keep each question paired with its answer.
- Separate each pair with a line of 60 equals signs.
- Preserve the question type in brackets.
- Do not add unrelated advice or extra commentary."""


def build_question_prompt(job_role: str) -> str:
    """Return the final prompt used to generate interview questions."""

    return QUESTION_PROMPT.format(job_role=job_role.strip())


def build_answer_prompt(job_role: str, questions: str) -> str:
    """Return the final prompt used to generate model answers."""

    return ANSWER_PROMPT.format(job_role=job_role.strip(), questions=questions.strip())

