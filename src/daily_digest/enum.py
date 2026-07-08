from enum import Enum


class GitlabMergeRequestsStatus(str, Enum):
    OPENED = 'opened'
    CLOSED = 'closed'
    LOCKED = 'locked'
    MERGED = 'merged'
    ALL = 'all'


class RedmineIssueRequest(str, Enum):
    ASSIGNED = 'assigned'
    EXPIRED = 'expired'
