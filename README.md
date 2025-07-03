
# MEN-PORT-GENAI

This repository contains a collection of GenAI agent challenges and supporting components.

## Challenges

| Challenge                                      | Description                                                   |
|-----------------------------------------------|---------------------------------------------------------------|
| [02 Email Drafting Agent](challenges/02-email-drafting-agent/README.md)   | Generate a professional email from bullet-point input         |
| [97 Translate Text Agent](challenges/97-translate-text-agent/README.md)   | Translate text from one language to another                   |
| [98 Weather Agent](challenges/98-weather-agent/README.md)                 | Retrieve weather forecast for a specific city and date        |
| [99 Current Date](challenges/99-current-date/README.md)                   | Return the current system date                                |

## Project Structure

```
men-port-genai/
├── challenges/                        # Individual GenAI agents
│   ├── 02-email-drafting-agent/
│   ├── 97-translate-text-agent/
│   ├── 98-weather-agent/
│   └── 99-current-date/
├── genai-agentos/                      # Shared session/router code
├── uv.lock                             # Locked dependency versions
├── pyproject.toml                      # Project dependencies
└── .gitignore                          # Git ignore rules
```

## Running a Challenge

Example for the Email Drafting Agent:

```
cd challenges/02-email-drafting-agent
uv pip install --project .
uv run main.py
```

Make sure you have configured the required environment variables (for example, OPENAI_API_KEY, AGENT_JWT, and any others listed in the agent's README).
