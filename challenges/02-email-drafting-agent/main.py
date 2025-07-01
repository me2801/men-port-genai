import asyncio
from typing import Annotated
import os
import sys



from genai_session.session import GenAISession

from email_generator import generate_email  # you will define this separately

session = GenAISession()

@session.bind(
    name="email_drafter",
    description="Generate a professional email from bullet-point input."
)
async def draft_email(
    agent_context,
    recipient: Annotated[str, "Recipient's name or role"],
    purpose: Annotated[str, "Purpose of the email"],
    points: Annotated[list[str], "List of bullet points to include"]
) -> dict:
    return generate_email(recipient, purpose, points)

async def main():
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
