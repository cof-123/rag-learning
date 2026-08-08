from dataclasses import dataclass, asdict


@dataclass
class Document:
    title: str
    content: str


document = Document(
    title="RAG",
    content="Retrieval Augmented Generation",
)


print("对象:")
print(document)


document_dict = asdict(document)

print("\n转换成dict:")
print(document_dict)


print("\n访问:")
print(document.title)
print(document_dict["title"])