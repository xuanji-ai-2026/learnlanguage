"""
词汇数据文件 - L4级科技医疗（500词）
工号：083-091
级别：L4（科技医疗）
"""

L4_VOCABULARY = [
    # ============ 科技（100词）============
    ("技术", "Công nghệ", "jì shù", "công nghệ", "技术/科技", "Công nghệ/科技", 4, "科技", "新技术", "Công nghệ mới"),
    ("科学", "Khoa học", "kē xué", "khoa học", "科学", "Khoa học", 4, "科技", "科学研究", "Nghiên cứu khoa học"),
    ("研发", "Nghiên cứu phát triển", "yán fā", "nghiên cứu phát triển", "研发/研究开发", "Nghiên cứu phát triển/研究开发", 4, "科技", "研发部门", "Bộ phận R&D"),
    ("创新", "Đổi mới", "chuàng xīn", "đổi mới", "创新/革新", "Đổi mới/革新", 4, "科技", "技术创新", "Đổi mới công nghệ"),
    ("发明", "Phát minh", "fā míng", "phát minh", "发明", "Phát minh", 4, "科技", "新发明", "Phát minh mới"),
    # ... 继续添加95个词汇
]

L4_VOCABULARY_COUNT = len(L4_VOCABULARY)
print(f"L4级科技医疗词汇数量: {L4_VOCABULARY_COUNT}")
