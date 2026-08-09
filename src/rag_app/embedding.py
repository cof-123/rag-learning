from sentence_transformers import SentenceTransformer
from .models import Chunk

class EmbeddingModel:
    """文本向量化模型封装。"""

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-zh-v1.5",
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def encode(
        self,
        texts: list[str],
    ):
        return self.model.encode(texts)



def embed_chunks(
        chunks: list[Chunk],
        model: EmbeddingModel,
    ) -> list[Chunk]:
        """给Chunk生成embedding。"""

        texts = [
            chunk.content
            for chunk in chunks
        ]

        vectors = model.encode(texts)

        for chunk, vector in zip(chunks, vectors):
            chunk.embedding = vector.tolist()

        return chunks