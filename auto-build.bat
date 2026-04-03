@echo off
echo 🛠️  绿申通自动构建脚本
echo ============================

echo 正在检查环境...

:: 检查 Java
java -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Java 未安装，请先安装 JDK
    pause
    exit /b 1
)

echo ✅ Java 已安装

:: 检查 Android SDK
where adb >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Android SDK 未找到
    echo 请确保 Android Studio 已安装
    pause
    exit /b 1
)

echo ✅ Android SDK 已安装

echo.
echo 📋 请手动完成以下步骤：
echo.
echo 1. 打开 Android Studio
echo 2. 选择 "Open" (打开项目)
echo 3. 选择 "android-project" 文件夹
echo 4. 等待项目配置完成
echo 5. 点击 "Build" → "Make Project" (构建 → 生成项目)
echo 6. APK 文件将生成在:
echo    android-project\app\build\outputs\apk\debug\app-debug.apk
echo.
echo 🚀 或者使用更简单的 HBuilder:
echo 1. 下载 HBuilderX: https://www.dcloud.io/hbuilderx.html
echo 2. 打开 cordova-project 文件夹
echo 3. 点击 "发行" → "原生App-云打包"
echo.
pause