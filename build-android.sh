#!/bin/bash
echo "🛠️  绿申通 APK 构建脚本"
echo "========================"

echo "1. 检查 Node.js 环境..."
node --version
if [ $? -ne 0 ]; then
    echo "❌ 请先安装 Node.js: https://nodejs.org/zh-cn/"
    exit 1
fi

echo "2. 检查 Cordova..."
cordova --version
if [ $? -ne 0 ]; then
    echo "❌ 请安装 Cordova: npm install -g cordova"
    exit 1
fi

echo "3. 进入项目目录..."
cd cordova-project

echo "4. 安装项目依赖..."
npm install
if [ $? -ne 0 ]; then
    echo "❌ npm install 失败"
    exit 1
fi

echo "5. 添加 Android 平台..."
cordova platform add android
if [ $? -ne 0 ]; then
    echo "❌ 添加 Android 平台失败"
    echo "请检查 Android SDK 环境"
    exit 1
fi

echo "6. 检查环境要求..."
cordova requirements android
if [ $? -ne 0 ]; then
    echo "⚠️  环境检查有警告，但继续构建..."
fi

echo "7. 开始构建 APK..."
cordova build android
if [ $? -ne 0 ]; then
    echo "❌ 构建失败"
    exit 1
fi

echo ""
echo "✅ 构建成功！"
echo "📦 APK 文件位置:"
echo "cordova-project/platforms/android/app/build/outputs/apk/debug/app-debug.apk"
echo ""
echo "请将 APK 文件发送到手机进行测试"