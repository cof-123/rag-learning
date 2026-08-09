from dataclasses import dataclass


@dataclass
class Chunk:
    content: str
    chunk_id: int
    source: str


chunks = [
    Chunk(
        content="RAG introduction",
        chunk_id=0,
        source="paper.pdf",
    ),
    Chunk(
        content="Vector database",
        chunk_id=1,
        source="paper.pdf",
    ),
]


for chunk in chunks:
    print(chunk)