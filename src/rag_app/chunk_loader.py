import json
from pathlib import Path

from .models import Chunk


def load_chunks_from_json(
    input_path: str | Path,
) -> list[Chunk]:
    """从 JSON 文件恢复 Chunk 列表。"""

    path = Path(input_path)

    data = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    chunks = [
        Chunk(
            content=item["content"],
            chunk_id=item["chunk_id"],
            source=item["source"],
        )
        for item in data
    ]

    return chunks