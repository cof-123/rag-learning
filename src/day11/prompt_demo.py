from src.rag_app.models import Chunk
from src.rag_app.prompt import build_prompt


chunks = [
    Chunk(
        content="RAG combines retrieval with large language models.",
        chunk_id=0,
        source="sample.md",
    ),
    Chunk(
        content="It can provide external knowledge.",
        chunk_id=1,
        source="sample.md",
    ),
]


prompt = build_prompt(
    "什么是RAG?",
    chunks,
)


print(prompt)