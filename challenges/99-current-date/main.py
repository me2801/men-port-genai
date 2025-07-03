import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from datetime import datetime 
from dotenv import load_dotenv

session = GenAISession(jwt_token=AGENT_JWT)
AGENT_JWT = os.environ.get("AGENT_JWT")

session = GenAISession(
    jwt_token=AGENT_JWT
)


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
