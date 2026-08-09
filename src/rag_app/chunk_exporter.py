import json
from pathlib import Path

from .models import Chunk


def save_chunks_as_json(
    chunks: list[Chunk],
    output_path: str | Path,
) -> None:

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    data = [
        {
            "content": chunk.content,
            "chunk_id": chunk.chunk_id,
            "source": chunk.source,
        }
        for chunk in chunks
    ]

    path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )