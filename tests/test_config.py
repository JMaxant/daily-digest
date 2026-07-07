import pytest
from daily_digest.config import get_config
from unittest.mock import patch


@patch('daily_digest.config.load_dotenv')
def test_get_config_returns_values(_, monkeypatch, dot_env_fixture):
    for key, value in dot_env_fixture.items():
        print(value)
        monkeypatch.setenv(key, value)
    config = get_config()

    assert config.gitlab_url == 'https://gitlab.example.com'
    assert config.gitlab_token == 'fake-token'
    assert config.gitlab_project_ids == ['12345']


@patch('daily_digest.config.load_dotenv')
def test_get_config_when_url_missing(_, monkeypatch, dot_env_fixture):
    for key, value in dot_env_fixture.items():
        monkeypatch.setenv(key, value)
    # On s'assure que la variable n'est pas définie&
    monkeypatch.delenv('GITLAB_URL', raising=False)

    with pytest.raises(RuntimeError, match='GITLAB_URL is required'):
        get_config()


@patch('daily_digest.config.load_dotenv')
def test_config_raises_when_token_missing(_, monkeypatch, dot_env_fixture):
    for key, value in dot_env_fixture.items():
        monkeypatch.setenv(key, value)
    # On s'assure que la variable n'est pas définie
    monkeypatch.delenv('GITLAB_TOKEN', raising=False)

    with pytest.raises(RuntimeError, match='GITLAB_TOKEN is required'):
        get_config()


@patch('daily_digest.config.load_dotenv')
def test_config_when_project_ids_missing(_, monkeypatch, dot_env_fixture):
    for key, value in dot_env_fixture.items():
        monkeypatch.setenv(key, value)
    monkeypatch.delenv('GITLAB_PROJECT_IDS', raising=False)

    with pytest.raises(RuntimeError, match='GITLAB_PROJECT_IDS is required'):
        get_config()
