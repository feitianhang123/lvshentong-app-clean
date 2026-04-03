@echo off
echo 🚀 GitHub项目上传脚本 - 绿申通
echo ===================================

echo 步骤1: 检查Git安装...
git --version
if %errorlevel% neq 0 (
    echo ❌ Git未安装，请先安装: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git已安装
echo.

echo 步骤2: 请先创建GitHub仓库:
echo 1. 访问 https://github.com/new
echo 2. 创建仓库: lvshentong-app
echo 3. 获取仓库URL
echo.

set /p GITHUB_URL=请输入GitHub仓库URL（例如: https://github.com/用户名/lvshentong-app.git）: 

if "%GITHUB_URL%"=="" (
    echo ❌ 必须提供GitHub仓库URL
    pause
    exit /b 1
)

echo.
echo 步骤3: 克隆仓库...
git clone %GITHUB_URL% github-build
if %errorlevel% neq 0 (
    echo ❌ 克隆失败，请检查URL是否正确
    pause
    exit /b 1
)

cd github-build

echo.
echo 步骤4: 复制项目文件...

:: 复制Android项目
xcopy /E /I "..\android-project" "."
if %errorlevel% neq 0 (
    echo ⚠️ Android项目复制可能有问题，继续...
)

:: 复制Cordova项目
xcopy /E /I "..\cordova-project" "."
if %errorlevel% neq 0 (
    echo ⚠️ Cordova项目复制可能有问题，继续...
)

:: 复制ZIP文件
if exist "..\greenfood-app.zip" (
    copy "..\greenfood-app.zip" "."
) else if exist "..\greenfood-app-new.zip" (
    copy "..\greenfood-app-new.zip" ".\greenfood-app.zip"
) else (
    echo ⚠️ ZIP文件不存在，正在创建...
    cd ..
    powershell -Command "Compress-Archive -Path index_fixed.html, module1_fixed_final_v4.html, module2_current_standards.html, module3_final.html, standards_data.js -DestinationPath greenfood-app.zip"
    cd github-build
    copy "..\greenfood-app.zip" "."
)
if %errorlevel% neq 0 (
    echo ⚠️ ZIP文件复制可能有问题，继续...
)

:: 复制GitHub Actions配置
if exist "..\.github" (
    xcopy /E /I "..\.github" "."
) else (
    echo ⚠️ .github目录不存在，创建中...
    mkdir .github\workflows
    copy "..\.github\workflows\android-build.yml" ".github\workflows\"
)

echo.
echo 步骤5: 提交到GitHub...
git add .
git commit -m "feat: 添加绿申通完整项目"

echo.
echo 步骤6: 推送到GitHub...
echo 请输入GitHub用户名和密码（或访问令牌）
git push origin main

if %errorlevel% neq 0 (
    echo ❌ 推送失败，请检查凭据
    echo 提示: 建议使用GitHub访问令牌而不是密码
    pause
    exit /b 1
)

echo.
echo ✅ 上传完成！
echo 📋 下一步操作:
echo 1. 访问你的GitHub仓库: %GITHUB_URL%
echo 2. 点击"Actions"标签页
echo 3. 运行"Android CI"工作流
echo 4. 等待构建完成
echo 5. 下载生成的APK文件
echo.
pause