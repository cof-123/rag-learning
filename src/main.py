from loader import load_text

from cleaner import clean_text

text = load_text("docs/article.txt")

text = clean_text(text)

print(text)