import re

def is_structure_line(line: str) -> bool:
    """判断一行是否属于标题、章节或条款结构。"""

    patterns = [
        r"^第[一二三四五六七八九十]+章",
        r"^第[一二三四五六七八九十]+节",
        r"^\d+\.\s",
        r"^\d+\.\d+\s",
        r"^\d+\.\d+\.\d+\s",
    ]

    return any(
        re.match(pattern, line)
        for pattern in patterns
    )

def clean_text(text: str) -> str:
    """清除首尾空白，并将连续空行压缩为一个空行。"""
    lines = text.strip().splitlines()

    cleaned_lines: list[str] = []
    previous_line_was_blank = False

    for line in lines:
        normalized_line = line.strip()
        current_line_is_blank = normalized_line == ""

        if current_line_is_blank and previous_line_was_blank:
            continue

        cleaned_lines.append(normalized_line)
        previous_line_was_blank = current_line_is_blank

    return "\n".join(cleaned_lines)



def clean_pdf_text(text: str) -> str:
    lines = [
        line.strip()
        for line in text.splitlines()
    ]

    lines = [
        line
        for line in lines
        if line
        and line != "京"
        and line != "京东集团员工手册"
        and not line.isdigit()
    ]

    cleaned_lines: list[str] = []

    for line in lines:
        if not cleaned_lines:
            cleaned_lines.append(line)
            continue

        previous = cleaned_lines[-1]

        if is_structure_line(line):
            cleaned_lines.append(line)
        elif is_structure_line(previous):
            cleaned_lines.append(line)
        else:
            cleaned_lines[-1] = previous + line

    return "\n".join(cleaned_lines)

