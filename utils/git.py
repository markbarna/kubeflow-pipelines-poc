import os
from datetime import datetime

from utils.paths import PROJECT_ROOT


def get_current_commit(full=False) -> str:
    """
    Retrieve the current git commit hash.
    :param full: If True, Return the full string. Otherwise, return the first-eight characters
    :return: commit hash
    """
    with open(os.path.join(PROJECT_ROOT, '.git', 'logs', 'HEAD'), 'r') as f:
        hash_string = f.readlines()[-1][41:73]

    if full is True:
        return hash_string

    return hash_string[:8]


def create_version_name() -> str:
    """
    Create a pipeline version name from the commit hash and timestamp.
    :return: a pipeline version name
    """
    commit = get_current_commit()
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%MZ')
    return f'{commit}_{timestamp}'
