# Gemini AI Agent
An AI agent built in Python with Gemini 1.12.1.

## Restrictions
The agent is limited to files and folders within the working directory.

## Functions
The agent may call upon the functions specified below based upon the prompts given.

### Get Files Information
The agent can retrieve a file's size and directory. The same can be returned for all files in a directory.

### Get File Content
The agent can return the contents of a file as a string. However, this is limited to the first 10,000 characters.

### Write File
The agent can write new or edit existing files when the prompt includes the content to be written or directs the type of change to be made, e.g, Fix the bug in main.py causing the loop to break too early.

### Run Python File
The agent can run files and will return the text results of the run file's output to `stdout`. There is a 30 second timeout. Errors will be returned to `stderr`.

## Instructions
To run the project, use `uv run main.py` followed by arguments in `""`. See requirements below as well. A virtual environment is required and may be setup by installing `UV` below and entering `source .venv/bin/activate` within the project folder once configured.

## Requirements
- Python 3.10+
- [UV](https://github.com/astral-sh/uv) project and package manager
- Runs a in zsh or bash, unix-like shell
- Google GenAI (Gemini) 1.12.1
- A [Google AI Studio](https://aistudio.google.com/) account
- A Google AI API key generated ([docs here](https://ai.google.dev/gemini-api/docs/api-key))
- Python dotenv 1.1.0
