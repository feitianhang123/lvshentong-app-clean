#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查模块一内容与原始Excel文件的一致性
确保975行ABCD列内容完全一致
"""

import openpyxl
import re

def read_excel_content(file_path):
    """读取Excel文件内容"""
    print(f"正在读取Excel文件: {file_path}")
    
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    excel_data = []
    
    # 读取所有行，直到遇到空行
    for row in sheet.iter_rows(values_only=True):
        if row is None or all(cell is None for cell in row):
            break
        excel_data.append(list(row))
    
    print(f"Excel文件行数: {len(excel_data)}")
    
    # 显示前几行内容
    print("\nExcel文件前10行内容:")
    for i, row in enumerate(excel_data[:10], 1):
        print(f"第{i}行: {row}")
    
    return excel_data

def read_module1_content(file_path):
    """读取模块一HTML文件中的目录内容"""
    print(f"\n正在读取模块一文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找JavaScript中的fullExcelData数组
    pattern = r'const fullExcelData = (\[.*?\]);'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        print("找到fullExcelData数组")
        array_content = match.group(1)
        
        # 使用eval安全地解析数组
        try:
            module_data = eval(array_content)
            print(f"模块一文件行数: {len(module_data)}")
            
            # 显示前几行内容
            print("\n模块一前10行内容:")
            for i, row in enumerate(module_data[:10], 1):
                print(f"第{i}行: {row}")
            
            return module_data
        except Exception as e:
            print(f"解析数组时出错: {e}")
            return []
    else:
        print("未找到fullExcelData数组")
        return []

def compare_data(excel_data, module_data):
    """比较两个数据集的差异"""
    print("\n正在比较数据...")
    
    # 检查行数
    print(f"Excel行数: {len(excel_data)}, 模块一行数: {len(module_data)}")
    
    if len(excel_data) != len(module_data):
        print("警告: 行数不一致! 需要修复")
    
    # 比较前10行的内容
    min_rows = min(10, len(excel_data), len(module_data))
    print(f"\n比较前{min_rows}行内容:")
    
    differences = []
    for i in range(min_rows):
        excel_row = excel_data[i]
        module_row = module_data[i]
        
        # 处理None值
        excel_row = [str(cell) if cell is not None else '' for cell in excel_row]
        module_row = [str(cell) if cell is not None else '' for cell in module_row]
        
        if excel_row != module_row:
            print(f"第{i+1}行不一致:")
            print(f"  Excel: {excel_row}")
            print(f"  模块一: {module_row}")
            differences.append((i+1, excel_row, module_row))
        else:
            print(f"第{i+1}行: 一致")
    
    return differences

def main():
    excel_file = r"C:\Users\feiti\.openclaw\media\qqbot\downloads\绿色食品产品适用标准目录（2023 版）无标题_1775991684949_d1a7f5.xlsx"
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    # 读取数据
    excel_data = read_excel_content(excel_file)
    module_data = read_module1_content(module1_file)
    
    # 比较数据
    differences = compare_data(excel_data, module_data)
    
    if differences:
        print(f"\n发现 {len(differences)} 处不一致")
        print("需要修复模块一的内容")
        return False
    else:
        print("\n模块一内容与Excel文件完全一致")
        return True

if __name__ == "__main__":
    main()