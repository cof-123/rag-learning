from src.rag_app.llm_client import LLMClient


client = LLMClient(
    base_url="http://192.168.153.223:11434",
    model="deepseek-r1:32b",
)


answer = client.generate(
    "请用一句话解释什么是RAG。"
)


print(answer)