@echo off
echo 🔍 环境检查脚本
echo ====================

echo 1. 检查 Node.js...
node --version
if %errorlevel% neq 0 echo ❌ Node.js 未安装

echo.
echo 2. 检查 npm...
npm --version
if %errorlevel% neq 0 echo ❌ npm 不可用

echo.
echo 3. 检查 Cordova...
cordova --version
if %errorlevel% neq 0 echo ❌ Cordova 未安装

echo.
echo 4. 检查 Java...
java -version
if %errorlevel% neq 0 echo ❌ Java JDK 未安装

echo.
echo 5. 检查 Android SDK...
where adb >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Android SDK 未找到
    echo 请安装 Android Studio 或设置 ANDROID_HOME
) else (
    echo ✅ Android SDK 已安装
)

echo.
echo 📋 环境变量检查:
echo JAVA_HOME=%JAVA_HOME%
echo ANDROID_HOME=%ANDROID_HOME%

echo.
echo 📚 安装指南:
echo 1. Node.js: https://nodejs.org/zh-cn/
echo 2. Cordova: npm install -g cordova
echo 3. Android Studio: https://developer.android.com/studio
echo.
pause