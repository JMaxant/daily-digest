import os
from dotenv import load_dotenv

def get_config() -> dict[str, str]:
    load_dotenv()
    token = os.getenv('GITLAB_TOKEN')
    url = os.getenv('GITLAB_URL')
    if token is None or url is None:
        raise RuntimeError('Both Gitlab url and token are required')

    return {
        'gitlab_url': url,
        'gitlab_token': token,
    }