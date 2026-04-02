@echo off
echo 🚀 开始构建绿色食品申报通APK...

REM 检查是否在项目根目录
if not exist "android-project" (
    echo ❌ 错误: 请在项目根目录运行此脚本
    pause
    exit /b 1
)

cd android-project

echo 📦 清理项目...
gradlew clean

if %errorlevel% neq 0 (
    echo ❌ 清理失败!
    pause
    exit /b 1
)

echo 🔨 构建Debug版本APK...
gradlew assembleDebug

if %errorlevel% neq 0 (
    echo ❌ 构建失败!
    pause
    exit /b 1
)

echo ✅ 构建成功!
echo 📱 APK位置: app\build\outputs\apk\debug\app-debug.apk
echo 💡 使用命令安装: adb install app\build\outputs\apk\debug\app-debug.apk

pause