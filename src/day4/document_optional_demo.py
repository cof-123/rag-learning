from dataclasses import dataclass


@dataclass
class Document:
    title: str
    source: str
    content: str
    author: str | None = None


doc1 = Document(
    title="RAG Introduction",
    source="article.txt",
    content="Hello RAG",
)


doc2 = Document(
    title="Knowledge Graph",
    source="kg.txt",
    content="Entity prediction",
    author="Xu Yi",
)


print(doc1)

print(doc2)