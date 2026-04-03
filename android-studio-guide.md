# 📱 Android Studio 构建指南 - 绿申通

## 🎯 手动构建步骤（推荐）

### 第一步：打开 Android Studio
1. 打开 Android Studio
2. 选择 "Open" (打开项目)
3. 选择 `android-project` 文件夹
4. 点击 "OK"

### 第二步：等待项目配置
Android Studio 会自动：
- ✅ 下载 Gradle
- ✅ 配置 Android SDK
- ✅ 同步项目依赖

### 第三步：构建 APK
1. 点击顶部菜单 "Build" (构建)
2. 选择 "Make Project" (生成项目)
   - 或使用快捷键 `Ctrl + F9`

### 第四步：找到 APK 文件
构建完成后：
1. 在左侧项目面板中展开：
   `app` → `build` → `outputs` → `apk` → `debug`
2. 右键点击 `app-debug.apk`
3. 选择 "Show in Explorer" (在资源管理器中显示)
4. 将 APK 文件发送到手机安装

## 📁 APK 文件位置
```
android-project/
└── app/
    └── build/
        └── outputs/
            └── apk/
                └── debug/
                    └── app-debug.apk  # 生成的 APK 文件
```

## ⚙️ 环境配置

### 必要组件：
- ✅ **Android Studio**: 已安装
- ✅ **Android SDK**: 已安装 (D:\Android\android-sdk)
- ✅ **Java JDK**: 已安装 (JDK 17.0.2)
- ✅ **平台工具**: android-33, android-34, android-35

### 环境变量：
```
ANDROID_HOME=D:\Android\android-sdk
JAVA_HOME=C:\Program Files\Java\jdk-17.0.2
```

## 🔧 故障排除

### 如果构建失败：
1. **检查 Gradle 版本**: Android Studio 会自动处理
2. **检查 SDK 平台**: 确保 android-33+ 已安装
3. **清理项目**: Build → Clean Project
4. **重新同步**: File → Sync Project with Gradle Files

### 如果找不到 APK：
1. 检查构建是否成功完成
2. 查看 "Build" 输出面板是否有错误
3. 尝试 "Build" → "Rebuild Project"

## 🚀 快速开始

### 最简单的方法：
1. **打开 Android Studio**
2. **打开项目**: 选择 `android-project` 文件夹
3. **等待配置**: 让 Android Studio 自动处理所有依赖
4. **构建**: Build → Make Project
5. **获取 APK**: 在 `app/build/outputs/apk/debug/` 中找到 APK

### 命令行方法（如果配置正确）：
```bash
cd android-project
./gradlew assembleDebug
```

## 📋 项目信息
- **应用名称**: 绿申通
- **包名**: com.lvshentong.app
- **目标 SDK**: Android 13 (API 33)
- **最低 SDK**: Android 5.0 (API 21)

## 💡 提示
- 第一次打开项目可能需要几分钟下载 Gradle
- 确保网络连接稳定
- 如果遇到 Gradle 错误，Android Studio 通常会提供修复建议
- 所有必要的 Android 平台都已经安装

---
**使用 Android Studio 手动构建是最可靠的方式！所有环境都已经配置好了。** 🎯