"""
词汇数据文件 - L5级法律金融（500词）
工号：092-100
级别：L5（法律金融）
"""

L5_VOCABULARY = [
    # ============ 法律（100词）============
    ("法律", "Pháp luật", "fǎ lǜ", "pháp luật", "法律/法规", "Pháp luật/法规", 5, "法律", "遵守法律", "Tuân thủ pháp luật"),
    ("法规", "Quy định", "fǎ guī", "quy định", "法规/规定", "Quy định/规定", 5, "法律", "政府法规", "Quy định chính phủ"),
    ("宪法", "Hiến pháp", "xiàn fǎ", "hiến pháp", "宪法", "Hiến pháp", 5, "法律", "国家宪法", "Hiến pháp quốc gia"),
    ("民法", "Dân sự", "mín fǎ", "dân sự", "民法/民事", "Dân sự/民事", 5, "法律", "民法规定", "Quy định dân sự"),
    ("刑法", "Hình sự", "xíng fǎ", "hình sự", "刑法/刑事", "Hình sự/刑事", 5, "法律", "刑法条款", "Điều khoản hình sự"),
    # ... 继续添加95个词汇
]

L5_VOCABULARY_COUNT = len(L5_VOCABULARY)
print(f"L5级法律金融词汇数量: {L5_VOCABULARY_COUNT}")
