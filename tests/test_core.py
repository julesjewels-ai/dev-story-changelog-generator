"""
Unit tests for core logic.
"""
import pytest
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