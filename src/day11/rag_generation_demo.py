from src.rag_app.llm_client import LLMClient
from src.rag_app.models import Chunk
from src.rag_app.prompt import build_prompt


chunks = [
    Chunk(
        content="RAG combines retrieval with large language models.",
        chunk_id=0,
        source="sample.md",
    ),
    Chunk(
        content="It can provide external knowledge to the model.",
        chunk_id=1,
        source="sample.md",
    ),
]


question = "什么是RAG？"


prompt = build_prompt(
    question,
    chunks,
)


client = LLMClient(
    base_url="http://192.168.153.223:11434",
    model="deepseek-r1:32b",
)


answer = client.generate(
    prompt
)


print("最终回答：")
print(answer)