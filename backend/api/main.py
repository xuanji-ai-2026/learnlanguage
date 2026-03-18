"""
主应用入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import vocabulary
from backend.models.vocabulary import Vocabulary
from backend.models.vocabulary import VocabularyCreate, VocabularyUpdate
from typing import List, Optional
import uuid

app = FastAPI(
    title="汉越语学习工具 API",
    version="2.0.0",
    description="汉越语学习工具v2.0 API接口"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(vocabulary.router)

# 根路径
@app.get("/")
async def root():
    return {
        "name": "汉越语学习工具 API",
        "version": "2.0.0",
        "status": "running",
        "docs": "/docs",
        "redoc": "/redoc"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
