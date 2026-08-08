from dataclasses import dataclass


@dataclass
class Document:
    title: str
    source: str
    content: str
    character_count: int


document = Document(
    title="RAG Introduction",
    source="article.txt",
    content="Hello RAG",
    character_count=9,
)


print(document)

print(document.title)

print(document.content)