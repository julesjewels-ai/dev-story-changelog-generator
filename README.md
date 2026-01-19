# DevStory: Narrative Changelog Generator

An AI-powered documentation tool that connects to Git repositories to transform technical commit history, code diffs, and pull request comments into readable, narrative-style release notes and stakeholder updates. It helps engineering teams communicate progress to non-technical management without manual report writing.

## Tech Stack

- TypeScript
- Next.js
- OpenAI API
- LangChain
- Prisma
- PostgreSQL
- Tailwind CSS

## Features

- One-click Git repository synchronization
- AI summarization of commits into semantic groups
- Adjustable output tone (Developer, Manager, Public Blog)
- Automated drafting of weekly progress emails
- Export to Markdown, HTML, or PDF

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd devstory:-narrative-changelog-generator
make install

# Run the application
make run
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
make install && make run
```

## Development

```bash
make install  # Create venv and install dependencies
make run      # Run the application
make test     # Run tests
make clean    # Remove cache files
```

## Testing

```bash
pytest tests/ -v
```
