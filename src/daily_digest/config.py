import os
from dotenv import load_dotenv

from daily_digest.models import Config


def get_config() -> Config:
    load_dotenv()
    return Config(
        gitlab_url=_require_env('GITLAB_URL'),
        gitlab_token=_require_env('GITLAB_TOKEN'),
        gitlab_project_ids=_require_env('GITLAB_PROJECT_IDS').split(','),
    )


def _require_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f'{key} is required')
    return value
