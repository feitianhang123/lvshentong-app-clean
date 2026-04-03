# 🚀 GitHub项目上传脚本 - 绿申通
# ===================================

Write-Host "步骤1: 检查Git安装..." -ForegroundColor Green
git --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git未安装，请先安装: https://git-scm.com/download/win" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "✅ Git已安装" -ForegroundColor Green
Write-Host ""

Write-Host "步骤2: 请先创建GitHub仓库:" -ForegroundColor Yellow
Write-Host "1. 访问 https://github.com/new"
Write-Host "2. 创建仓库: lvshentong-app"
Write-Host "3. 获取仓库URL"
Write-Host ""

$GITHUB_URL = Read-Host "请输入GitHub仓库URL（例如: https://github.com/用户名/lvshentong-app.git）"

if ([string]::IsNullOrEmpty($GITHUB_URL)) {
    Write-Host "❌ 必须提供GitHub仓库URL" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "步骤3: 克隆仓库..." -ForegroundColor Green
git clone $GITHUB_URL github-build
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 克隆失败，请检查URL是否正确" -ForegroundColor Red
    pause
    exit 1
}

Set-Location github-build

Write-Host ""
Write-Host "步骤4: 复制项目文件..." -ForegroundColor Green

# 复制Android项目
if (Test-Path "../android-project") {
    Copy-Item -Path "../android-project" -Destination "." -Recurse -Force
    Write-Host "✅ Android项目复制完成" -ForegroundColor Green
} else {
    Write-Host "⚠️ Android项目目录不存在" -ForegroundColor Yellow
}

# 复制Cordova项目
if (Test-Path "../cordova-project") {
    Copy-Item -Path "../cordova-project" -Destination "." -Recurse -Force
    Write-Host "✅ Cordova项目复制完成" -ForegroundColor Green
} else {
    Write-Host "⚠️ Cordova项目目录不存在" -ForegroundColor Yellow
}

# 复制ZIP文件
if (Test-Path "../greenfood-app.zip") {
    Copy-Item -Path "../greenfood-app.zip" -Destination "." -Force
    Write-Host "✅ ZIP文件复制完成" -ForegroundColor Green
} elseif (Test-Path "../greenfood-app-new.zip") {
    Copy-Item -Path "../greenfood-app-new.zip" -Destination ".\greenfood-app.zip" -Force
    Write-Host "✅ ZIP文件复制完成（重命名）" -ForegroundColor Green
} else {
    Write-Host "⚠️ ZIP文件不存在，正在创建..." -ForegroundColor Yellow
    Set-Location ..
    Compress-Archive -Path index_fixed.html, module1_fixed_final_v4.html, module2_current_standards.html, module3_final.html, standards_data.js -DestinationPath greenfood-app.zip
    Set-Location github-build
    Copy-Item -Path "../greenfood-app.zip" -Destination "." -Force
    Write-Host "✅ ZIP文件创建并复制完成" -ForegroundColor Green
}

# 复制GitHub Actions配置
if (Test-Path "../.github") {
    Copy-Item -Path "../.github" -Destination "." -Recurse -Force
    Write-Host "✅ GitHub Actions配置复制完成" -ForegroundColor Green
} else {
    Write-Host "⚠️ .github目录不存在，创建中..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path ".github/workflows" -Force
    if (Test-Path "../.github/workflows/android-build.yml") {
        Copy-Item -Path "../.github/workflows/android-build.yml" -Destination ".github/workflows/" -Force
    }
}

Write-Host ""
Write-Host "步骤5: 提交到GitHub..." -ForegroundColor Green
git add .
git commit -m "feat: 添加绿申通完整项目"

Write-Host ""
Write-Host "步骤6: 推送到GitHub..." -ForegroundColor Green
Write-Host "请输入GitHub用户名和密码（建议使用访问令牌）" -ForegroundColor Yellow
git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 推送失败，请检查凭据" -ForegroundColor Red
    Write-Host "提示: 建议使用GitHub访问令牌而不是密码" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host ""
Write-Host "✅ 上传完成！" -ForegroundColor Green
Write-Host "📋 下一步操作:" -ForegroundColor Cyan
Write-Host "1. 访问你的GitHub仓库: $GITHUB_URL"
Write-Host "2. 点击'Actions'标签页"
Write-Host "3. 运行'Android CI'工作流"
Write-Host "4. 等待构建完成"
Write-Host "5. 下载生成的APK文件"
Write-Host ""
pause