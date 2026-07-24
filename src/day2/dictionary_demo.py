# 用一个字典表示一篇文档
document = {
    "title": "RAG Introduction",
    "author": "Xu Yi",
    "pages": 12,
    "language": "English"
}

# 1. 打印整个字典
print(document)

# 2. 打印标题
print(document["title"])

# 3. 修改页数
document["pages"] = 15

# 4. 增加一个字段
document["year"] = 2026

# 5. 遍历所有键和值
for key, value in document.items():
    print(f"{key}: {value}")