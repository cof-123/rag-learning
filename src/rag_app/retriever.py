from .embedding import EmbeddingModel
from .vector_store import VectorStore
from .models import Chunk


class Retriever:
    """负责查询并返回相关Chunk。"""

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store


    def search(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[Chunk]:

        query_vector = self.embedding_model.encode(
            [query]
        )[0]

        return self.vector_store.search(
            query_vector,
            top_k,
        )