import asyncio
import os 
from dotenv import load_dotenv 
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, OpenAIChatCompletionsModel, set_tracing_disabled, AsyncOpenAI, Runner
# ====================================================
# this file is used to run the agent with streaming response.

load_dotenv()
set_tracing_disabled(disabled=True)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# ====================================================

client = AsyncOpenAI(
    
  api_key=OPENROUTER_API_KEY,
  base_url="https://openrouter.ai/api/v1"  
    
    
)

agent = Agent(
    model= OpenAIChatCompletionsModel(model="google/gemini-2.0-flash-exp:free", openai_client=client),
    name="gemeniAgent",
    instructions="you are a helpful assistant.",
)


async def main():
    
    result=Runner.run_streamed(starting_agent=agent,input="what is your name?",)
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
           print(event.data.delta, end="", flush=True)
        
if __name__ == "__main__":
    asyncio.run(main())        