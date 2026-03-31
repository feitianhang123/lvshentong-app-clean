# 📱 Cordova 构建指南 - 绿申通

## 🎯 本地构建方案（国内友好）

### 方法一：使用 HBuilder（推荐）
HBuilder 是国内最流行的 Web 应用打包工具，对国内网络优化良好。

**步骤：**
1. 下载 HBuilder: https://www.dcloud.io/hbuilderx.html
2. 打开 `cordova-project` 文件夹
3. 点击"发行" → "原生App-云打包"
4. 设置：
   - 应用名称：绿申通
   - 包名：com.lvshentong.app
   - 选择 Android 平台
5. 使用自有证书或测试证书
6. 开始打包

### 方法二：使用 APKOnline
**网址**: https://www.apkonline.net/
**特点**: 国内访问相对稳定，支持中文

### 方法三：本地 Cordova 环境
```bash
# 1. 安装 Node.js (https://nodejs.org/zh-cn/)
# 2. 安装 Cordova
npm install -g cordova

# 3. 进入项目目录
cd cordova-project

# 4. 安装依赖
npm install

# 5. 添加 Android 平台
cordova platform add android

# 6. 构建 APK
cordova build android

# 生成的 APK 位置:
# cordova-project/platforms/android/app/build/outputs/apk/
```

## 📦 项目结构
```
cordova-project/
├── www/                 # Web文件
│   ├── index.html              # 主页
│   ├── module1_fixed_final_v4.html    # 模块一
│   ├── module2_current_standards.html # 模块二
│   ├── module3_final.html      # 模块三
│   └── standards_data.js       # 数据文件
├── config.xml           # 应用配置
├── package.json         # 项目配置
└── cordova-build-guide.md    # 构建指南
```

## ⚙️ 应用配置
- **应用ID**: com.lvshentong.app
- **应用名称**: 绿申通
- **版本**: 1.0.0
- **入口页面**: index.html

## 🚀 快速开始

### 使用 HBuilder（最简单）：
1. 下载 HBuilderX
2. 打开 `cordova-project` 文件夹
3. 云打包 → 设置应用信息 → 开始打包

### 使用 APKOnline：
1. 访问 https://www.apkonline.net/
2. 上传 `cordova-project/www` 文件夹内容
3. 设置包名和应用名称
4. 生成 APK

## 📋 环境要求
- **Node.js**: 14.x 或更高版本
- **Java JDK**: 8 或 11
- **Android SDK**: API 21+

## 🔧 故障排除

### 如果构建失败：
1. 检查 Node.js 和 Java 环境
2. 确保 Android SDK 已安装
3. 使用 HBuilder 云打包避免环境问题

### 如果网络问题：
1. 使用 HBuilder 国内服务器
2. 或使用 APKOnline 在线构建

## 🌐 替代方案

### 1. 微信小程序
考虑将应用改造成微信小程序，使用更方便

### 2. UniApp
使用 UniApp 框架，一次开发多端发布

### 3. 国内应用商店
上传到腾讯应用宝、华为应用市场等

---
**推荐优先使用 HBuilder 云打包，国内网络友好且简单易用！** 🎯