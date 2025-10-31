from langchain_core.prompts import PromptTemplate

#字符模板 -----------------------------LLM chat PromptTemplate --------------------
#起名大师
get_prompt_name = PromptTemplate.from_template("你是一个起名大师,请模仿示例起3个具有{county}特色的名字,示例：男孩常用名{boy},女孩常用名{girl}。请返回以逗号分隔的列表形式。仅返回逗号分隔的列表，不要返回其他内容。")
get_prompt_name_msg = get_prompt_name.format(county="中国特色的",boy="狗蛋",girl="翠花")
# print(get_prompt_name_msg)


# 对话模板具有结构 ------------------------- chat models ChatPromptTemplate ---------------------
from langchain_classic.prompts import ChatPromptTemplate

get_chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个起名大师，你的名字叫{name}"),
        ("human", "你好{name}，你感觉如何？"),
        ("ai", "我的状态还行"),
        ("human", "{user_input}"),
    ]
)

get_chat_template_msg = get_chat_template.format_messages(name="算命大师", user_input="你叫什么名字呢？")
# print(get_chat_template_msg)

# 包引入方式
from langchain_classic.schema import SystemMessage,HumanMessage,AIMessage

#直接创建消息
sy = SystemMessage(
    content="你是一个起名大师",
    additional_kwargs={"大师姓名": "陈瞎子"}
)
hu = HumanMessage(
    content="请问大师叫什么"
)
ai = AIMessage(
    content="我叫程瞎子"
)

# print(sy,hu,ai)

# 可以自定义角色 --------------- ChatMessagePromptTemplate ----------------
from langchain_core.prompts import ChatMessagePromptTemplate,AIMessagePromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate

get_chat_prompt_msg = "愿{subjuct}与你同在!"
get_chat_message_prompt = ChatMessagePromptTemplate.from_template(role="天行者", template=get_chat_prompt_msg)
get_chat_message_prompt.format(subjuct="神力")
# print(get_chat_message_prompt)


# 函数大师 根据函数名，查找代码，并给出中午的代码说明 ------------------ StringPromptTemplate -----------------------
from langchain_core.prompts import StringPromptTemplate

Get_PROMPT = """\
你是一个非常有经验和天赋的程序员，现在给你如下函数名称，你会按照如下格式，输出这段代码的名称，源代码，中文解释。
函数名称：{function_name}
源代码:
{source_code}
代码解释:
"""

fsting_template = """
给我讲一个关于{name}的{what}故事
"""

#f-string 是python内置的一种模板引擎
f_sting_template = """
给我讲一个关于{name}的{what}故事
"""
get_f_sting_template_prompt = PromptTemplate.from_template(f_sting_template)
get_f_sting_template_prompt.format(name="悲伤",what="逆流成河的")


#Jinja2 是一个灵活、高效的Python模板引擎，可以方便地生成各种标记格式文档
get_jinja2_template = "给我讲一个关于{{name}}的{{what}}故事"
get_jinja2_template_prompt = PromptTemplate.from_template(get_jinja2_template, template_format="jinja2")
get_jinja2_template_prompt_msg = get_jinja2_template_prompt.format(name="人生",what="如何走好这一生的")



# 组合提示词模板分层 --------------- PipelinePromptTemplate ------------



# 序列化：使用文件来管理提示词模板 ------------------------------- load_prompt ----------------------------------------------
from langchain_classic.prompts import load_prompt
# - 便于分享
# - 便于版本管理
# - 便于存储
# - 支撑常见的格式(json/yaml/txt)

# yaml_prompt = load_prompt("../simple_prompts.yaml")
# print(yaml_prompt.format(name="李白",what="从军"))

# json_prompt = load_prompt("../simple_prompts.json")
# print(json_prompt.format(name="花木兰",what="从军"))

















