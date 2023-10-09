from datetime import datetime
import re
import requests

def get_commits(userId):
    url = f"https://api.github.com/users/{userId}/repos"
    try:
        test_userId = validate_userId(userId)
        if(test_userId):
            return test_userId
        response = requests.get(url)
        response.raise_for_status()

        repos = [repo["name"] for repo in response.json()]
        if len(repos) <= 0:
            return "No repositories found"
        
        git_commits = []
        for repo in repos:
            url = f"https://api.github.com/repos/{userId}/{repo}/commits"
            response = requests.get(url)
            response.raise_for_status()
            user_commits = response.json()
            user_commits_count = len(user_commits)
            git_commits.append(f"Repo: {repo} Number of commits: {user_commits_count}")
        return git_commits
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return "User not found"
        elif response.status_code == 403:
            return "API rate limit exceeded"
        else:
            return (f"HTTP error occured: {err}")
        
def validate_userId(userId):
    if userId == "":
        return "Please enter a username"
    elif not isinstance(userId, str):
        return "Username must be a string"
    elif not re.match("^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$", userId):
        return "Username must be alphanumeric"
    return False

if __name__ == "__main__":
    userId = input("Enter a GitHub username: ")
    git_repo = get_commits(userId)
    print(git_repo)

    if type(git_repo) == list:
        for repo in git_repo:
            print(repo)
    else:
        print(git_repo)
        