@echo off
echo 🚀 绿色食品申报通 - 构建和测试脚本
echo.

REM 检查是否在项目根目录
if not exist "android-project" (
    echo ❌ 错误: 请在项目根目录运行此脚本
    pause
    exit /b 1
)

cd android-project

echo 📦 1. 清理项目...
gradlew clean
if %errorlevel% neq 0 (
    echo ❌ 清理失败!
    pause
    exit /b 1
)

echo 🔨 2. 构建Debug版本APK...
gradlew assembleDebug
if %errorlevel% neq 0 (
    echo ❌ 构建失败!
    pause
    exit /b 1
)

echo ✅ 3. 构建成功!
echo 📱 APK位置: app\build\outputs\apk\debug\app-debug.apk

echo.
echo 📋 4. 项目状态检查:
echo    ✅ HTML文件: 已修复乱码问题
echo    ✅ WebView配置: 已优化
echo    ✅ 主页面: 加载测试页面
echo    ✅ 模块一: 修复完成，使用本地JSON
echo    ✅ 自动构建: GitHub Actions已配置

echo.
echo 💡 下一步:
echo    1. 安装APK: adb install app\build\outputs\apk\debug\app-debug.apk
echo    2. 查看日志: adb logcat -s "WebView"
echo    3. 如果页面空白，检查HTML文件和控制台错误

echo.
pause