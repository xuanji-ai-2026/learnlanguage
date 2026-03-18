"""
初始化数据库 - L0 核心词汇（100词）
"""
import sqlite3
import uuid
from datetime import datetime

# L0 核心词汇 - 日常生活最常用词汇
L0_VOCABULARY = [
    # 问候语
    ("你好", "Xin chào", "nǐ hǎo", "xin chào", "你好", "Xin chào", 0),
    ("再见", "Tạm biệt", "zài jiàn", "tạm biệt", "再见/告别", "Tạm biệt", 0),
    ("谢谢", "Cảm ơn", "xiè xie", "cảm ơn", "谢谢", "Cảm ơn", 0),
    ("不客气", "Không có gì", "bù kè qì", "không có gì", "不客气", "Không có gì", 0),
    ("对不起", "Xin lỗi", "duì bù qǐ", "xin lỗi", "对不起", "Xin lỗi", 0),
    ("没关系", "Không sao", "méi guān xi", "không sao", "没关系", "Không sao", 0),
    
    # 人称
    ("我", "Tôi", "wǒ", "tôi", "我", "Tôi", 0),
    ("你", "Bạn", "nǐ", "bạn", "你", "Bạn", 0),
    ("他", "Anh ấy", "tā", "anh ấy", "他", "Anh ấy", 0),
    ("她", "Cô ấy", "tā", "cô ấy", "她", "Cô ấy", 0),
    ("我们", "Chúng tôi", "wǒ men", "chúng tôi", "我们", "Chúng tôi", 0),
    ("你们", "Các bạn", "nǐ men", "các bạn", "你们", "Các bạn", 0),
    ("他们", "Họ", "tā men", "họ", "他们", "Họ", 0),
    
    # 是/否
    ("是", "Có", "shì", "có", "是", "Có", 0),
    ("不是", "Không", "bù shì", "không", "不是", "Không", 0),
    ("有", "Có", "yǒu", "có", "有", "Có", 0),
    ("没有", "Không có", "méi yǒu", "không có", "没有", "Không có", 0),
    
    # 数字 1-10
    ("一", "Một", "yī", "một", "一", "Một", 0),
    ("二", "Hai", "èr", "hai", "二", "Hai", 0),
    ("三", "Ba", "sān", "ba", "三", "Ba", 0),
    ("四", "Bốn", "sì", "bốn", "四", "Bốn", 0),
    ("五", "Năm", "wǔ", "năm", "五", "Năm", 0),
    ("六", "Sáu", "liù", "sáu", "六", "Sáu", 0),
    ("七", "Bảy", "qī", "bảy", "七", "Bảy", 0),
    ("八", "Tám", "bā", "tám", "八", "Tám", 0),
    ("九", "Chín", "jiǔ", "chín", "九", "Chín", 0),
    ("十", "Mười", "shí", "mười", "十", "Mười", 0),
    
    # 时间
    ("今天", "Hôm nay", "jīn tiān", "hôm nay", "今天", "Hôm nay", 0),
    ("明天", "Ngày mai", "míng tiān", "ngày mai", "明天", "Ngày mai", 0),
    ("昨天", "Hôm qua", "zuó tiān", "hôm qua", "昨天", "Hôm qua", 0),
    ("现在", "Bây giờ", "xiàn zài", "bây giờ", "现在", "Bây giờ", 0),
    ("什么时候", "Khi nào", "shén me shí hòu", "khi nào", "什么时候", "Khi nào", 0),
    
    # 星期
    ("星期一", "Thứ hai", "xīng qī yī", "thứ hai", "星期一", "Thứ hai", 0),
    ("星期二", "Thứ ba", "xīng qī èr", "thứ ba", "星期二", "Thứ ba", 0),
    ("星期三", "Thứ tư", "xīng qī sān", "thứ tư", "星期三", "Thứ tư", 0),
    ("星期四", "Thứ năm", "xīng qī sì", "thứ năm", "星期四", "Thứ năm", 0),
    ("星期五", "Thứ sáu", "xīng qī wǔ", "thứ sáu", "星期五", "Thứ sáu", 0),
    ("星期六", "Thứ bảy", "xīng qī liù", "thứ bảy", "星期六", "Thứ bảy", 0),
    ("星期日", "Chủ nhật", "xīng qī tiān", "chủ nhật", "星期日/周日", "Chủ nhật", 0),
    
    # 家庭
    ("爸爸", "Bố", "bà ba", "bố", "爸爸", "Bố", 0),
    ("妈妈", "Mẹ", "mā ma", "mẹ", "妈妈", "Mẹ", 0),
    ("哥哥", "Anh trai", "gē gē", "anh trai", "哥哥", "Anh trai", 0),
    ("姐姐", "Chị gái", "jiě jie", "chị gái", "姐姐", "Chị gái", 0),
    ("弟弟", "Em trai", "dì dì", "em trai", "弟弟", "Em trai", 0),
    ("妹妹", "Em gái", "mèi mèi", "em gái", "妹妹", "Em gái", 0),
    ("儿子", "Con trai", "ér zi", "con trai", "儿子", "Con trai", 0),
    ("女儿", "Con gái", "nǚ ér", "con gái", "女儿", "Con gái", 0),
    ("丈夫", "Chồng", "zhàng fu", "chồng", "丈夫", "Chồng", 0),
    ("妻子", "Vợ", "qī zi", "vợ", "妻子", "Vợ", 0),
    
    # 食物
    ("米饭", "Cơm", "mǐ fàn", "cơm", "米饭", "Cơm", 0),
    ("面条", "Mì", "miàn tiáo", "mì", "面条", "Mì", 0),
    ("水", "Nước", "shuǐ", "nước", "水", "Nước", 0),
    ("茶", "Trà", "chá", "trà", "茶", "Trà", 0),
    ("咖啡", "Cà phê", "kā fēi", "cà phê", "咖啡", "Cà phê", 0),
    ("吃", "Ăn", "chī", "ăn", "吃", "Ăn", 0),
    ("喝", "Uống", "hē", "uống", "喝", "Uống", 0),
    
    # 常见形容词
    ("大", "Lớn", "dà", "lớn", "大", "Lớn", 0),
    ("小", "Nhỏ", "xiǎo", "nhỏ", "小", "Nhỏ", 0),
    ("新", "Mới", "xīn", "mới", "新", "Mới", 0),
    ("旧", "Cũ", "jiù", "cũ", "旧", "Cũ", 0),
    ("好", "Tốt", "hǎo", "tốt", "好", "Tốt", 0),
    ("坏", "Xấu", "huài", "xấu", "坏", "Xấu", 0),
    ("多", "Nhiều", "duō", "nhiều", "多", "Nhiều", 0),
    ("少", "Ít", "shǎo", "ít", "少", "Ít", 0),
    ("快", "Nhanh", "kuài", "nhanh", "快/迅速", "Nhanh", 0),
    ("慢", "Chậm", "màn", "chậm", "慢", "Chậm", 0),
    ("热", "Nóng", "rè", "nóng", "热", "Nóng", 0),
    ("冷", "Lạnh", "lěng", "lạnh", "冷", "Lạnh", 0),
    
    # 常见动词
    ("来", "Đến", "lái", "đến", "来", "Đến", 0),
    ("去", "Đi", "qù", "đi", "去", "Đi", 0),
    ("看", "Nhìn", "kàn", "nhìn", "看", "Nhìn", 0),
    ("听", "Nghe", "tīng", "nghe", "听", "Nghe", 0),
    ("说", "Nói", "shuō", "nói", "说", "Nói", 0),
    ("写", "Viết", "xiě", "viết", "写", "Viết", 0),
    ("读", "Đọc", "dú", "đọc", "读", "Đọc", 0),
    ("做", "Làm", "zuò", "làm", "做/干", "Làm", 0),
    ("给", "Cho", "gěi", "cho", "给", "Cho", 0),
    ("买", "Mua", "mǎi", "mua", "买", "Mua", 0),
    ("卖", "Bán", "mài", "bán", "卖", "Bán", 0),
    ("喜欢", "Thích", "xǐ huan", "thích", "喜欢", "Thích", 0),
    ("要", "Cần", "yào", "cần", "要/需要", "Cần", 0),
    ("知道", "Biết", "zhī dào", "biết", "知道", "Biết", 0),
    ("不懂", "Không hiểu", "bù dǒng", "không hiểu", "不懂", "Không hiểu", 0),
    
    # 地点
    ("家", "Nhà", "jiā", "nhà", "家/房子", "Nhà", 0),
    ("学校", "Trường học", "xué xiào", "trường học", "学校", "Trường học", 0),
    ("医院", "Bệnh viện", "yī yuàn", "bệnh viện", "医院", "Bệnh viện", 0),
    ("商店", "Cửa hàng", "shāng diàn", "cửa hàng", "商店", "Cửa hàng", 0),
    ("银行", "Ngân hàng", "yín háng", "ngân hàng", "银行", "Ngân hàng", 0),
    ("车站", "Ga xe", "chē zhàn", "ga xe", "车站", "Ga xe", 0),
    ("机场", "Sân bay", "jī chǎng", "sân bay", "机场", "Sân bay", 0),
    
    # 其他常用词
    ("钱", "Tiền", "qián", "tiền", "钱", "Tiền", 0),
    ("电话", "Điện thoại", "diàn huà", "điện thoại", "电话", "Điện thoại", 0),
    ("名字", "Tên", "míng zì", "tên", "名字", "Tên", 0),
    ("时间", "Thời gian", "shí jiān", "thời gian", "时间", "Thời gian", 0),
    ("年", "Năm", "nián", "năm", "年", "Năm", 0),
    ("月", "Tháng", "yuè", "tháng", "月", "Tháng", 0),
    ("日", "Ngày", "rì", "ngày", "日/天", "Ngày", 0),
    ("电脑", "Máy tính", "diàn nǎo", "máy tính", "电脑", "Máy tính", 0),
    ("手机", "Điện thoại", "shǒu jī", "điện thoại", "手机", "Điện thoại", 0),
    ("工作", "Công việc", "gōng zuò", "công việc", "工作", "Công việc", 0),
    ("学习", "Học tập", "xué xí", "học tập", "学习", "Học tập", 0),
]

