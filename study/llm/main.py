from langchain_community.chat_models import ChatSparkLLM
from langchain_classic.prompts import PromptTemplate
from dotenv import load_dotenv
import os

#  加载环境
load_dotenv()

# os.getenv()

sp_llm = ChatSparkLLM(
    spark_api_url="https://spark-api-open.xf-yun.com/v1/chat/completions",
    spark_app_id="34aa2cd9",
    spark_api_key="72963ae6510313ad117a9edb1996105f",
    spark_api_secret="ZTNhYzkyYWM0Y2UxN2Q0NGQxNDAzNTdk",
    request_timeout=30,
    streaming=True,
)

prompt = PromptTemplate.from_template("你是一个起名大师,请模仿示例起3个{county}名字,比如男孩经常被叫做{boy},女孩经常被叫做{girl}")
message = prompt.format(county="中国特色的",boy="狗蛋",girl="翠花")

sp_llm.generate()

