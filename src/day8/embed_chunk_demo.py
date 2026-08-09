from src.rag_app.embedding import (
    EmbeddingModel,
    embed_chunks,
)

from src.rag_app.models import Chunk


chunks = [
    Chunk(
        content="RAG是什么",
        chunk_id=0,
        source="demo.txt",
    ),
    Chunk(
        content="向量数据库",
        chunk_id=1,
        source="demo.txt",
    ),
]


model = EmbeddingModel()


chunks = embed_chunks(
    chunks,
    model,
)


for chunk in chunks:
    print(chunk)
    print(
        "embedding长度:",
        len(chunk.embedding)
    )
    print()