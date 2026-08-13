from src.rag_app.vector_store import VectorStore
from src.rag_app.models import Chunk


chunks = [
    Chunk(
        content="RAG是什么",
        chunk_id=0,
        source="demo.txt",
    ),

    Chunk(
        content="向量数据库是什么",
        chunk_id=1,
        source="demo.txt",
    ),
]


store = VectorStore.load(
    "output/test.index",
    chunks,
)


results = store.search(
    [0.1,0.2,0.25],
    top_k=2,
)


for chunk in results:
    print(
        chunk.content
    )