# 格式化输出
from langchain_classic.schema import BaseOutputParser

from langchain_core.prompts import StringPromptTemplate

from common import func

from prompt import chatbot_prompt

from langchain_classic.docstore.document import Document

from langchain_classic.document_loaders.base import BaseLoader

import json

from pathlib import Path

from typing import Callable, Dict, List, Optional, Union

#自定义类
class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        print(text)
        return text.strip().split(",")


# 自定义的模板Class
class CustPrompt(StringPromptTemplate):

    def format(self, **kwargs) -> str:
        # 获得源代码
        source_code = func.get_source_code(kwargs['function_name'])

        # 生成提示词模板
        prompt = chatbot_prompt.Get_PROMPT.format(
            function_name=kwargs['function_name'].__name__, source_code=source_code
        )
        return prompt

# 加载json文件
class JSONLoader(BaseLoader):
    def __init__(
        self,
        file_path: Union[str, Path],
        content_key: Optional[str] = None,
        metadata_func: Optional[Callable[[dict, dict], dict]] = None,
    ):
        """
        Initializes the JSONLoader with a file path, an optional content key to extract specific content,
        and an optional metadata function to extract metadata from each record.
        """
        self.file_path = Path(file_path).resolve()
        self.content_key = content_key
        self.metadata_func = metadata_func

    def create_documents(self, processed_data):
        """
        Creates Document objects from processed data.
        """
        documents = []
        for item in processed_data:
            content = item.get('content', '')
            metadata = item.get('metadata', {})
            document = Document(page_content=content, metadata=metadata)
            documents.append(document)
        return documents

    def process_json(self, data):
        """
        Processes JSON data to prepare for document creation, extracting content based on the content_key
        and applying the metadata function if provided.
        """
        processed_data = []
        if isinstance(data, list):
            for item in data:
                content = item.get(self.content_key, '') if self.content_key else ''
                metadata = {}
                if self.metadata_func and isinstance(item, dict):
                    metadata = self.metadata_func(item, {})
                processed_data.append({'content': content, 'metadata': metadata})
        return processed_data

    def load(self) -> List[Document]:
        """
        Load and return documents from the JSON file.
        """
        docs = []
        with open(self.file_path, mode="r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
                processed_json = self.process_json(data)
                docs = self.create_documents(processed_json)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in the file.")
        return docs