@echo off
echo 文件检查:
echo.

echo 检查 android-project...
if exist android-project echo ✅ 存在
echo.

echo 检查 cordova-project...
if exist cordova-project echo ✅ 存在
echo.

echo 检查 .github...
if exist .github echo ✅ 存在
echo.

echo 检查 ZIP文件...
if exist greenfood-app.zip (
    echo ✅ greenfood-app.zip 存在
) else if exist greenfood-app-new.zip (
    echo ✅ greenfood-app-new.zip 存在
) else (
    echo ❌ ZIP文件不存在
)

echo.
echo 检查完成
echo.
pause