import json
import requests
from nomad.constants import GITHUB_API_URL, GITHUB_REPO_ORG, GITHUB_REPO_NAME
from nomad.settings import GITHUB_USERNAME, GITHUB_PASSWORD


def make_github_issue(title):
    """
    Create an issue on github.com using the given parameters.
    :param title: title of created issue
    """
    # Our url to create issues via POST
    url = '{base}/repos/{repo_owner}/{repo_name}/issues'.format(
                base=GITHUB_API_URL,
                repo_owner=GITHUB_REPO_ORG,
                repo_name=GITHUB_REPO_NAME)

    # Create our issue
    issue = {'title': title,
             'labels': ["bug"]}

    r = requests.post(url, json.dumps(issue), auth=(GITHUB_USERNAME, GITHUB_PASSWORD))
    if r.status_code == 201:
        print('Successfully created Issue ', title)
    else:
        print('Could not create Issue ', title)
        print('Response:', r.content)
