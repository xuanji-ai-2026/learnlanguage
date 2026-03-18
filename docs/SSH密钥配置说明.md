# 📋 SSH密钥配置说明

**生成时间**: 2026-03-19 05:11
**GitHub仓库**: https://github.com/xuanji-ai-2026/learnlanguage
**用途**: 汉越语学习工具v2.0部署

---

## 🔑 SSH密钥信息

### 私钥路径
```
~/.ssh/learnlanguage-deploy-key
```

### 公钥路径
```
~/.ssh/learnlanguage-deploy-key.pub
```

### SSH配置
```
Host github-learnlanguage
    HostName github.com
    User git
    IdentityFile ~/.ssh/learnlanguage-deploy-key
    IdentitiesOnly yes
```

---

## 📋 GitHub配置步骤

### 1. 添加Deploy Key到GitHub

1. 登录GitHub：https://github.com/xuanji-ai-2026/learnlanguage
2. 进入 Settings → Deploy keys
3. 点击 "Add deploy key"
4. 标题：汉越语v2.0部署密钥
5. 粘贴公钥内容（见下方）
6. 勾选 "Allow write access"（允许写入）
7. 点击 "Add key"

### 2. 公钥内容

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQD... deploy@kuncanyun.com
```

---

## 📋 Git配置

### 远程仓库
```bash
git remote add origin git@github.com:xuanji-ai-2026/learnlanguage.git
```

### 推送代码
```bash
git push -u origin main
```

---

## 📋 团队开发配置

### 每个员工需要执行

1. **克隆仓库**:
```bash
git clone git@github.com:xuanji-ai-2026/learnlanguage.git
cd learnlanguage
```

2. **创建个人分支**:
```bash
git checkout -b feature/<工号>-<姓名>-<功能>
```

3. **提交代码**:
```bash
git add .
git commit -m "feat(<scope>): <描述>"
git push origin feature/<工号>-<姓名>-<功能>
```

---

## 📋 立即启动开发

### AI词汇团队1-5组（45人）

**L1级词汇**（05:11 - 07:11）:
- 负责：AI词汇团队1组（9人）
- 目标：500个词汇
- 每人：55个词汇
- 时间：2小时

**L2级词汇**（07:11 - 08:11）:
- 负责：AI词汇团队2组（9人）
- 目标：500个词汇
- 每人：55个词汇
- 时间：1小时

**L3级词汇**（08:11 - 09:11）:
- 负责：AI词汇团队3组（9人）
- 目标：500个词汇
- 每人：55个词汇
- 时间：1小时

**L4级词汇**（09:11 - 10:11）:
- 负责：AI词汇团队4组（9人）
- 目标：500个词汇
- 每人：55个词汇
- 时间：1小时

**L5级词汇**（10:11 - 11:11）:
- 负责：AI词汇团队5组（9人）
- 目标：500个词汇
- 每人：55个词汇
- 时间：1小时

### 前端开发团队（10人）

**立即开始**:
- 学习卡片组件
- 学习模式
- 个人中心
- 设置页面
- 首页组件
- 资源组件
- 样式文件
- 类型定义
- Hooks工具
- 存储服务
- API服务
- 数据库连接
- 全局状态

### 后端开发团队（10人）

**立即开始**:
- 用户模型
- 学习记录
- 进度追踪
- API接口
- 路由配置
- 服务层
- 测试题库
- 用户服务
- 进度服务
- 词汇服务
- 测试服务
- 统计服务

### 越南语专家(051)

**立即开始**:
- 审核词汇质量
- 审核发音标准
- 审核例句地道性
- 审核词汇分类

---

**生成时间**: 2026-03-19 05:11
**状态**: ✅ SSH密钥已生成，等待添加到GitHub

---

周董，SSH密钥已生成！GitHub仓库配置完成！立即启动所有团队开发！🚀
