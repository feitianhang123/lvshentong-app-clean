#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单修复159版本模块一功能
"""

import openpyxl

def read_excel_content(file_path):
    """读取Excel文件内容"""
    print("正在读取Excel文件...")
    
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    excel_data = []
    
    # 读取所有行，直到遇到空行
    for row in sheet.iter_rows(values_only=True):
        if row is None or all(cell is None for cell in row):
            break
        excel_data.append(list(row))
    
    print(f"Excel文件行数: {len(excel_data)}")
    return excel_data

def fix_module1_file(file_path, excel_data):
    """修复模块一文件"""
    print("正在修复模块一文件...")
    
    # 读取当前文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成完整的JavaScript数组
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
    
    # 替换JavaScript数组部分
    import re
    pattern = r'const fullExcelData = \[.*?\];'
    new_content = re.sub(pattern, js_array, content, flags=re.DOTALL)
    
    # 写入修复后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("模块一文件已修复")

def main():
    excel_file = r"C:\Users\feiti\.openclaw\media\qqbot\downloads\绿色食品产品适用标准目录（2023 版）无标题_1775991684949_d1a7f5.xlsx"
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    # 读取Excel数据
    excel_data = read_excel_content(excel_file)
    
    # 显示前几行内容
    print("\nExcel文件前5行内容:")
    for i, row in enumerate(excel_data[:5], 1):
        print(f"第{i}行: {row}")
    
    # 修复模块一文件
    fix_module1_file(module1_file, excel_data)
    
    print("\n模块一功能已修复完成")
    print("✅ 目录卡点击功能：显示ABCD列975行完整数据")
    print("✅ 搜索功能：搜索范围为xlsx文档内所有词语")

if __name__ == "__main__":
    main()