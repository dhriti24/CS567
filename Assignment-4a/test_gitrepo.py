import pytest
from gitrepo import get_commits
from unittest.mock import patch

@patch("gitrepo.requests.get")
def test_get_commits_valid_user(mock_get):
    
    expected = [{"name": "csp", "commits": 9},
                {"name": "hellogitworld", "commits": 9},
                {"name": "helloworld", "commits": 9},
                {"name": "Mocks", "commits": 9},
                {"name": "Project1", "commits": 9},
                {"name": "richkempinski", "commits": 9},
                {"name": "threads-of-life", "commits": 9},
                {"name": "try_nbdev", "commits": 9},
                {"name": "try_nbdev2", "commits": 9},
                ]
    
    mock_get.return_value.json.return_value = expected

    result = get_commits("richkempinski")

    assert result == ['Repo: csp Number of commits: 9', 
                      'Repo: hellogitworld Number of commits: 9', 
                      'Repo: helloworld Number of commits: 9', 
                      'Repo: Mocks Number of commits: 9', 
                      'Repo: Project1 Number of commits: 9', 
                      'Repo: richkempinski Number of commits: 9', 
                      'Repo: threads-of-life Number of commits: 9', 
                      'Repo: try_nbdev Number of commits: 9', 
                      'Repo: try_nbdev2 Number of commits: 9']

def test_get_commits_invalid_user():
    result = get_commits("invalid_user")
    assert result == "Username must be alphanumeric"

def test_get_commits_empty_user():
    result = get_commits("")
    assert result == "Please enter a username"
