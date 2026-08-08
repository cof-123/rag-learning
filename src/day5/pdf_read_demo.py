from pathlib import Path

from pypdf import PdfReader


pdf_path = Path("docs/sample.pdf")


reader = PdfReader(pdf_path)


print("页数:", len(reader.pages))


for index, page in enumerate(reader.pages):
    text = page.extract_text()

    print()
    print("第", index + 1, "页")
    print(text[:200])