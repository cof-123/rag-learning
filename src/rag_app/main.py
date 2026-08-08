from pathlib import Path

from .cleaner import clean_text
from .exporter import save_documents_as_json
from .loader import find_documents, load_text
from .models import Document
from dataclasses import asdict


def build_document(file_path: Path) -> dict:
    """读取、清洗并构造统一文档结构。"""
    raw_text = load_text(file_path)
    cleaned_text = clean_text(raw_text)

    return Document(
        title=file_path.stem,
        source=file_path.as_posix(),
        file_type=file_path.suffix.lower(),
        content=cleaned_text,
        character_count=len(cleaned_text),
    )

class UnsupportedFileTypeError(ValueError):
    """文件类型不受支持。"""

def main() -> None:
    source_directory = Path("docs")
    output_path = Path("output/documents.json")

    file_paths = find_documents(source_directory)

    documents: list[dict] = []
    failed_files: list[dict] = []

    for file_path in file_paths:
        try:
            document = build_document(file_path)
            documents.append(document)
            print(f"[成功] {file_path}")

        except (OSError, UnicodeError, ValueError) as error:
            failed_files.append(
                {
                    "source": file_path.as_posix(),
                    "error": str(error),
                }
            )
            print(f"[失败] {file_path}：{error}")

    json_documents = [
    asdict(document)
    for document in documents
    ]

    save_documents_as_json(
    json_documents,
    output_path,
    )

    print()
    print(f"成功处理：{len(documents)} 个文件")
    print(f"处理失败：{len(failed_files)} 个文件")
    print(f"输出位置：{output_path}")


if __name__ == "__main__":
    main()