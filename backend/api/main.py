"""
汉越语学习工具 - 后端 API
极简MVP版本 - 3天极速开发
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import sqlite3
import uuid

app = FastAPI(title="汉越语学习工具 API", version="0.1.0")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== 数据模型 ====================

class Vocabulary(BaseModel):
    word_zh: str
    word_vi: str
    pronunciation_zh: Optional[str] = None
    pronunciation_vi: Optional[str] = None
    meaning_zh: str
    meaning_vi: str
    level: int = 0
    image_url: Optional[str] = None

class User(BaseModel):
    username: str
    native_language: str = "zh"
    target_language: str = "vi"

class LearningProgress(BaseModel):
    vocabulary_id: str
    status: str = "learning"  # learning, mastered

# ==================== 数据库初始化 ====================

def init_db():
    conn = sqlite3.connect('hanyu_vi.db')
    cursor = conn.cursor()
    
    # 用户表
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
    
    # 词汇表
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
    
    # 学习进度表
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
    
    conn.commit()
    conn.close()

init_db()

# ==================== API 路由 ====================

@app.get("/")
def root():
    return {"message": "汉越语学习工具 API", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# ------------------- 词汇相关 -------------------

@app.get("/api/vocabulary")
def get_vocabulary(level: int = None, limit: int = 20):
    """获取词汇列表"""
    conn = sqlite3.connect('hanyu_vi.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if level is not None:
        cursor.execute("SELECT * FROM vocabulary WHERE level = ? LIMIT ?", (level, limit))
    else:
        cursor.execute("SELECT * FROM vocabulary LIMIT ?", (limit,))
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

@app.get("/api/vocabulary/{vocab_id}")
def get_vocabulary_detail(vocab_id: str):
    """获取词汇详情"""
    conn = sqlite3.connect('hanyu_vi.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vocabulary WHERE id = ?", (vocab_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="词汇不存在")
    return dict(row)

@app.post("/api/vocabulary")
def add_vocabulary(vocab: Vocabulary):
    """添加词汇"""
    conn = sqlite3.connect('hanyu_vi.db')
    cursor = conn.cursor()
    
    vocab_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    cursor.execute('''
        INSERT INTO vocabulary (id, word_zh, word_vi, pronunciation_zh, pronunciation_vi, meaning_zh, meaning_vi, level, image_url, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (vocab_id, vocab.word_zh, vocab.word_vi, vocab.pronunciation_zh, vocab.pronunciation_vi, vocab.meaning_zh, vocab.meaning_vi, vocab.level, vocab.image_url, now))
    
    conn.commit()
    conn.close()
    
    return {"id": vocab_id, "message": "添加成功"}

# ------------------- 用户相关 -------------------

@app.post("/api/users")
def create_user(user: User):
    """创建用户"""
    conn = sqlite3.connect('hanyu_vi.db')
    cursor = conn.cursor()
    
    user_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    try:
        cursor.execute('''
            INSERT INTO users (id, username, native_language, target_language, membership_level, created_at)
            VALUES (?, ?, ?, ?, 0, ?)
        ''', (user_id, user.username, user.native_language, user.target_language, now))
        conn.commit()
        conn.close()
        return {"id": user_id, "username": user.username}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="用户名已存在")

@app.get("/api/users/{user_id}")
def get_user(user_id: str):
    """获取用户信息"""
    conn = sqlite3.connect('hanyu_vi.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="用户不存在")
    return dict(row)

# ------------------- 学习进度 -------------------

@app.post("/api/progress")
def update_progress(user_id: str, progress: LearningProgress):
    """更新学习进度"""
    conn = sqlite3.connect('hanyu_vi.db')
    cursor = conn.cursor()
    
    progress_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    cursor.execute('''
        INSERT OR REPLACE INTO learning_progress (id, user_id, vocabulary_id, status, review_count, last_reviewed)
        VALUES (?, ?, ?, ?, 1, ?)
    ''', (progress_id, user_id, progress.vocabulary_id, progress.status, now))
    
    conn.commit()
    conn.close()
    
    return {"message": "进度已更新"}

@app.get("/api/progress/{user_id}")
def get_user_progress(user_id: str):
    """获取用户学习进度"""
    conn = sqlite3.connect('hanyu_vi.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM learning_progress WHERE user_id = ?", (user_id,))
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

# ------------------- 语音相关 -------------------

@app.get("/api/speech/voices")
def get_voices(language: str = "zh-CN"):
    """获取可用音色列表"""
    return {
        "voices": [
            {"name": "browser_default", "gender": "neutral", "language": language}
        ]
    }

@app.post("/api/speech/tts")
def text_to_speech(text: str, language: str = "zh-CN"):
    """
    文本转语音
    MVP版本返回JavaScript代码，前端执行
    """
    js_code = f'''
    (function() {{
        const utterance = new SpeechSynthesisUtterance("{text}");
        utterance.lang = "{language}";
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }})();
    '''
    return {"type": "javascript", "code": js_code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
