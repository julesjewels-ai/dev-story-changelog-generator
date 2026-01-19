"""
Unit tests for core logic.
"""
import pytest
from unittest.mock import MagicMock, patch
from src.core.app import DevStoryApp

@pytest.fixture
def app():
    return DevStoryApp()

def test_app_initialization(app):
    """Ensure the app initializes correctly."""
    assert isinstance(app, DevStoryApp)

def test_generate_narrative_with_data(app):
    """Test narrative generation with mock data."""
    mock_commits = [
        {"message": "feat: new api", "author": "Alice", "hash": "123"},
        {"message": "fix: serious bug", "author": "Bob", "hash": "456"}
    ]
    result = app._generate_narrative(mock_commits)
    
    assert "Engineering Update" in result
    assert "New Capabilities" in result
    assert "new api" in result
    assert "serious bug" in result

def test_generate_narrative_empty(app):
    """Test narrative generation with no commits."""
    result = app._generate_narrative([])
    assert result == "No changes found."

def test_run_execution(app):
    """Test the main run method returns a string."""
    # We pass '.' as path, but logic is currently mocked inside
    result = app.run(".")
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_narrative_with_ai(app):
    """Test narrative generation using mocked AI client."""
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "AI Generated Narrative"
    mock_client.chat.completions.create.return_value = mock_response

    app.client = mock_client

    commits = [{"message": "feat: new api", "author": "Alice", "hash": "123"}]
    result = app._generate_narrative(commits)

    assert result == "AI Generated Narrative"
    mock_client.chat.completions.create.assert_called_once()

def test_get_commits_mocked(app):
    """Test _get_commits with mocked git.Repo."""
    with patch("src.core.app.git.Repo") as MockRepo:
        mock_repo_instance = MockRepo.return_value
        mock_commit = MagicMock()
        mock_commit.hexsha = "abc"
        mock_commit.author.name = "Tester"
        mock_commit.committed_datetime = "2023-01-01"
        mock_commit.message = "test commit"
        mock_repo_instance.iter_commits.return_value = [mock_commit]

        commits = app._get_commits("dummy/path")

        assert len(commits) == 1
        assert commits[0]['hash'] == "abc"
        assert commits[0]['message'] == "test commit"