import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from datetime import datetime 

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYjM2NWIyMS1mODVkLTRhZWYtYThhZS04ZmE2MTMwYWI5MDgiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6ImE0MjlmNmQyLTdkZmYtNDQyNi05ZWU4LWU5OGZmNzkyNzFiNiJ9.Gkb7dHpDcNti8OnShRzXn4oqd4pIXQq6_1MACI6ODcY" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="current_date",
    description="Return current date"
)
async def current_date(
    agent_context: GenAIContext):
    agent_context.logger.info("Inside get current date")
    return datetime.now().strftime("%Y-%m-%d")


async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
