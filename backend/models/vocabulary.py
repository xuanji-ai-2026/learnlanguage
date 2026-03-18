"""
词汇数据模型
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VocabularyBase(BaseModel):
    """词汇基础模型"""
    word_zh: str = Field(..., description="中文词汇")
    word_vi: str = Field(..., description="越南语词汇")
    pronunciation_zh: str = Field(..., description="中文拼音")
    pronunciation_vi: str = Field(..., description="越南语发音")
    meaning_zh: str = Field(..., description="中文释义")
    meaning_vi: str = Field(..., description="越南语释义")
    level: int = Field(..., ge=1, le=5, description="词汇等级（1-5）")
    category: str = Field(..., description="词汇分类")
    example_zh: str = Field(..., description="中文例句")
    example_vi: str = Field(..., description="越南语例句")
    image_url: Optional[str] = Field(None, description="图片URL")


class Vocabulary(VocabularyBase):
    """词汇完整模型"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="词汇ID")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "uuid",
                "word_zh": "你好",
                "word_vi": "Xin chào",
                "pronunciation_zh": "nǐ hǎo",
                "pronunciation_vi": "xin chào",
                "meaning_zh": "你好/问候",
                "meaning_vi": "Xin chào/问候",
                "level": 1,
                "category": "问候语",
                "example_zh": "你好，我是小李",
                "example_vi": "Xin chào, tôi là Tiểu Lý",
                "image_url": None
            }
        }


class VocabularyCreate(VocabularyBase):
    """创建词汇模型"""
    pass


class VocabularyUpdate(BaseModel):
    """更新词汇模型"""
    word_zh: Optional[str] = None
    word_vi: Optional[str] = None
    pronunciation_zh: Optional[str] = None
    pronunciation_vi: Optional[str] = None
    meaning_zh: Optional[str] = None
    meaning_vi: Optional[str] = None
    level: Optional[int] = None
    category: Optional[str] = None
    example_zh: Optional[str] = None
    example_vi: Optional[str] = None
    image_url: Optional[str] = None
