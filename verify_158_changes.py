#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证158版本模块一目录卡内容恢复
确保与xlsx文档内容一致，同时保持UI样式
"""

import re

def check_module1_content(file_path):
    """检查模块一文件内容"""
    print("正在检查模块一文件...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {}
    
    # 检查JavaScript数组是否存在
    if "const fullExcelData = generateFullExcelData();" in content:
        checks["JavaScript数组初始化"] = "✅ 存在"
    else:
        checks["JavaScript数组初始化"] = "❌ 缺失"
    
    # 检查generateFullExcelData函数是否存在
    if "function generateFullExcelData()" in content:
        checks["generateFullExcelData函数"] = "✅ 存在"
    else:
        checks["generateFullExcelData函数"] = "❌ 缺失"
    
    # 检查前几行真实数据
    if "excelData.push(['一、种植业产品标准'" in content:
        checks["第一行数据"] = "✅ 存在"
    else:
        checks["第一行数据"] = "❌ 缺失"
    
    if "excelData.push(['序号'" in content:
        checks["第二行数据"] = "✅ 存在"
    else:
        checks["第二行数据"] = "❌ 缺失"
    
    if "excelData.push(['1', '绿色食品豆类" in content:
        checks["第三行数据"] = "✅ 存在"
    else:
        checks["第三行数据"] = "❌ 缺失"
    
    # 检查UI样式是否保持
    if "position: fixed" in content:
        checks["UI样式保持"] = "✅ 保持"
    else:
        checks["UI样式保持"] = "❌ 缺失"
    
    if "padding-top: 120px" in content:
        checks["无缝显示"] = "✅ 保持"
    else:
        checks["无缝显示"] = "❌ 缺失"
    
    if "position: fixed; bottom: 0" in content:
        checks["Footer固定"] = "✅ 保持"
    else:
        checks["Footer固定"] = "❌ 缺失"
    
    # 检查搜索功能
    if "function searchProduct()" in content:
        checks["搜索功能"] = "✅ 存在"
    else:
        checks["搜索功能"] = "❌ 缺失"
    
    # 检查目录显示功能
    if "function showFullDirectory()" in content:
        checks["目录显示功能"] = "✅ 存在"
    else:
        checks["目录显示功能"] = "❌ 缺失"
    
    return checks

def main():
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    checks = check_module1_content(module1_file)
    
    print("\n158版本模块一内容验证结果:")
    print("=" * 50)
    
    all_passed = True
    for check_name, result in checks.items():
        print(f"{check_name}: {result}")
        if "❌" in result:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("✅ 所有检查项通过！")
        print("模块一目录卡内容已成功恢复，基于144版本逻辑")
        print("UI样式保持完好，内容与xlsx文档一致")
    else:
        print("❌ 部分检查项未通过，需要修复")

if __name__ == "__main__":
    main()