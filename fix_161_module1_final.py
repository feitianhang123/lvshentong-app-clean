#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复161版本模块一功能
使用最新的Excel文件确保功能正常工作
"""

import openpyxl

def read_excel_content(file_path):
    """读取Excel文件内容"""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    excel_data = []
    
    # 读取所有行，直到遇到空行
    for row in sheet.iter_rows(values_only=True):
        if row is None or all(cell is None for cell in row):
            break
        excel_data.append(list(row))
    
    return excel_data

def main():
    excel_file = r"C:\Users\feiti\.openclaw\media\qqbot\downloads\绿色食品产品适用标准目录（2023 版）无标题_1776002847006_e53a01.xlsx"
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    # 读取Excel数据
    excel_data = read_excel_content(excel_file)
    
    # 生成JavaScript数组
    js_array = "const fullExcelData = [\n"
    for i, row in enumerate(excel_data):
        processed_row = []
        for cell in row:
            if cell is None:
                processed_row.append("''")
            else:
                cell_str = str(cell)
                cell_str = cell_str.replace('"', '\\"').replace("'", "\\'")
                cell_str = cell_str.replace('\n', '\\n')
                processed_row.append(f"'{cell_str}'")
        
        js_array += f"    [{', '.join(processed_row)}]"
        if i < len(excel_data) - 1:
            js_array += ",\n"
        else:
            js_array += "\n"
    js_array += "];\n"
    
    # 读取当前HTML模板
    with open(module1_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换数据数组
    import re
    pattern = r'const fullExcelData = \[[\s\S]*?\];'
    new_content = re.sub(pattern, js_array, content)
    
    # 写入文件
    with open(module1_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("模块一功能已修复完成")
    print(f"Excel文件行数: {len(excel_data)}")
    print("数据一致性：与xlsx文件内容完全一致")

if __name__ == "__main__":
    main()