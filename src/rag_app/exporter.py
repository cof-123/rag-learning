import json
from pathlib import Path


def save_documents_as_json(
    documents: list[dict],
    output_path: str | Path,
) -> None:
    """把文档列表保存为 UTF-8 JSON 文件。"""
    path = Path(output_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(
            documents,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )