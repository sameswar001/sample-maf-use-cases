import asyncio
from dis import Instruction
from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

async def main():
    Instructions = "You are good at telling jokes."
    async with (

        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            instructions=Instructions
        ) as agent,
    ):
        result = await agent.run("Tell me joke about AI agents")
        print(result.text)

if __name__ == "__main__":
    asyncio.run(main())