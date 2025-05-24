import os
from dotenv import load_dotenv
from agents import Agent, RunConfig,Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
# ===============================================================================

load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ===================================================================================


agent = Agent(
    
    name = "myCustomAgent",
    instructions="you are a helpful assistant.",
)
# =================================================================================
client = AsyncOpenAI(
    
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
    
    
)

config = RunConfig(
    
     model = OpenAIChatCompletionsModel(model= "deepseek/deepseek-chat-v3-0324:free",openai_client=client),
    model_provider="client",
    tracing_disabled=True,
    
    
)

    
result = Runner.run_sync(agent,"What is your name?", run_config=config)
print(result.final_output)    








