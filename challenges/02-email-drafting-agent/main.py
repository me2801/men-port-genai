import asyncio
import os
from typing import Any, Annotated

from dotenv import load_dotenv
from genai_session.session import GenAISession
from openai import OpenAI

load_dotenv()

OPENAPI_KEY = os.environ.get("OPENAPI_KEY")
AGENT_JWT = os.environ.get("AGENT_JWT")

openai_client = OpenAI(
    api_key=AGENT_JWT
)

session = GenAISession(
    jwt_token=""
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
    await session.process_events()


if __name__ == "__main__":
    asyncio.run(main())