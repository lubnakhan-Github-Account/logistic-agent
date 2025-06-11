import os
from dotenv import load_dotenv

from agents import Agent,Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
# ===============================================================================
# this file is only for basic agent code.

load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")

# ===================================================================================


client = AsyncOpenAI(
    
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
    
    
)


agent = Agent(
    model = OpenAIChatCompletionsModel(model= "deepseek/deepseek-chat-v3-0324:free",openai_client=client),
    name = "myCustomAgent",
    instructions="you are a helpful assistant.",
)
# ==================================================================================

    # it is main.py code only use for agent.
    
result = Runner.run_sync(agent,"What is your name?")
print(result.final_output)   

# ================================================================

    
      

