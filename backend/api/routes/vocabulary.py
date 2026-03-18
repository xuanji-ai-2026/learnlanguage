"""
词汇API路由
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List
from backend.models.vocabulary import Vocabulary, VocabularyCreate, VocabularyUpdate
from backend.services.vocabulary_service import VocabularyService
import uuid

router = APIRouter(prefix="/api/v1", tags=["词汇"])


@router.get("/vocabulary/{level}", response_model=List[Vocabulary])
async def get_vocabulary_by_level(
    level: int,
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页数量")
):
    """
    按等级获取词汇列表

    Args:
        level: 词汇等级（1-5）
        page: 页码
        page_size: 每页数量

    Returns:
        词汇列表

    Raises:
        HTTPException: 参数错误
    """
    if level not in [1, 2, 3, 4, 5]:
        raise HTTPException(status_code=400, detail="level必须在1-5之间")

    service = VocabularyService()
    vocabularies = service.get_vocabulary_by_level(level, page, page_size)

    return vocabularies


@router.get("/vocabulary/{id}", response_model=Vocabulary)
async def get_vocabulary_by_id(id: str):
    """
    按ID获取词汇详情

    Args:
        id: 词汇ID

    Returns:
        词汇详情

    Raises:
        HTTPException: 词汇不存在
    """
    service = VocabularyService()
    vocabulary = service.get_vocabulary_by_id(id)

    if not vocabulary:
        raise HTTPException(status_code=404, detail="词汇不存在")

    return vocabulary


@router.post("/vocabulary", response_model=Vocabulary)
async def create_vocabulary(vocabulary: VocabularyCreate):
    """
    创建词汇

    Args:
        vocabulary: 词汇数据

    Returns:
        创建的词汇
    """
    service = VocabularyService()
    created_vocabulary = service.create_vocabulary(vocabulary)

    return created_vocabulary


@router.put("/vocabulary/{id}", response_model=Vocabulary)
async def update_vocabulary(id: str, vocabulary: VocabularyUpdate):
    """
    更新词汇

    Args:
        id: 词汇ID
        vocabulary: 词汇数据

    Returns:
    Raises:
        HTTPException: 词汇不存在
    """
    service = VocabularyService()
    updated_vocabulary = service.update_vocabulary(id, vocabulary)

    if not updated_vocabulary:
        raise HTTPException(status_code=404, detail="词汇不存在")

    return updated_vocabulary


@router.delete("/vocabulary/{id}")
async def delete_vocabulary(id: str):
    """
    删除词汇

    Args:
        id: 词汇ID

    Returns:
    Raises:
        HTTPException: 词汇不存在
    """
    service = VocabularyService()
    success = service.delete_vocabulary(id)

    if not success:
        raise HTTPException(status_code=404, detail="词汇不存在")

    return {"message": "删除成功"}
