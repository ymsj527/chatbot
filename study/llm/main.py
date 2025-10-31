from chatbot_ai import ai
from prompt import chatbot_prompt as p
from common import base,func

# token追踪
from langchain_classic.callbacks import get_openai_callback


llm = ai.llm

#起名大师
# a = llm.generate(prompts=[p.get_prompt_name_msg]).generations
# txt = a[0][0].text


# 格式化输出
# base.CommaSeparatedListOutputParser().parse(text=txt)

# 程序翻译
# a = base.CustPrompt(input_variables=["function_name"])
# pm = a.format(function_name=func.hello_world)
# pm_msg = llm.invoke(pm)
# print(pm_msg)

# llm.invoke(p.get_f_sting_template_prompt)
# llm.invoke(p.get_jinja2_template_prompt_msg)

# 流式
# llm.stream()

#  追踪token
# with get_openai_callback() as cb:
#     result = llm.invoke("讲一个笑话")
#     print(result)
#     print(cb)







