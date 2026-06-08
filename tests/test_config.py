"""Tests for environment configuration."""

from __future__ import annotations

import pytest

from app.config import ConfigurationError, load_settings


def test_load_settings_reads_valid_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-value")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-test")
    monkeypatch.setenv("OPENAI_TEMPERATURE", "0.2")

    settings = load_settings()

    assert settings.openai_api_key == "sk-test-value"
    assert settings.model_name == "gpt-test"
    assert settings.temperature == 0.2


def test_load_settings_rejects_placeholder_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-your-api-key-here")

    with pytest.raises(ConfigurationError):
        load_settings()


def test_load_settings_rejects_invalid_temperature(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-value")
    monkeypatch.setenv("OPENAI_TEMPERATURE", "very-hot")

    with pytest.raises(ConfigurationError):
        load_settings()
