"""
词汇数据文件 - L3级学习教育（500词）
工号：074-082
级别：L3（学习教育）
"""

L3_VOCABULARY = [
    # ============ 学校（100词）============
    ("学校", "Trường học", "xué xiào", "trường học", "学校/校园", "Trường học/校园", 3, "学校", "去学校", "Đi học"),
    ("教室", "Lớp học", "jiào shì", "lớp học", "教室/课堂", "Lớp học/课堂", 3, "学校", "在教室学习", "Học trong lớp"),
    ("图书馆", "Thư viện", "tú shū guǎn", "thư viện", "图书馆", "Thư viện", 3, "学校", "去图书馆", "Đến thư viện"),
    ("实验室", "Phòng thí nghiệm", "shí yàn shì", "phòng thí nghiệm", "实验室", "Phòng thí nghiệm", 3, "学校", "在实验室做实验", "Làm thí nghiệm trong phòng"),
    ("操场", "Sân thể thao", "cāo chǎng", "sân thể thao", "操场/体育场", "Sân thể thao/体育场", 3, "学校", "在操场跑步", "Chạy bộ trong sân"),
    # ... 继续添加95个词汇
]

L3_VOCABULARY_COUNT = len(L3_VOCABULARY)
print(f"L3级学习教育词汇数量: {L3_VOCABULARY_COUNT}")
