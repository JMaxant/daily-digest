import pytest
from daily_digest.config import get_config
from unittest.mock import patch

@patch('daily_digest.config.load_dotenv')
def test_get_config_returns_values(_, monkeypatch):
    monkeypatch.setenv('GITLAB_URL', 'https://gitlab.example.com')
    monkeypatch.setenv('GITLAB_TOKEN', 'fake-token')
    
    config = get_config()
    
    assert config['gitlab_url'] == 'https://gitlab.example.com'
    assert config['gitlab_token'] == 'fake-token'

@patch('daily_digest.config.load_dotenv')
def test_get_config_when_url_missing(_, monkeypatch):
    # On s'assure que la variable n'est pas définie
    monkeypatch.delenv('GITLAB_URL', raising=False)
    monkeypatch.setenv('GITLAB_TOKEN', 'fake-token')

    with pytest.raises(RuntimeError, match='Both Gitlab url and token are required'):
        get_config()

@patch('daily_digest.config.load_dotenv')
def test_config_raises_when_token_missing(_, monkeypatch):
    # On s'assure que la variable n'est pas définie
    monkeypatch.setenv('GITLAB_URL', 'https://gitlab.example.com')
    monkeypatch.delenv('GITLAB_TOKEN', raising=False)

    with pytest.raises(RuntimeError, match='Both Gitlab url and token are required'):
        get_config()