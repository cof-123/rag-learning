import json
from pathlib import Path


def load_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"文件不存在：{path.resolve()}")

    return path.read_text(encoding="utf-8")


def build_document(title: str, source: str, content: str) -> dict:
    return {
        "title": title,
        "source": source,
        "content": content,
        "character_count": len(content),
    } 


def save_json(data: dict, output_path: str) -> None:
    path = Path(output_path)

    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


text = load_text("docs/article.txt")

document = build_document(
    title="RAG Introduction",
    source="docs/article.txt",
    content=text,
)

save_json(document, "docs/article.json")

print(document)
print("JSON 文件保存成功")