def init_database():
    conn = sqlite3.connect('hanyu_vi.db')
    cursor = conn.cursor()
    
    # 创建表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            native_language TEXT,
            target_language TEXT,
            membership_level INTEGER DEFAULT 0,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id TEXT PRIMARY KEY,
            word_zh TEXT NOT NULL,
            word_vi TEXT NOT NULL,
            pronunciation_zh TEXT,
            pronunciation_vi TEXT,
            meaning_zh TEXT,
            meaning_vi TEXT,
            level INTEGER DEFAULT 0,
            image_url TEXT,
            created_at TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learning_progress (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            vocabulary_id TEXT,
            status TEXT DEFAULT 'learning',
            review_count INTEGER DEFAULT 0,
            last_reviewed TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (vocabulary_id) REFERENCES vocabulary(id)
        )
    ''')
    
    # 检查是否已有数据
    cursor.execute("SELECT COUNT(*) FROM vocabulary WHERE level = 0")
    count = cursor.fetchone()[0]
    
    if count == 0:
        now = datetime.now().isoformat()
        print(f"正在插入 {len(L0_VOCABULARY)} 个L0词汇...")
        
        for vocab in L0_VOCABULARY:
            vocab_id = str(uuid.uuid4())
            cursor.execute('''
                INSERT INTO vocabulary (id, word_zh, word_vi, pronunciation_zh, pronunciation_vi, meaning_zh, meaning_vi, level, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (vocab_id, *vocab, now))
        
        conn.commit()
        print(f"✅ 成功插入 {len(L0_VOCABULARY)} 个词汇！")
    else:
        print(f"数据库中已有 {count} 个L0词汇")
    
    conn.close()

if __name__ == "__main__":
    init_database()
