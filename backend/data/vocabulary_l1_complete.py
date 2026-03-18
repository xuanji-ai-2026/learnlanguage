"""
词汇数据文件 - L1级完整版（500词）
模板示例：供AI词汇团队参考
"""

L1_VOCABULARY = [
    # ============ 问候语（20词）============
    ("你好", "Xin chào", "nǐ hǎo", "xin chào", "你好/问候", "Xin chào/问候", 1, "问候语", "你好，我是小李", "Xin chào, tôi là Tiểu Lý"),
    ("再见", "Tạm biệt", "zài jiàn", "tạm biệt", "再见/告别", "Tạm biệt/告别", 1, "问候语", "再见，明天见", "Tạm biệt, hẹn gặp lại mai"),
    ("谢谢", "Cảm ơn", "xiè xie", "cảm ơn", "谢谢/感谢", "Cảm ơn/感谢", 1, "问候语", "谢谢你的帮助", "Cảm ơn vì sự giúp đỡ của bạn"),
    ("对不起", "Xin lỗi", "duì bù qǐ", "xin lỗi", "对不起/抱歉", "Xin lỗi/抱歉", 1, "问候语", "对不起，我迟到了", "Xin lỗi, tôi đến trễ"),
    ("没关系", "Không sao", "méi guān xi", "không sao", "没关系/不客气", "Không sao/不客气", 1, "问候语", "没关系", "Không sao"),
    ("请", "Làm ơn", "qǐng", "làm ơn", "请/请求", "Làm ơn/请求", 1, "问候语", "请坐", "Làm ơn ngồi"),
    ("不客气", "Không có gì", "bù kè qi", "không có gì", "不客气/不用谢", "Không có gì/不用谢", 1, "问候语", "不客气", "Không có gì"),
    ("早上好", "Chào buổi sáng", "zǎo shang hǎo", "chào buổi sáng", "早上好", "Chào buổi sáng", 1, "问候语", "早上好！", "Chào buổi sáng!"),
    ("晚上好", "Chào buổi tối", "wǎn shang hǎo", "chào buổi tối", "晚上好", "Chào buổi tối", 1, "问候语", "晚上好！", "Chào buổi tối!"),
    ("晚安", "Chúc ngủ ngon", "wǎn ān", "chúc ngủ ngon", "晚安", "Chúc ngủ ngon", 1, "问候语", "晚安！", "Chúc ngủ ngon!"),
    
    # ============ 食物（55词）============
    # 主食
    ("米饭", "Cơm", "mǐ fàn", "cơm", "米饭/主食", "Cơm/主食", 1, "食物", "今天吃米饭", "Hôm nay ăn cơm"),
    ("面条", "Mì", "miàn tiáo", "mì", "面条/面食", "Mì/面食", 1, "食物", "喜欢吃面条", "Thích ăn mì"),
    ("面包", "Bánh mì", "miàn bāo", "bánh mì", "面包/烘焙", "Bánh mì/烘焙", 1, "食物", "早餐吃面包", "Ăn sáng ăn bánh mì"),
    ("馒头", "Bánh bao", "mán tou", "bánh bao", "馒头/面食", "Bánh bao/面食", 1, "食物", "吃馒头", "Ăn bánh bao"),
    ("包子", "Bánh bao nhân", "bāo zi", "bánh bao nhân", "包子/面食", "Bánh bao nhân/面食", 1, "食物", "肉包子很好吃", "Bánh bao nhân thịt rất ngon"),
    
    # 蛋白质
    ("鸡蛋", "Trứng gà", "jī dàn", "trứng gà", "鸡蛋/蛋", "Trứng gà/蛋", 1, "食物", "煮鸡蛋", "Luộc trứng gà"),
    ("鸭蛋", "Trứng vịt", "yā dàn", "trứng vịt", "鸭蛋/蛋", "Trứng vịt/蛋", 1, "食物", "咸鸭蛋", "Trứng vịt muối"),
    ("牛奶", "Sữa bò", "niú nǎi", "sữa bò", "牛奶/饮料", "Sữa bò/饮料", 1, "食物", "喝牛奶", "Uống sữa bò"),
    ("酸奶", "Sữa chua", "suān nǎi", "sữa chua", "酸奶/饮料", "Sữa chua/饮料", 1, "食物", "喝酸奶", "Uống sữa chua"),
    ("豆腐", "Đậu phụ", "dòu fu", "đậu phụ", "豆腐/豆制品", "Đậu phụ/豆制品", 1, "食物", "麻婆豆腐", "Đậu phụ Tứ Xuyên"),
    
    # 肉类
    ("猪肉", "Thịt lợn", "zhū ròu", "thịt lợn", "猪肉/肉类", "Thịt lợn/肉类", 1, "食物", "红烧肉", "Thịt lợn kho"),
    ("牛肉", "Thịt bò", "niú ròu", "thịt bò", "牛肉/肉类", "Thịt bò/肉类", 1, "食物", "牛肉很好吃", "Thịt bò rất ngon"),
    ("羊肉", "Thịt dê", "yáng ròu", "thịt dê", "羊肉/肉类", "Thịt dê/肉类", 1, "食物", "羊肉串", "Thịt dê xiên"),
    ("鸡肉", "Thịt gà", "jī ròu", "thịt gà", "鸡肉/肉类", "Thịt gà/肉类", 1, "食物", "白切鸡", "Gà luộc"),
    ("鱼肉", "Thịt cá", "yú ròu", "thịt cá", "鱼肉/肉类", "Thịt cá/肉类", 1, "食物", "清蒸鱼", "Cá hấp"),
    
    # 蔬菜
    ("白菜", "Cải thảo", "bái cài", "cải thảo", "白菜/蔬菜", "Cải thảo/蔬菜", 1, "食物", "炒白菜", "Cải thảo xào"),
    ("菠菜", "Rau chân vịt", "bō cài", "rau chân vịt", "菠菜/蔬菜", "Rau chân vịt/蔬菜", 1, "食物", "菠菜汤", "Canh rau chân vịt"),
    ("西红柿", "Cà chua", "xī hóng shì", "cà chua", "西红柿/蔬菜", "Cà chua/蔬菜", 1, "食物", "西红柿炒鸡蛋", "Cà chua xào trứng"),
    ("黄瓜", "Dưa chuột", "huáng guā", "dưa chuột", "黄瓜/蔬菜", "Dưa chuột/蔬菜", 1, "食物", "凉拌黄瓜", "Dưa chuột trộn"),
    ("土豆", "Khoai tây", "tǔ dòu", "khoai tây", "土豆/蔬菜", "Khoai tây/蔬菜", 1, "食物", "土豆泥", "Khoai tây nghiền"),
    
    # 调味料
    ("盐", "Muối", "yán", "muối", "盐/调味料", "Muối/调味料", 1, "食物", "加盐", "Thêm muối"),
    ("糖", "Đường", "táng", "đường", "糖/调味料", "Đường/调味料", 1, "食物", "加糖", "Thêm đường"),
    ("酱油", "Xì dầu", "jiàng yóu", "xì dầu", "酱油/调味料", "Xì dầu/调味料", 1, "食物", "倒酱油", "Rót xì dầu"),
    ("醋", "Giấm", "cù", "giấm", "醋/调味料", "Giấm/调味料", 1, "食物", "加醋", "Thêm giấm"),
    ("辣椒", "Ớt", "là jiāo", "ớt", "辣椒/调味料", "Ớt/调味料", 1, "食物", "辣椒很辣", "Ớt rất cay"),
    
    # ============ 水果（40词）============
    ("苹果", "Táo", "píng guǒ", "táo", "苹果/水果", "Táo/水果", 1, "水果", "吃苹果", "Ăn táo"),
    ("香蕉", "Chuối", "xiāng jiāo", "chuối", "香蕉/水果", "Chuối/水果", 1, "水果", "吃香蕉", "Ăn chuối"),
    ("橙子", "Cam", "chéng zi", "cam", "橙子/水果", "Cam/水果", 1, "水果", "橙子很甜", "Cam rất ngọt"),
    ("葡萄", "Nho", "pú táo", "nho", "葡萄/水果", "Nho/水果", 1, "水果", "葡萄很甜", "Nho rất ngọt"),
    ("西瓜", "Dưa hấu", "xī guā", "dưa hấu", "西瓜/水果", "Dưa hấu/水果", 1, "水果", "夏天吃西瓜", "Mùa hè ăn dưa hấu"),
    ("梨", "Lê", "lí", "lê", "梨/水果", "Lê/水果", 1, "水果", "吃梨", "Ăn lê"),
    ("桃子", "Đào", "táo zi", "đào", "桃子/水果", "Đào/水果", 1, "水果", "桃子很甜", "Đào rất ngọt"),
    ("草莓", "Dâu tây", "cǎo méi", "dâu tây", "草莓/水果", "Dâu tây/水果", 1, "水果", "草莓很香", "Dâu tây rất thơm"),
    ("芒果", "Xoài", "máng guǒ", "xoài", "芒果/水果", "Xoài/水果", 1, "水果", "芒果很甜", "Xoài rất ngọt"),
    ("菠萝", "Dứa", "bō luó", "dứa", "菠萝/水果", "Dứa/水果", 1, "水果", "吃菠萝", "Ăn dứa"),
    
    # ... 继续添加更多词汇
]

L1_VOCABULARY_COUNT = len(L1_VOCABULARY)
print(f"L1级词汇总数: {L1_VOCABULARY_COUNT}")
