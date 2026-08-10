import faiss
import numpy as np


# 假设三个512维向量
vectors = np.array(
    [
        [0.1, 0.2, 0.3],
        [0.2, 0.3, 0.4],
        [0.9, 0.8, 0.7],
    ],
    dtype="float32",
)


# 向量维度
dimension = 3


# 创建索引
index = faiss.IndexFlatL2(
    dimension
)


# 添加向量
index.add(vectors)


print("向量数量:")
print(index.ntotal)


# 查询向量
query = np.array(
    [
        [0.1,0.2,0.25]
    ],
    dtype="float32",
)


# 搜索最近的2个
distance, indices = index.search(
    query,
    2,
)


print("距离:")
print(distance)

print("索引:")
print(indices)