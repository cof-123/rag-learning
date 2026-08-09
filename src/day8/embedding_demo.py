from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "BAAI/bge-small-zh-v1.5"
)


texts = [
    "什么是RAG",
    "Retrieval Augmented Generation",
    "今天天气很好",
]


embeddings = model.encode(texts)


similarity = cosine_similarity(
    embeddings
)


print(similarity)