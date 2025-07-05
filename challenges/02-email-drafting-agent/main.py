"""
email_agent.py

This module defines an Email Drafting Agent built for the GenAI AgentOS platform.
It leverages OpenAI's GPT models to convert bullet-point-style inputs into a 
professional email draft. The agent can be registered and executed on the AgentOS 
platform.

Features:
- Accepts a recipient, purpose, and bullet points describing key content.
- Returns a complete email including subject, greeting, body, and closing.
- Uses OpenAI's GPT-4o-mini model for natural language generation.

Environment Variables:
- OPENAPI_KEY: API key for authenticating with the OpenAI API.
- AGENT_JWT: JWT token used for registering the agent session.

Usage:
Run this file directly to start processing agent events in the GenAI AgentOS platform.
"""

import asyncio
import os
from typing import Any, Annotated

from dotenv import load_dotenv
from genai_session.session import GenAISession
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv()

# Retrieve API keys and tokens from environment variables
OPENAPI_KEY = os.environ.get("OPENAPI_KEY")
AGENT_JWT = os.environ.get("AGENT_JWT")
ROUTER_WS_URL = os.environ.get("ROUTER_WS_URL")

# Initialize OpenAI client
openai_client = OpenAI(
    api_key=OPENAPI_KEY
)

# Initialize GenAI session, using router_ws_url if provided
if ROUTER_WS_URL:
    print(f"[INFO] Connecting to router at: {ROUTER_WS_URL}")
    session = GenAISession(
        jwt_token=AGENT_JWT,
        router_ws_url=ROUTER_WS_URL
    )
else:
    print("[INFO] Connecting to default router (localhost)")
    session = GenAISession(
        jwt_token=AGENT_JWT
    )

@session.bind(
    name="email_drafter",
    description="Generate a professional email from bullet-point input."
)
async def get_email(
    agent_context,
    recipient: Annotated[str, "Recipient's name or role"],
    purpose: Annotated[str, "Purpose of the email"],
    points: Annotated[list[str], "List of bullet points to include"]
) -> dict[str, Any]:
    """
    Generates a professional email draft based on user-provided bullet points.

    Args:
        agent_context: The context object provided by GenAI AgentOS (includes logging).
        recipient (str): The name or role of the email recipient.
        purpose (str): The purpose or subject matter of the email.
        points (list[str]): Bullet points containing the key details to include.

    Returns:
        dict[str, Any]: A dictionary containing the generated email text under the key "translation".

    Notes:
        - This function sends a prompt to the OpenAI GPT-4o-mini model to compose the email.
        - The response includes a subject line, greeting, body, and closing.
    """
    agent_context.logger.info("Inside get_email")
    
    prompt = (
        f"You are an expert email writing assistant. "
        f"Write a clear and professional email based on the following information:\n\n"
        f"Recipient: {recipient}\n"
        f"Purpose: {purpose}\n"
        f"Key Points:\n" + "\n".join(f"- {point}" for point in points) + "\n\n"
        f"The email should include:\n"
        f"- A subject line\n"
        f"- A natural and respectful greeting\n"
        f"- A concise body covering all the key points\n"
        f"- A professional closing.\n\n"
        f"Respond with only the email text."
    )

    response = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4o-mini"
    )
    translation = response.choices[0].message.content
    return {"translation": translation}


async def main():
    """
    Starts the GenAI session and processes incoming agent events.

    This function serves as the entry point when running the script directly.
    """
    await session.process_events()


if __name__ == "__main__":
    asyncio.run(main())
