import uuid
from pkg import fortune
from fastapi import FastAPI,WebSocket,WebSocketDisconnect,BackgroundTasks
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Qdrant
# from langchain_classic.vectorstores import RecursiveCharacterTextSplitter
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatSparkLLM

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Welcome to chat Fortune telling"}


@app.post("/chat")
def chat(query:str, background_tasks: BackgroundTasks):
    master = fortune.Master()
    msg = master.run(query)
    uni_uid = str(uuid.uuid4()) # 生成唯一标识
    background_tasks.add_task(master.background_voice_synthesis,msg['output'], uni_uid)
    return {"msg": msg, "id": uni_uid}

@app.post("/add_urls")
def add_urls(URL:str):
    loader = WebBaseLoader(URL)
    docs = loader.load()
    docments = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=50,
    ).split_documents(docs)
    #引入向量数据库
    qdrant = Qdrant.from_documents(
        docments,
        ChatSparkLLM(app_id="",api_secret="",api_key=""),
        path="../local_qdrant",
        collection_name="local_documents",
    )
    print("向量数据库创建完成")
    print(qdrant.collection_name)
    return {"ok": "添加成功！"}

@app.post("/add_pdfs")
def add_pdfs():
    return {"Hello": "add_pdfs"}

@app.post("/add_texts")
def add_texts():
    return {"Hello": "add_texts"}


@app.post("/add_images")
def add_images():
    return {"Hello": "add_images"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("WebSocket Disconnected")
        await websocket.close()