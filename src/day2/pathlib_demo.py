from pathlib import Path


def load_text(file_path: str) -> str:
    """读取 UTF-8 文本文件并返回内容。"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"文件不存在：{path.resolve()}")

    if not path.is_file():
        raise ValueError(f"路径不是文件：{path.resolve()}")

    return path.read_text(encoding="utf-8")

text = load_text("docs/article.txt")
print(text)