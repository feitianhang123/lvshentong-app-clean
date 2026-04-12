#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将原始Excel文件内容更新到模块一文件中
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
    return excel_data

def generate_js_array(excel_data):
    """生成JavaScript数组代码"""
    js_lines = []
    js_lines.append("const fullExcelData = [")
    
    for i, row in enumerate(excel_data):
        # 处理None值
        processed_row = []
        for cell in row:
            if cell is None:
                processed_row.append("''")
            else:
                # 处理字符串中的特殊字符
                cell_str = str(cell)
                # 转义引号和换行符
                cell_str = cell_str.replace('"', '\\"').replace("'", "\\'")
                cell_str = cell_str.replace('\n', '\\n')
                processed_row.append(f"'{cell_str}'")
        
        js_line = f"    [{', '.join(processed_row)}]"
        if i < len(excel_data) - 1:
            js_line += ","
        js_lines.append(js_line)
    
    js_lines.append("];")
    return '\n'.join(js_lines)

def update_module1_file(file_path, excel_data):
    """更新模块一文件内容"""
    print(f"正在更新模块一文件: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的JavaScript数组代码
    new_js_array = generate_js_array(excel_data)
    
    # 查找并替换原有的数组定义
    pattern = r'const fullExcelData = \[.*?\];'
    new_content = re.sub(pattern, new_js_array, content, flags=re.DOTALL)
    
    # 移除generateFullExcelData函数
    pattern2 = r'function generateFullExcelData\(\) \{[\s\S]*?return excelData\.slice\(0, 975\); // 确保正好975行\s*\}'
    new_content = re.sub(pattern2, '', new_content, flags=re.DOTALL)
    
    # 移除函数调用
    new_content = new_content.replace("const fullExcelData = generateFullExcelData();", "")
    
    # 写入更新后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("模块一文件已更新")
    return new_content

def main():
    excel_file = r"C:\Users\feiti\.openclaw\media\qqbot\downloads\绿色食品产品适用标准目录（2023 版）无标题_1775991684949_d1a7f5.xlsx"
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    # 读取Excel数据
    excel_data = read_excel_content(excel_file)
    
    # 显示前几行内容
    print("\nExcel文件前10行内容:")
    for i, row in enumerate(excel_data[:10], 1):
        print(f"第{i}行: {row}")
    
    # 更新模块一文件
    update_module1_file(module1_file, excel_data)
    
    print("\n✅ 模块一内容已成功更新为原始Excel数据")
    print(f"共更新 {len(excel_data)} 行数据")

if __name__ == "__main__":
    main()