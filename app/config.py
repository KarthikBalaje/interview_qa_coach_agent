"""Configuration loading for the Interview Q&A Coach."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


class ConfigurationError(RuntimeError):
    """Raised when required runtime configuration is missing or invalid."""


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the coach application."""

    openai_api_key: str
    model_name: str = "gpt-4.1-mini"
    temperature: float = 0.7


def load_settings() -> Settings:
    """Load settings from environment variables and a local .env file."""

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key or api_key.startswith("sk-your"):
        raise ConfigurationError(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and add your real key."
        )

    model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip() or "gpt-4.1-mini"
    raw_temperature = os.getenv("OPENAI_TEMPERATURE", "0.7").strip()

    try:
        temperature = float(raw_temperature)
    except ValueError as exc:
        raise ConfigurationError("OPENAI_TEMPERATURE must be a number.") from exc

    if not 0 <= temperature <= 2:
        raise ConfigurationError("OPENAI_TEMPERATURE must be between 0 and 2.")

    return Settings(
        openai_api_key=api_key,
        model_name=model_name,
        temperature=temperature,
    )

