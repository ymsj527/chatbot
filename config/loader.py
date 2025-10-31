# Loader机制
# - 加载markdown
# - 加载csv
# - 加载文件目录
# - 加载html
# - 加载json
# - 加载pdf

# ------------------------ TextLoader --------------------
# from langchain_classic.document_loaders import TextLoader  # 已弃用
from langchain_community.document_loaders import TextLoader

def get_text_loader(path):
    loaders = TextLoader(path)

    return loaders

# ---------------------CSVLoader-----------------------------------
from langchain_community.document_loaders import CSVLoader

def get_csv_loader(path):
    loaders = CSVLoader(path)
    return loaders


# -----------------------DirectoryLoader excel----------------------------------------
# 某个目录下有 excel文件，我们需要把目录下的文件加载进来
from langchain_community.document_loaders import DirectoryLoader

def get_excel(path):
    loaders = DirectoryLoader(path=path, glob="*.xlsx")
    docs = loaders.load()
    return docs

# --------------------------BSHTMLLoader------------------------------------------
# from langchain_classic.document_loaders import UnstructuredHTMLLoader
# loader = UnstructuredHTMLLoader("loader.html")
from langchain_community.document_loaders import BSHTMLLoader

def get_bs_html_loader(path):
    data = BSHTMLLoader(path)
    return data.load()


# ------------JSONLoader--------------------
from common.base import JSONLoader

def get_json_loader(path):
    loaders = JSONLoader(path)
    return loaders.load()


# -------------------------PyPDFLoader---------------------------------
from langchain_community.document_loaders import PyPDFLoader

def get_pypdf_loader(path):
    loaders = PyPDFLoader(path)
    return loaders.load_and_split()







