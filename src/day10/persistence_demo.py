from src.rag_app.chunk_exporter import save_chunks_as_json
from src.rag_app.chunk_loader import load_chunks_from_json
from src.rag_app.models import Chunk
from src.rag_app.vector_store import VectorStore


chunks = [
    Chunk(
        content="RAG是什么",
        chunk_id=0,
        source="demo.txt",
        embedding=[0.1, 0.2, 0.3],
    ),
    Chunk(
        content="向量数据库是什么",
        chunk_id=1,
        source="demo.txt",
        embedding=[0.2, 0.3, 0.4],
    ),
]


# ---------- 构建并保存 ----------

store = VectorStore(
    dimension=3
)

store.add(chunks)

store.save(
    "output/test.index"
)

save_chunks_as_json(
    chunks,
    "output/test_chunks.json",
)


# ---------- 模拟重新启动程序 ----------

loaded_chunks = load_chunks_from_json(
    "output/test_chunks.json"
)

loaded_store = VectorStore.load(
    "output/test.index",
    loaded_chunks,
)


results = loaded_store.search(
    [0.1, 0.2, 0.25],
    top_k=2,
)


for chunk in results:
    print(
        chunk.content,
        chunk.embedding,
    )