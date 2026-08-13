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
    
    def save(
        self,
        path: str,
        ) -> None:
        """保存FAISS索引。"""

        faiss.write_index(
            self.index,
            path,
        )

    @classmethod
    def load(
        cls,
        path: str,
        chunks: list[Chunk],
    ) -> "VectorStore":
        """加载FAISS索引。"""

        index = faiss.read_index(
            path
        )

        store = cls(
            dimension=index.d
        )

        store.index = index
        store.chunks = chunks

        return store