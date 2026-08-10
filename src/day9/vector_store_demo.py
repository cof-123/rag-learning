import faiss
import numpy as np


chunks = [
    "RAG是什么",
    "向量数据库是什么",
    "今天天气很好",
]


vectors = np.array(
    [
        [0.1,0.2,0.3],
        [0.2,0.3,0.4],
        [0.9,0.8,0.7],
    ],
    dtype="float32",
)


index = faiss.IndexFlatL2(
    3
)

index.add(vectors)


query = np.array(
    [
        [0.1,0.2,0.25]
    ],
    dtype="float32",
)


distance, indices = index.search(
    query,
    2,
)


for idx in indices[0]:
    print(
        "找到:",
        chunks[idx]
    )