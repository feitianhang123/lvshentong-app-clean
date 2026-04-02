#!/usr/bin/env python3
"""
诊断模块一JSON加载问题
"""
import json
import os

def diagnose_json_loading():
    print("=== JSON加载问题诊断 ===")
    
    # 1. 检查文件是否存在
    json_path = "complete_excel.json"
    print(f"1. 检查文件是否存在: {json_path}")
    if os.path.exists(json_path):
        print(f"   文件存在，大小: {os.path.getsize(json_path)} 字节")
    else:
        print(f"   文件不存在")
        return False
    
    # 2. 检查文件可读性
    print(f"2. 检查文件可读性")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"   文件可读取，长度: {len(content)} 字符")
    except Exception as e:
        print(f"   文件读取失败: {e}")
        return False
    
    # 3. 检查JSON格式
    print(f"3. 检查JSON格式")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"   JSON格式正确，共 {len(data)} 行数据")
        print(f"   第一行数据: {data[0]}")
    except Exception as e:
        print(f"   JSON解析失败: {e}")
        return False
    
    # 4. 检查数据内容
    print(f"4. 检查数据内容")
    products = [item for item in data if item.get('col3') and item['col3'] != 'nan']
    print(f"   有效产品数量: {len(products)}")
    
    # 5. 测试搜索功能
    print(f"5. 测试搜索功能")
    test_terms = ['苹果', '肉', '茶']
    for term in test_terms:
        results = [item for item in products if term in item.get('col3', '')]
        print(f"   搜索'{term}': 找到 {len(results)} 个结果")
    
    print("\n=== 诊断完成 ===")
    print("所有检查通过！JSON文件和数据都正常")
    return True

if __name__ == "__main__":
    diagnose_json_loading()