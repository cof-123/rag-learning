from importlib.resources import path
from pathlib import Path
from pypdf import PdfReader

SUPPORTED_SUFFIXES = {
    ".txt",
    ".md",
    ".pdf",
}


class UnsupportedFileTypeError(Exception):
    """文件类型不受支持。"""


def load_text(file_path: str | Path) -> str:
    """读取一个 UTF-8 编码的 TXT 或 Markdown 文件。"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"文件不存在：{path.resolve()}")

    if not path.is_file():
        raise ValueError(f"路径不是文件：{path.resolve()}")

    if path.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise UnsupportedFileTypeError(
            f"不支持的文件类型：{path.suffix or '无扩展名'}"
        )
    if path.suffix.lower() == ".pdf":
        return load_pdf(path)
    
    return path.read_text(encoding="utf-8")



def find_documents(directory: str | Path) -> list[Path]:
    """递归查找目录中的 TXT 和 Markdown 文件。"""
    root = Path(directory)

    if not root.exists():
        raise FileNotFoundError(f"目录不存在：{root.resolve()}")

    if not root.is_dir():
        raise ValueError(f"路径不是目录：{root.resolve()}")

    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    )

def load_pdf(file_path: str | Path) -> str:
    """读取PDF文本。"""

    path = Path(file_path)

    reader = PdfReader(path)

    texts = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            texts.append(page_text)

    return "\n".join(texts)