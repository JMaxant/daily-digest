from daily_digest.config import get_config
from daily_digest.connectors.gitlab import get_merge_requests
from daily_digest.renderers.terminal import render_merge_requests


def main():
    config = get_config()
    result = get_merge_requests(config)
    render_merge_requests(result)


if __name__ == '__main__':
    main()
