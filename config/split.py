# 文档转换器

# 文档切割
### 原理
# 1. 将文档分成小的、有意义的块（句子）。
# 2. 将小的块组合成一个更大的块，直到达到一定的大小。
# 3. 一旦达到一定的大小，接着开始创建与下一个块重叠的部分


from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        # 使用递归字符切分器
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,  # 切割的块大小 一般通过长度函数计算
            chunk_overlap=50,  # 切分的文本块重叠大小，
            length_function=len,  # 长度函数，也可以传递tokenize函数
            add_start_index=True,  # 是否添加开始索引
        )

        text = text_splitter.create_documents([data])
        print(text)

# get_text_splitter("../study/test.txt")

from langchain_classic.text_splitter import CharacterTextSplitter

def get_char_splitter(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        char_splitter = CharacterTextSplitter(
            separator="。",  # 切割标识符 默认是换行
            chunk_size=50,
            chunk_overlap=20,
            length_function=len,
            add_start_index=True,
            is_separator_regex=False,  # 是否是正则表达式
        )
        text = char_splitter.create_documents([data])
        print(text)


# get_char_splitter("../study/test.txt")

# 代码文档切割
from langchain_classic.text_splitter import  PythonCodeTextSplitter,Language

#支持解析的编程语言有
# [e.value for e in Language]
# 检测代码是哪种语言
def get_code_splitter(txt):
    txt_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=50,  # 切割的块大小 一般通过长度函数计算
        chunk_overlap=10,  # 切分的文本块重叠大小，
    )

    py = txt_splitter.create_documents([txt])
    print(py)

# 按token来切割
def get_token_splitter(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        py_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=4000,  # 切割的块大小 一般通过长度函数计算
            chunk_overlap=30,  # 切分的文本块重叠大小，
        )
        text = py_splitter.create_documents([data])
        print(text)

# 文档的总结、精炼、翻译
# from doctran_openai import Doctran
#
# doctran = Doctran(
#     openai_api_key=openai_api_key,
#     model=openai_model,
#     max_tokens=1000,
# )
#
# document = doctran.create_document(content=content)
#
# summary = document.summarize(document=document, token_limit=100).execute()
# print(summary.transformed_summary)
#
# #翻译文档
# translation = document.translate(language="zh").execute()
# print(translation.transformed_content)
#
# # 精炼文档 删除除了某主题或关键字之外的内容，仅保留与主题相关的内容
# refined = document.refine(
#     topics=["marketing"],
# ).execute()
# print(refined.transformed_content)

