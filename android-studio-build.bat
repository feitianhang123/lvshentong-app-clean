@echo off
echo 🛠️  Android Studio 自动构建脚本
echo ================================

echo 1. 设置环境变量...
set ANDROID_HOME=D:\Android\android-sdk
set JAVA_HOME=C:\Program Files\Java\jdk-17.0.2

echo 2. 检查 Android SDK...
if not exist "%ANDROID_HOME%" (
    echo ❌ Android SDK 未找到，请检查安装路径
    pause
    exit /b 1
)

echo ✅ Android SDK 已安装: %ANDROID_HOME%

echo 3. 检查 Java JDK...
if not exist "%JAVA_HOME%" (
    echo ❌ Java JDK 未找到，请检查安装路径
    pause
    exit /b 1
)

echo ✅ Java JDK 已安装: %JAVA_HOME%

echo 4. 添加环境变量到 PATH...
set PATH=%JAVA_HOME%\bin;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools;%ANDROID_HOME%\cmdline-tools\latest\bin;%PATH%

echo 5. 进入项目目录...
cd android-project

echo 6. 尝试使用 Gradle 构建...
echo   如果失败，请使用 Android Studio 手动构建:
echo   1. 打开 Android Studio
echo   2. 选择 "Open" (打开项目)
echo   3. 选择 "android-project" 文件夹
echo   4. 等待项目配置完成
echo   5. 点击 "Build" -> "Make Project" (构建 -> 生成项目)
echo   6. APK 文件将生成在: android-project\app\build\outputs\apk\debug\app-debug.apk

echo.
echo 📋 手动构建步骤（推荐）:
echo   - 打开 Android Studio
echo   - 打开 android-project 文件夹
echo   - Build -> Make Project
echo   - 获取 APK 文件

echo.
pause