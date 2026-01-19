"""
Entry point for the DevStory application.
"""
import argparse
import sys
import os
from src.core.app import DevStoryApp

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DevStory: Narrative Changelog Generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--repo", 
        type=str, 
        default=".", 
        help="Path to the local git repository to analyze"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="DevStory v0.1.0"
    )

    args = parser.parse_args()

    # Validate path
    if not os.path.isdir(args.repo):
        print(f"Error: The path '{args.repo}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    print(f"Starting DevStory analysis on: {os.path.abspath(args.repo)}\n")

    try:
        app = DevStoryApp()
        report = app.run(args.repo)
        print("--- Generated Narrative Report ---\n")
        print(report)
        print("\n--------------------------------")
    except Exception as e:
        print(f"An error occurred during execution: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()