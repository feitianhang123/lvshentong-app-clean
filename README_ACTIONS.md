# GitHub Actions 使用指南

## 🚀 自动化部署流程

本项目配置了两个GitHub Actions工作流：

### 1. 主部署工作流 (.github/workflows/deploy.yml)
- **触发条件**: push 到 master 分支或创建 pull request
- **功能**: 
  - 验证HTML和JavaScript语法
  - 创建部署包
  - 自动部署到GitHub Pages
  - 生成构建 artifacts

### 2. 测试工作流 (.github/workflows/test.yml)
- **触发条件**: push 到 master/develop 分支或创建 pull request
- **功能**:
  - 基础文件存在性检查
  - HTML结构验证
  - 部署就绪检查

## 📋 使用方法

### 首次设置
1. 确保仓库已启用GitHub Actions
2. 推送代码到master分支即可触发自动化流程

### 查看Actions状态
1. 访问仓库的 "Actions" 标签页
2. 查看工作流运行状态和日志

### 访问部署版本
- 部署成功后访问: `https://feitianhang123.github.io/lvshentong-app-clean/`
- 下载构建artifacts: 在Actions运行详情页面下载

## 🔧 自定义配置

### 修改部署设置
编辑 `.github/workflows/deploy.yml`:
- 调整Node.js版本
- 修改部署目录
- 添加自定义测试步骤

### 添加环境变量
在仓库 Settings → Secrets and variables → Actions 中添加:
- 部署密钥
- API令牌
- 其他敏感配置

## 📊 监控和调试

### 查看日志
- 每个工作流运行都有详细日志
- 失败时会显示具体错误信息

### 常见问题
1. **权限问题**: 确保GITHUB_TOKEN有足够权限
2. **文件路径**: 检查文件路径是否正确
3. **依赖问题**: 检查package.json配置

## 🎯 最佳实践

1. **分支策略**: 在feature分支开发，通过PR合并到master
2. **测试优先**: 在本地测试后再推送
3. **版本控制**: 保持commit信息清晰
4. **监控部署**: 定期检查Actions运行状态

## 📞 支持

如有问题，请:
1. 查看Actions运行日志
2. 检查文件路径和权限
3. 提交GitHub Issue