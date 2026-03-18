#!/bin/bash
# 汉越语学习工具 - 启动脚本

echo "🚀 启动汉越语学习工具..."

# 启动后端
echo "📡 启动后端服务..."
cd /workspace/projects/workspace/han-yu-vietnamese-learning/backend
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "✅ 后端已启动 (PID: $BACKEND_PID)"
echo "🌐 API地址: http://localhost:8000"
echo "📚 API文档: http://localhost:8000/docs"

# 等待后端就绪
sleep 2

# 测试API
curl -s http://localhost:8000/health > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ API健康检查通过"
else
    echo "❌ API健康检查失败"
fi

echo ""
echo "🎉 启动完成！"
echo "   后端: http://localhost:8000"
echo "   前端: npm start (在 frontend 目录)"
