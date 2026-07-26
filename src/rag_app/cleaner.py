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