from .embedding import EmbeddingModel
from .vector_store import VectorStore
from .models import SearchResult


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
        top_k: int = 5,
        absolute_threshold: float = 0.35,
        relative_ratio: float = 0.85,
        debug: bool = False,
    ) -> list[SearchResult]:

        query_vector = self.embedding_model.encode(
            [query]
        )[0]

        results = self.vector_store.search(
            query_vector,
            top_k,
        )

        if not results:
            return []

        best_score = results[0].score

        threshold = max(
            absolute_threshold,
            best_score * relative_ratio,
        )

        filtered_results = [
            result
            for result in results
            if result.score >= threshold
        ]

        if debug:
            print()
            print("=== Retriever Debug ===")
            print(f"Query: {query}")
            print(f"Best score: {best_score:.4f}")
            print(f"Absolute threshold: {absolute_threshold:.4f}")
            print(
                f"Relative threshold: "
                f"{best_score * relative_ratio:.4f}"
            )
            print(f"Final threshold: {threshold:.4f}")
            print()

            for result in results:
                status = (
                    "保留"
                    if result.score >= threshold
                    else "过滤"
                )

                print(
                    f"[{status}] "
                    f"score={result.score:.4f} "
                    f"source={result.chunk.source}"
                )

                print(
                    result.chunk.content[:100]
                )

                print("-" * 60)

        return filtered_results