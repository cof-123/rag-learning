import faiss
import numpy as np

from src.rag_app.chunk_loader import load_chunks_from_json
from src.rag_app.embedding import EmbeddingModel
from src.rag_app.vector_store import VectorStore


chunks = load_chunks_from_json(
    "output/chunks.json"
)

vector_store = VectorStore.load(
    "output/faiss.index",
    chunks,
)

embedding_model = EmbeddingModel()


query = "什么是RAG"

query_embedding = embedding_model.encode(
    [query]
)

query_embedding = np.array(
    query_embedding,
    dtype="float32",
)

faiss.normalize_L2(
    query_embedding
)


scores, indices = vector_store.index.search(
    query_embedding,
    5,
)



results = vector_store.search(
    query_embedding[0],
    top_k=5,
)

for result in results:
    print(f"相似度: {result.score:.4f}")
    print(result.chunk.content[:100])
    print("-" * 50)