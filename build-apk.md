# 📦 绿色食品申报通 - APK打包指南

## 🛠️ 构建方法

### 方法一：使用Android Studio（推荐）
1. 安装 [Android Studio](https://developer.android.com/studio)
2. 打开项目文件夹 `android-project`
3. 连接Android手机并启用USB调试
4. 点击 "Run" 按钮安装到设备

### 方法二：命令行构建
```bash
# 进入项目目录
cd android-project

# 编译APK (需要安装Android SDK)
./gradlew assembleDebug

# 生成的APK位置:
# android-project/app/build/outputs/apk/debug/app-debug.apk
```

### 方法三：在线构建服务
如果本地没有Android环境，可以使用在线服务：
1. [Appetize.io](https://appetize.io/) - 在线构建和测试
2. [Cordova Build](https://build.phonegap.com/) - 在线打包
3. [APKOnline](https://www.apkonline.net/) - 在线APK构建

## 📁 项目结构
```
android-project/
├── app/
│   ├── src/main/
│   │   ├── assets/www/          # Web文件
│   │   │   ├── index_fixed.html         # 主页
│   │   │   ├── module1_fixed_final_v4.html    # 模块一
│   │   │   ├── module2_current_standards.html # 模块二
│   │   │   ├── module3_final.html      # 模块三
│   │   │   └── standards_data.js       # 标准数据
│   │   ├── java/com/greenfood/app/MainActivity.java
│   │   ├── res/layout/activity_main.xml
│   │   └── AndroidManifest.xml
│   └── build.gradle
├── build.gradle
├── settings.gradle
└── gradle.properties
```

## ⚙️ 配置说明

### Android配置
- **minSdk**: 21 (Android 5.0+)
- **targetSdk**: 34 (Android 14)
- **包名**: com.lvshentong.app

### WebView配置
- 启用JavaScript
- 启用DOM存储
- 支持内部链接导航
- 支持后退按钮

## 📲 功能特性
- ✅ 离线使用 - 所有文件本地存储
- ✅ 响应式设计 - 完美适配手机
- ✅ 原生体验 - WebView封装
- ✅ 快速加载 - 本地文件无需网络

## 🔧 自定义修改

### 修改应用名称
编辑 `android-project/app/src/main/res/values/strings.xml`

### 修改图标
替换 `android-project/app/src/main/res/mipmap-*/ic_launcher.png`

### 添加权限
编辑 `android-project/app/src/main/AndroidManifest.xml`

## 🚀 测试建议

1. **功能测试**: 确保所有模块链接正常工作
2. **性能测试**: 检查页面加载速度
3. **兼容性测试**: 在不同Android版本测试
4. **用户体验测试**: 确保触摸操作流畅

## 📞 技术支持

如果构建遇到问题，可以：
1. 使用在线构建服务
2. 安装Android Studio学习基础开发
3. 考虑使用更简单的打包工具如"WebView App"

---
**项目已准备好构建，祝你测试顺利！** 🎉