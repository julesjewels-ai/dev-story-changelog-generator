"""
Main business logic for DevStory.
"""
from typing import List, Dict, Any
import datetime
import git
import os
from dotenv import load_dotenv
from openai import OpenAI

class DevStoryApp:
    """
    Orchestrates the retrieval of git history and generation of narrative text.
    """

    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
            print("Warning: OPENAI_API_KEY not found. AI features will be disabled.")

    def _get_commits(self, repo_path: str) -> List[Dict[str, str]]:
        """
        Extracts commit history from a git repository.
        """
        try:
            repo = git.Repo(repo_path)
            commits = []
            # Fetch last 20 commits
            for commit in list(repo.iter_commits(max_count=20)):
                commits.append({
                    "hash": commit.hexsha,
                    "author": commit.author.name,
                    "date": str(commit.committed_datetime),
                    "message": commit.message.strip()
                })
            return commits
        except git.exc.InvalidGitRepositoryError:
            print(f"Warning: {repo_path} is not a valid git repository.")
            return []
        except Exception as e:
            print(f"Error accessing git repository: {e}")
            return []

    def _generate_narrative(self, commits: List[Dict[str, str]]) -> str:
        """
        Transforms technical commit messages into a narrative story using AI.
        Falls back to rule-based generation if AI is unavailable.
        """
        if not commits:
            return "No changes found."

        if self.client:
            try:
                commit_text = "\n".join([f"- {c['message']} (Author: {c['author']})" for c in commits])
                prompt = (
                    "You are a technical writer. Transform the following git commit history into a "
                    "readable, narrative-style release note. Group them logically and highlight key changes.\n"
                    "Use Markdown format.\n\n"
                    f"{commit_text}"
                )

                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that writes release notes."},
                        {"role": "user", "content": prompt}
                    ]
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"Error generating AI narrative: {e}")
                return "Error generating narrative via AI. Please check logs."

        # Fallback to rule-based narrative generation
        lines = [
            f"# Engineering Update ({datetime.date.today()})",
            "",
            "## Key Highlights",
            "The team has been focused on stability and security this sprint.",
            ""
        ]

        features = [c for c in commits if c['message'].startswith('feat')]
        fixes = [c for c in commits if c['message'].startswith('fix')]
        refactors = [c for c in commits if c['message'].startswith('refactor')]
        others = [c for c in commits if c not in features and c not in fixes and c not in refactors]

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

        if others:
             lines.append("### Other Changes")
             for c in others:
                 lines.append(f"- {c['message']}")

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