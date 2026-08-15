from pathlib import Path

from src.rag_app.cleaner import clean_pdf_text
from src.rag_app.loader import load_pdf


pdf_path = Path(
    "docs/京东集团员工手册_2018.pdf"
)

raw_text = load_pdf(
    pdf_path
)

cleaned_text = clean_pdf_text(
    raw_text
)


keywords = [
    "9:00-18:00",
    "商务宴请",
]


for keyword in keywords:
    print()
    print("=" * 80)
    print(f"关键词: {keyword}")
    print("=" * 80)

    raw_index = raw_text.find(
        keyword
    )

    cleaned_index = cleaned_text.find(
        keyword
    )

    print("【清洗前】")
    print(
        raw_text[
            max(0, raw_index - 150):
            raw_index + 250
        ]
    )

    print()

    print("【清洗后】")
    print(
        cleaned_text[
            max(0, cleaned_index - 150):
            cleaned_index + 250
        ]
    )