@echo off
echo 🛠️  绿申通 APK 构建脚本
echo ================================

echo 1. 检查 Node.js 环境...
node --version
if %errorlevel% neq 0 (
    echo ❌ 请先安装 Node.js: https://nodejs.org/zh-cn/
    pause
    exit /b 1
)

echo 2. 检查 Cordova...
cordova --version
if %errorlevel% neq 0 (
    echo ❌ 请安装 Cordova: npm install -g cordova
    pause
    exit /b 1
)

echo 3. 进入项目目录...
cd cordova-project

echo 4. 安装项目依赖...
npm install
if %errorlevel% neq 0 (
    echo ❌ npm install 失败
    pause
    exit /b 1
)

echo 5. 添加 Android 平台...
cordova platform add android
if %errorlevel% neq 0 (
    echo ❌ 添加 Android 平台失败
    echo 请检查 Android SDK 环境
    pause
    exit /b 1
)

echo 6. 检查环境要求...
cordova requirements android
if %errorlevel% neq 0 (
    echo ⚠️  环境检查有警告，但继续构建...
)

echo 7. 开始构建 APK...
cordova build android
if %errorlevel% neq 0 (
    echo ❌ 构建失败
    pause
    exit /b 1
)

echo.
echo ✅ 构建成功！
echo 📦 APK 文件位置:
echo cordova-project/platforms/android/app/build/outputs/apk/debug/app-debug.apk
echo.
echo 请将 APK 文件发送到手机进行测试
pause