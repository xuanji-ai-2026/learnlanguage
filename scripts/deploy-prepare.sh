#!/bin/bash
# 部署准备脚本

echo "🚀 准备部署汉越语学习工具..."

# 检查后端
echo "📡 检查后端服务..."
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ 后端服务正常"
else
    echo "❌ 后端服务未运行"
    exit 1
fi

# 检查数据库
echo "📊 检查数据库..."
if [ -f "/workspace/projects/workspace/han-yu-vietnamese-learning/backend/hanyu_vi.db" ]; then
    VOCAB_COUNT=$(sqlite3 /workspace/projects/workspace/han-yu-vietnamese-learning/backend/hanyu_vi.db "SELECT COUNT(*) FROM vocabulary")
    echo "✅ 数据库正常，词汇数量: $VOCAB_COUNT"
else
    echo "❌ 数据库文件不存在"
    exit 1
fi

# 备份数据库
echo "💾 备份数据库..."
bash /workspace/projects/workspace/han-yu-vietnamese-learning/scripts/backup.sh

# 检查前端
echo "📱 检查前端代码..."
if [ -f "/workspace/projects/workspace/han-yu-vietnamese-learning/frontend/App.js" ]; then
    echo "✅ 前端代码存在"
else
    echo "❌ 前端代码不存在"
    exit 1
fi

# 生成部署包
echo "📦 生成部署包..."
cd /workspace/projects/workspace/han-yu-vietnamese-learning
tar -czf ../hanyu-vietnamese-learning-v0.1.tar.gz \
    --exclude='*.db' \
    --exclude='__pycache__' \
    --exclude='backups' \
    --exclude='node_modules' \
    .

echo "✅ 部署包已生成: hanyu-vietnamese-learning-v0.1.tar.gz"

echo ""
echo "🎉 部署准备完成！"
echo "📦 部署包: ../hanyu-vietnamese-learning-v0.1.tar.gz"
echo "🌐 API地址: http://localhost:8000"
echo "📚 API文档: http://localhost:8000/docs"
