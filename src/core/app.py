"""
Main business logic for DevStory.
"""
from typing import List, Dict, Any
import datetime

class DevStoryApp:
    """
    Orchestrates the retrieval of git history and generation of narrative text.
    """

    def __init__(self) -> None:
        # In a real implementation, we might initialize LLM clients here
        pass

    def _get_commits(self, repo_path: str) -> List[Dict[str, str]]:
        """
        Simulates extracting commit history from a git repository.
        In a production version, this would use GitPython.
        """
        # Mock data for MVP demonstration
        return [
            {
                "hash": "a1b2c3d",
                "author": "Jane Doe",
                "date": "2023-10-01",
                "message": "feat: implement user authentication middleware"
            },
            {
                "hash": "e4f5g6h",
                "author": "John Smith",
                "date": "2023-10-02",
                "message": "fix: resolve race condition in database pool"
            },
            {
                "hash": "i7j8k9l",
                "author": "Jane Doe",
                "date": "2023-10-03",
                "message": "refactor: optimize image processing algorithm"
            }
        ]

    def _generate_narrative(self, commits: List[Dict[str, str]]) -> str:
        """
        Transforms technical commit messages into a narrative story.
        This mocks what an LLM (e.g., GPT-4) would do.
        """
        if not commits:
            return "No changes found."

        lines = [
            f"# Engineering Update ({datetime.date.today()})",
            "",
            "## Key Highlights",
            "The team has been focused on stability and security this sprint.",
            ""
        ]

        # Simple rule-based narrative generation for MVP
        features = [c for c in commits if c['message'].startswith('feat')]
        fixes = [c for c in commits if c['message'].startswith('fix')]
        refactors = [c for c in commits if c['message'].startswith('refactor')]

        if features:
            lines.append("### New Capabilities")
            for f in features:
                clean_msg = f['message'].replace('feat: ', '')
                lines.append(f"- We introduced **{clean_msg}**, enhancing system security.")
            lines.append("")

        if fixes:
            lines.append("### Stability Improvements")
            for f in fixes:
                clean_msg = f['message'].replace('fix: ', '')
                lines.append(f"- A critical issue was addressed to **{clean_msg}**, ensuring smoother data handling.")
            lines.append("")

        if refactors:
            lines.append("### Technical Debt")
            lines.append(f"- {len(refactors)} background improvements were made to codebase efficiency.")

        return "\n".join(lines)

    def run(self, repo_path: str) -> str:
        """
        Main execution pipeline.

        Args:
            repo_path (str): Path to the repository.

        Returns:
            str: The generated narrative report.
        """
        # 1. Extract context
        commits = self._get_commits(repo_path)
        
        # 2. Process / Analyze (Simulated AI)
        narrative = self._generate_narrative(commits)
        
        return narrative