import faiss
import numpy as np

from .models import Chunk


class VectorStore:
    """基于FAISS的向量存储。"""

    def __init__(
        self,
        dimension: int,
    ):
        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.chunks: list[Chunk] = []


    def add(
        self,
        chunks: list[Chunk],
    ) -> None:
        """添加Chunk及对应向量。"""

        vectors = np.array(
            [
                chunk.embedding
                for chunk in chunks
            ],
            dtype="float32",
        )

        self.index.add(vectors)

        self.chunks.extend(chunks)


    def search(
        self,
        query_vector,
        top_k: int = 3,
    ) -> list[Chunk]:
        """搜索相似Chunk。"""

        query_vector = np.array(
            [query_vector],
            dtype="float32",
        )

        distances, indices = self.index.search(
            query_vector,
            top_k,
        )

        results = []

        for idx in indices[0]:
            results.append(
                self.chunks[idx]
            )

        return results