import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent,Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
# ===============================================================================
# this file is only for chainlit agent code.
load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# if not OPENROUTER_API_KEY:
#     raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")

# ===================================================================================

history = []
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


# chainlit code start here.
 
@cl.on_message
async def main(message: cl.Message):
    ui_question = message.content
    
    history.append({"role": "user", "content": ui_question})
    # Append the question to the history
    result = await Runner.run(agent, history)
    
    history.append({"role": "assistant", "content": result.final_output})
    
    
    
    await cl.Message(content=result.final_output).send()