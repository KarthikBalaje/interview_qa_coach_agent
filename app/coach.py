"""Core Interview Q&A Coach workflow.

This module is deliberately independent from CLI input and environment loading so
it can be tested without calling OpenAI.
"""

from __future__ import annotations

import logging
import re
from typing import Any, Protocol

from app.prompts import build_answer_prompt, build_question_prompt

logger = logging.getLogger(__name__)


class CoachError(RuntimeError):
    """Raised when the coach workflow cannot complete."""


class LLMClient(Protocol):
    """Minimal interface required from LangChain chat models."""

    def invoke(self, prompt: str) -> Any:
        """Generate a response for a prompt."""


INVALID_ROLE_PATTERNS = (
    re.compile(r"^(hi|hello|hey|thanks|thank you)$", re.IGNORECASE),
    re.compile(r"^(help|test|asdf|qwerty)$", re.IGNORECASE),
)


def validate_job_role(job_role: str) -> str:
    """Validate and normalize a user-provided job role."""

    normalized = " ".join(job_role.strip().split())

    if not normalized:
        raise ValueError("Please enter a job role.")

    if len(normalized) < 4:
        raise ValueError("Please provide a more specific job role.")

    if any(pattern.match(normalized) for pattern in INVALID_ROLE_PATTERNS):
        raise ValueError("Please provide a valid job role, such as 'Data Analyst at a bank'.")

    return normalized


def response_content(response: Any) -> str:
    """Extract text content from a LangChain/OpenAI response-like object."""

    content = getattr(response, "content", response)
    if content is None:
        raise CoachError("The language model returned an empty response.")

    text = str(content).strip()
    if not text:
        raise CoachError("The language model returned an empty response.")

    return text


class InterviewQACoach:
    """Generate interview questions and model answers for a job role."""

    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    def generate_interview_questions(self, job_role: str) -> str:
        """Generate likely interview questions for a validated job role."""

        role = validate_job_role(job_role)
        logger.info("Generating interview questions for role: %s", role)

        try:
            return response_content(self.llm.invoke(build_question_prompt(role)))
        except Exception as exc:
            if isinstance(exc, (CoachError, ValueError)):
                raise
            raise CoachError("Failed to generate interview questions.") from exc

    def generate_model_answers(self, questions: str, job_role: str) -> str:
        """Generate STAR-style answers for the supplied interview questions."""

        role = validate_job_role(job_role)
        clean_questions = questions.strip()
        if not clean_questions:
            raise ValueError("Questions are required before answers can be generated.")

        logger.info("Generating model answers for role: %s", role)

        try:
            return response_content(self.llm.invoke(build_answer_prompt(role, clean_questions)))
        except Exception as exc:
            if isinstance(exc, (CoachError, ValueError)):
                raise
            raise CoachError("Failed to generate model answers.") from exc

    def run(self, job_role: str) -> str:
        """Run the full Q&A preparation workflow."""

        role = validate_job_role(job_role)
        questions = self.generate_interview_questions(role)
        answers = self.generate_model_answers(questions, role)

        return (
            f"Interview preparation package for: {role}\n"
            f"{'=' * 60}\n"
            f"{answers}\n"
            f"{'=' * 60}"
        )

