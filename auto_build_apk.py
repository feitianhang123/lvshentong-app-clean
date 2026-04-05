#!/usr/bin/env python3
"""
绿色食品申报通 - 自动APK构建脚本
版本: 118
"""

import os
import requests
import zipfile
import time

def create_web_app_package():
    """创建Web应用包"""
    print("创建Web应用包...")
    
    # 确保目录存在
    os.makedirs("web-app-package", exist_ok=True)
    
    # 复制最新文件
    files_to_copy = [
        "module1-complete.html",
        "module2_current_standards.html", 
        "module3_final.html",
        "standards_data.js",
        "green_food_products.json",
        "green_food_standards.xlsx"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            os.system(f"copy {file} web-app-package\\")
            print(f"复制: {file}")
    
    # 创建主页
    index_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>绿色食品申报通</title>
    <style>
        body { background: #f5f5f5; font-family: Arial; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #388e3c; text-align: center; }
        .module { background: #e8f5e8; margin: 10px 0; padding: 15px; border-radius: 5px; cursor: pointer; }
        .module:hover { background: #c8e6c9; }
    </style>
</head>
<body>
    <div class="container">
        <h1>绿色食品申报通</h1>
        <div class="module" onclick="location.href='module1-complete.html'">
            <h3>📋 产品标准查询</h3>
            <p>智能搜索绿色食品产品标准</p>
        </div>
        <div class="module" onclick="location.href='module2_current_standards.html'">
            <h3>📊 现行标准查询</h3>
            <p>143个绿色食品标准库</p>
        </div>
        <div class="module" onclick="location.href='module3_final.html'">
            <h3>📝 材料清单</h3>
            <p>申报材料清单和下载</p>
        </div>
        <p style="text-align: center; margin-top: 20px; color: #666;">版本: 118 - 最新版本</p>
    </div>
</body>
</html>"""
    
    with open("web-app-package/index.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print("主页创建完成")
    
    # 创建zip包
    with zipfile.ZipFile("greenfood-web-app-v118.zip", "w") as zipf:
        for root, dirs, files in os.walk("web-app-package"):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, "web-app-package"))
    
    print("ZIP包创建完成: greenfood-web-app-v118.zip")
    return "greenfood-web-app-v118.zip"

def upload_to_github():
    """上传到GitHub"""
    print("上传到GitHub...")
    
    # 提交更改
    os.system("git add .")
    os.system('git commit -m "版本118: 自动构建APK准备"')
    os.system("git push")
    
    print("代码已推送到GitHub")

def main():
    """主函数"""
    print("绿色食品申报通 - APK自动构建")
    print("=" * 50)
    
    # 1. 创建Web应用包
    zip_file = create_web_app_package()
    
    # 2. 上传到GitHub
    upload_to_github()
    
    # 3. 提供构建指南
    print("\nAPK构建指南:")
    print("1. 下载文件: greenfood-web-app-v118.zip")
    print("2. 访问在线构建服务:")
    print("   - APKOnline: https://www.apkonline.net/")
    print("   - Appetize: https://appetize.io/")
    print("3. 上传ZIP文件并配置应用信息")
    print("4. 下载生成的APK文件")
    
    print("\n自动构建准备完成!")
    print(f"文件: {zip_file}")
    print("GitHub: https://github.com/feitianhang123/lvshentong-app-clean")

if __name__ == "__main__":
    main()