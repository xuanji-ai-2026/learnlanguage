#!/bin/bash
# 数据库备份脚本

BACKUP_DIR="/workspace/projects/workspace/han-yu-vietnamese-learning/backups"
DB_FILE="/workspace/projects/workspace/han-yu-vietnamese-learning/backend/hanyu_vi.db"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 备份数据库
cp "$DB_FILE" "$BACKUP_DIR/hanyu_vi_backup_$TIMESTAMP.db"

echo "✅ 数据库已备份: hanyu_vi_backup_$TIMESTAMP.db"

# 保留最近7天的备份
find "$BACKUP_DIR" -name "hanyu_vi_backup_*.db" -mtime +7 -delete

echo "📁 当前备份文件:"
ls -lh "$BACKUP_DIR"
