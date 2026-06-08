"""Command-line entry point for the Interview Q&A Coach Agent."""

from __future__ import annotations

import logging
import sys

from app.config import ConfigurationError, load_settings
from app.langchain_agent import create_interview_agent, run_agent


def configure_logging() -> None:
    """Configure readable application logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def run_interview_coach(job_role: str) -> str:
    """Create the configured agent and run it for a single job role."""

    settings = load_settings()
    agent = create_interview_agent(settings)
    return run_agent(agent, job_role)


def main() -> int:
    """Run the interactive command-line interface."""

    configure_logging()

    try:
        settings = load_settings()
        agent = create_interview_agent(settings)
    except ConfigurationError as exc:
        print(f"Configuration error: {exc}")
        return 1

    print("\n" + "=" * 60)
    print("  INTERVIEW Q&A COACH AGENT")
    print("  Powered by LangChain + OpenAI")
    print("=" * 60)
    print("\nDescribe the job role you are interviewing for.")
    print("Type 'quit' to exit.\n")

    while True:
        job_role = input("Your job role: ").strip()

        if job_role.lower() in {"quit", "exit", "q"}:
            print("\nGoodbye! All the very best for your interviews!")
            return 0

        if not job_role:
            print("Please enter a job role.\n")
            continue

        try:
            result = run_agent(agent, job_role)
            print("\n" + "=" * 60)
            print(result)
            print("=" * 60 + "\n")
        except ValueError as exc:
            print(f"\nInput error: {exc}\n")
        except Exception as exc:
            logging.exception("Interview coach failed")
            print(f"\nError: {exc}")
            print("Please check your API key, network connection, and model access.\n")


if __name__ == "__main__":
    raise SystemExit(main())
