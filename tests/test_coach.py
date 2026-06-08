"""Tests for the core Interview Q&A Coach workflow."""

from __future__ import annotations

import pytest

from app.coach import CoachError, InterviewQACoach, response_content, validate_job_role


class FakeResponse:
    def __init__(self, content: str) -> None:
        self.content = content


class FakeLLM:
    def __init__(self, responses: list[str]) -> None:
        self.responses = responses
        self.prompts: list[str] = []

    def invoke(self, prompt: str) -> FakeResponse:
        self.prompts.append(prompt)
        return FakeResponse(self.responses.pop(0))


def test_validate_job_role_normalizes_whitespace() -> None:
    assert validate_job_role("  Data   Analyst at a Bank  ") == "Data Analyst at a Bank"


@pytest.mark.parametrize("job_role", ["", "hi", "q", "test"])
def test_validate_job_role_rejects_invalid_input(job_role: str) -> None:
    with pytest.raises(ValueError):
        validate_job_role(job_role)


def test_response_content_rejects_empty_model_response() -> None:
    with pytest.raises(CoachError):
        response_content(FakeResponse("   "))


def test_interview_coach_runs_question_then_answer_workflow() -> None:
    llm = FakeLLM(
        [
            "1. [Technical Skills] How do you validate a model?",
            "Question 1. [Technical Skills] How do you validate a model?\nAnswer: Use STAR.",
        ]
    )
    coach = InterviewQACoach(llm)

    result = coach.run("Data Scientist at a Corporate Bank")

    assert "Interview preparation package for: Data Scientist at a Corporate Bank" in result
    assert "Answer: Use STAR." in result
    assert len(llm.prompts) == 2
    assert "generate 8 to 10 realistic interview questions" in llm.prompts[0]
    assert "Interview Questions:" in llm.prompts[1]

