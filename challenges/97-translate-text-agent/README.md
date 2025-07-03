
# 97 Translate Text Agent

This agent uses OpenAI's GPT API to translate text into a specified language.
It runs as a GenAI agent and listens for translation requests over the GenAI Router.

## Description

Given a text and a target language code, the agent constructs a translation prompt and uses OpenAI's `chat.completions.create()` API to generate the translated text.

Example target language codes:
- "fr" → French
- "es" → Spanish
- "de" → German

## Environment Variables

The following environment variables must be set in a `.env` file in the project root:

```
OPENAPI_KEY=sk-your-openai-api-key
AGENT_JWT=your-agent-router-jwt
```

## Installation

Run the following commands from the `97-translate-text-agent` directory:

```
uv pip install --project .
```

## Running the Agent

Activate the environment and run:

```
uv run main.py
```

The agent will connect to the GenAI Router and wait for translation events.

## Exposed Function

| Function Name   | Description                          | Parameters                              | Returns               |
|-----------------|--------------------------------------|-----------------------------------------|-----------------------|
| get_translation | Translate the given text to a language | text: str, language: str                | { "translation": str } |

## Example Usage (if using an AgentOS client)

Request:

```
{
  "function": "get_translation",
  "parameters": {
    "text": "Hello, how are you?",
    "language": "es"
  }
}
```

Response:

```
{
  "translation": "Hola, ¿cómo estás?"
}
```
