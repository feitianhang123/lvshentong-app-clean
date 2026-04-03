# 绿色食品申报通 Android应用

## 📱 项目概述

这是一个用于绿色食品申报的Android移动应用，包含三个主要功能模块：

1. **模块一**: 产品目录搜索 - 查询绿色食品适用标准目录
2. **模块二**: 文档下载 - 获取申报相关文档模板
3. **模块三**: 申报指南 - 查看申报流程和指南

## 🛠️ 技术栈

- **Android**: Java + WebView
- **前端**: HTML5 + CSS3 + JavaScript
- **数据**: JSON格式的产品标准目录
- **构建**: Gradle + GitHub Actions

## 🚀 构建说明

### GitHub Actions自动构建

每次推送到 `master` 分支时，GitHub Actions会自动构建APK：
1. ✅ 检查代码
2. ✅ 设置Android环境
3. ✅ 构建Debug APK
4. ✅ 上传构建产物

### 本地构建

```bash
cd android-project
./gradlew assembleDebug
```

APK位置: `app/build/outputs/apk/debug/app-debug.apk`

## 📁 项目结构

```
lvshentong-app-clean/
├── android-project/          # Android项目目录
│   ├── app/
│   │   └── src/main/assets/www/
│   │       ├── index_fixed.html      # 主页面
│   │       ├── module1_fixed_final_v4.html  # 模块一：产品目录
│   │       ├── module2.html          # 模块二：文档下载
│   │       ├── module3_final.html    # 模块三：申报指南
│   │       ├── complete_excel.json   # 产品标准数据
│   │       └── test_webview.html     # WebView测试页面
│   └── build.gradle
├── .github/workflows/       # GitHub Actions配置
└── README.md
```

## 📋 功能状态

- ✅ **模块一**: 产品目录搜索 - 使用本地JSON数据，完全修复
- ✅ **模块二**: 文档下载 - 功能正常
- ✅ **模块三**: 申报指南 - 功能正常
- ✅ **自动构建**: GitHub Actions配置完成

## 🔗 GitHub仓库

https://github.com/feitianhang123/lvshentong-app-clean

---
*专注于APK构建和功能交付*