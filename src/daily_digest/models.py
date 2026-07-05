from dataclasses import dataclass


@dataclass
class Config:
    gitlab_url: str
    gitlab_token: str
    gitlab_project_ids: list[str]


@dataclass
class RenderableMergeRequest:
    title: str
    created_at: str
    updated_at: str
    branch: str
    project_name: str
    author: str
