# 一个函数，只负责清洗文本
def clean_text(text):
    return text.strip()


# 一个函数，只负责统计字符数
def count_characters(text):
    return len(text)


# 测试
document = "   Hello RAG!   "

cleaned = clean_text(document)

print(cleaned)

print(count_characters(cleaned))