from src.rag_app.embedding import EmbeddingModel


model = EmbeddingModel()


texts = [
    "RAG是什么",
    "向量数据库"
]


vectors = model.encode(texts)


print(type(vectors))
print(vectors.shape)