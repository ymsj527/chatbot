from config import conf
from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI

llm = OpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=conf.OPEN_AI_KEY,
    )


