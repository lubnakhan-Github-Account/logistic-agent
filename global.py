from agents import Agent, RunConfig,Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_default_openai_client,set_tracing_disabled,set_default_openai_api

import os
from dotenv import load_dotenv

# ===============================================================================

load_dotenv()

set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ===================================================================================


agent = Agent(
    
    name = "myCustomAgent",
    instructions="you are a helpful assistant.",
    model= "deepseek/deepseek-chat-v3-0324:free"
)
# =================================================================================
client = AsyncOpenAI(
    
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
    
    
)


set_default_openai_client(client)
    
result = Runner.run_sync(agent,"What is your name?")
print(result.final_output)    
