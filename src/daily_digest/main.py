from daily_digest.config import get_config
from daily_digest.connectors.gitlab import get_merge_requests
from daily_digest.connectors.redmine import get_assigned_issues
from daily_digest.renderers.terminal import render_merge_requests


def main():
    config = get_config()
    result = get_merge_requests(config)
    render_merge_requests(result)
    print(get_assigned_issues(config))


if __name__ == '__main__':
    main()
