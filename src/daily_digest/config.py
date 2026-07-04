import os
from dotenv import load_dotenv

def get_config() -> dict[str, str|list[str] ]:
    load_dotenv()
    required = {
        'gitlab_url': os.getenv('GITLAB_URL'),
        'gitlab_token': os.getenv('GITLAB_TOKEN'),
        'gitlab_project_ids': os.getenv('GITLAB_PROJECT_IDS'),
    }

    for key, value in required.items():
        if value is None:
            raise RuntimeError(f'{key} is required')

    required['gitlab_project_ids'] = required['gitlab_project_ids'].split(',')

    return required