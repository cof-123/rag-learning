import faiss
import numpy as np


vectors = np.array(
    [
        [0.0, 0.0],
        [1.0, 1.0],
        [5.0, 5.0],
    ],
    dtype="float32",
)


index = faiss.IndexFlatL2(2)

index.add(vectors)


query = np.array(
    [
        [0.1, 0.1]
    ],
    dtype="float32",
)


distances, indices = index.search(
    query,
    3,
)


print("索引：")
print(indices)

print()

print("距离：")
print(distances)