#!/bin/bash
# 绿色食品申报通 Android 构建脚本

echo "🚀 开始构建绿色食品申报通APK..."

# 检查是否在项目根目录
if [ ! -d "android-project" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

cd android-project

# 检查gradlew权限
if [ ! -x "gradlew" ]; then
    echo "🔧 设置gradlew执行权限..."
    chmod +x gradlew
fi

echo "📦 清理项目..."
./gradlew clean

echo "🔨 构建Debug版本APK..."
if ./gradlew assembleDebug; then
    echo "✅ 构建成功!"
    echo "📱 APK位置: app/build/outputs/apk/debug/app-debug.apk"
    echo "💡 使用命令安装: adb install app/build/outputs/apk/debug/app-debug.apk"
else
    echo "❌ 构建失败!"
    exit 1
fi