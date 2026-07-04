from dataclasses import dataclass


@dataclass
class Config:
    gitlab_url: str
    gitlab_token: str
    gitlab_project_ids: list[str]
