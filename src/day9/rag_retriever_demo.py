import faiss
import numpy as np

from src.rag_app.embedding import (
    EmbeddingModel,
)

from src.rag_app.models import Chunk


# 1.准备知识库Chunk

chunks = [
    Chunk(
        content="RAG是一种检索增强生成技术",
        chunk_id=0,
        source="demo.txt",
    ),

    Chunk(
        content="向量数据库用于保存Embedding向量",
        chunk_id=1,
        source="demo.txt",
    ),

    Chunk(
        content="今天天气很好",
        chunk_id=2,
        source="demo.txt",
    ),
]


# 2.加载Embedding模型

model = EmbeddingModel()


texts = [
    chunk.content
    for chunk in chunks
]


# 3.生成知识库向量

vectors = model.encode(
    texts
)


vectors = np.array(
    vectors,
    dtype="float32"
)


# 4.创建FAISS

dimension = vectors.shape[1]


index = faiss.IndexFlatL2(
    dimension
)


index.add(
    vectors
)


# 5.用户问题

query = [
    "什么是RAG"
]


query_vector = model.encode(
    query
)


query_vector = np.array(
    query_vector,
    dtype="float32"
)


# 6.搜索

distance, indices = index.search(
    query_vector,
    2,
)


# 7.输出结果

for idx in indices[0]:
    print(
        "检索结果:",
        chunks[idx].content
    )