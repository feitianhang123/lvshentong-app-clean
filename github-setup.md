# 📱 GitHub 自动化构建指南 - 绿申通

## 🚀 快速开始

### 步骤一：创建GitHub仓库
1. 访问 https://github.com/new
2. 创建新仓库，名称如 `lvshentong-app`
3. 选择"Public"（公开仓库）
4. 勾选"Add a README file"

### 步骤二：上传文件到GitHub
1. 使用Git桌面客户端或网页上传以下文件：
   - `android-project/` 文件夹（整个Android项目）
   - `cordova-project/` 文件夹（Cordova项目）
   - `greenfood-app.zip`（在线构建包）
   - `.github/workflows/android-build.yml`（GitHub Actions配置）

### 步骤三：触发自动构建
1. 进入GitHub仓库
2. 点击"Actions"标签页
3. 选择"Android CI"工作流
4. 点击"Run workflow"运行构建

### 步骤四：下载APK
构建完成后：
1. 在"Actions"页面找到完成的构建
2. 点击构建记录
3. 在"Artifacts"部分下载APK文件

## ⚙️ GitHub Actions配置说明

### 自动触发条件：
- **push到main分支** - 自动构建
- **手动触发** - 点击Run workflow按钮

### 构建环境：
- **操作系统**: Ubuntu Latest
- **Java版本**: JDK 17
- **Android SDK**: 自动安装
- **构建工具**: Gradle

### 输出结果：
- `lvshentong-apk` - 生成的APK文件
- `build-output` - 构建日志和输出文件

## 📁 项目结构要求

```
仓库根目录/
├── android-project/          # Android Studio项目
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── assets/www/   # Web文件
│   │   │   ├── java/         # Java代码
│   │   │   └── res/          # 资源文件
│   │   └── build.gradle
│   └── build.gradle
├── cordova-project/          # Cordova项目
│   └── www/                 # Web文件
├── greenfood-app.zip         # 在线构建包
└── .github/workflows/        # GitHub Actions配置
    └── android-build.yml     # 构建工作流
```

## 🔧 故障排除

### 常见问题：
1. **构建失败**: 检查Android SDK版本兼容性
2. **权限问题**: 确保gradlew有执行权限
3. **依赖问题**: GitHub会自动处理依赖下载

### 解决方案：
1. 查看Actions日志详情
2. 调整Android SDK版本
3. 检查Gradle配置

## 🌐 替代方案

### 如果GitHub构建复杂：
1. **APKOnline**: https://www.apkonline.net/
   - 上传 `greenfood-app.zip`
   - 设置包名 `com.lvshentong.app`
   - 立即生成APK

2. **HBuilder备用**: 
   - 确保登录DCloud账号
   - 检查网络连接
   - 更新到最新版本

## 💡 优势

### GitHub构建的优势：
- ✅ 完全自动化，无需手动干预
- ✅ 免费使用GitHub的构建资源
- ✅ 版本控制，可追溯每次构建
- ✅ 支持持续集成和自动部署

### 在线服务的优势：
- ✅ 最简单，无需技术知识
- ✅ 最快获得APK文件
- ✅ 无需配置开发环境

---
**推荐优先尝试APKOnline，如果失败再使用GitHub Actions方案！**