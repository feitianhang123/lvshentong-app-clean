@echo off
echo 📋 上传前文件检查
echo ====================

echo 检查必需文件是否存在...
echo.

if exist android-project (
    echo ✅ android-project/ 存在
dir android-project | find "app"
) else (
    echo ❌ android-project/ 不存在
)

echo.

if exist cordova-project (
    echo ✅ cordova-project/ 存在
dir cordova-project | find "www"
) else (
    echo ❌ cordova-project/ 不存在
)

echo.

if exist .github (
    echo ✅ .github/ 存在
dir .github\workflows | find "android-build"
) else (
    echo ❌ .github/ 不存在
)

echo.

if exist greenfood-app.zip (
    echo ✅ greenfood-app.zip 存在
dir greenfood-app.zip
) else (
    echo ❌ greenfood-app.zip 不存在
)

echo.
echo 📊 文件状态总结:
echo.
if exist android-project if exist cordova-project if exist .github if exist greenfood-app.zip (
    echo 🎉 所有文件就绪！可以运行 github-upload.bat
echo.
echo 运行命令:
echo   github-upload.bat
) else (
    echo ⚠️ 部分文件缺失，请检查以上列表
)

echo.
pause