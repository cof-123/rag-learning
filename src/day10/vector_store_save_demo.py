from src.rag_app.vector_store import VectorStore
from src.rag_app.models import Chunk


chunks = [
    Chunk(
        content="RAG是什么",
        chunk_id=0,
        source="demo.txt",
        embedding=[0.1,0.2,0.3],
    ),

    Chunk(
        content="向量数据库是什么",
        chunk_id=1,
        source="demo.txt",
        embedding=[0.2,0.3,0.4],
    ),
]


store = VectorStore(
    dimension=3
)


store.add(chunks)


store.save(
    "output/test.index"
)


print("保存完成")