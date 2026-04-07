import pandas as pd
import json

def read_excel_content():
    """读取Excel文件内容"""
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    
    excel_data = []
    for i in range(len(df)):
        row_data = []
        for col in range(4):  # ABCD列
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            row_data.append(str(value))
        excel_data.append(row_data)
    
    return excel_data

def analyze_module1_content():
    """分析模块一的内容"""
    # 读取模块一文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找JavaScript中的fullExcelData数组
    start_idx = content.find('const fullExcelData = generateFullExcelData();')
    if start_idx == -1:
        return None
    
    # 查找generateFullExcelData函数
    func_start = content.find('function generateFullExcelData()')
    func_end = content.find('function searchProduct()', func_start)
    
    if func_start == -1 or func_end == -1:
        return None
    
    function_code = content[func_start:func_end]
    
    # 提取push语句中的数组
    import re
    push_matches = re.findall(r'excelData\.push\(\[(.*?)\]\)', function_code, re.DOTALL)
    
    module1_data = []
    for match in push_matches:
        # 解析数组内容
        row_str = match.replace('\n', '').replace('\\n', '\n')
        row_items = []
        
        # 简单的字符串分割
        parts = row_str.split(",'")
        if len(parts) > 1:
            for i, part in enumerate(parts):
                if i == 0:
                    part = part.strip()[1:] if part.strip().startswith("['") else part.strip()
                part = part.strip(" '")
                row_items.append(part)
        else:
            # 尝试其他解析方式
            row_items = [item.strip(" '\"") for item in row_str.split(",")]
        
        module1_data.append(row_items)
    
    return module1_data

def compare_data(excel_data, module1_data):
    """比较Excel数据和模块一数据"""
    differences = []
    
    # 比较行数
    if len(excel_data) != len(module1_data):
        differences.append(f"行数不一致: Excel有{len(excel_data)}行，模块一有{len(module1_data)}行")
    
    # 比较具体内容
    min_rows = min(len(excel_data), len(module1_data))
    for i in range(min_rows):
        excel_row = excel_data[i]
        module1_row = module1_data[i] if i < len(module1_data) else []
        
        for col in range(4):
            excel_val = excel_row[col] if col < len(excel_row) else ''
            module1_val = module1_row[col] if col < len(module1_row) else ''
            
            if excel_val != module1_val:
                differences.append(f"第{i+1}行第{col+1}列不一致:")
                differences.append(f"  Excel: {excel_val}")
                differences.append(f"  模块一: {module1_val}")
                differences.append("---")
    
    return differences

if __name__ == "__main__":
    print("开始对比Excel文件和模块一内容...")
    
    # 读取Excel数据
    excel_data = read_excel_content()
    print(f"Excel文件总行数: {len(excel_data)}")
    
    # 读取模块一数据
    module1_data = analyze_module1_content()
    if module1_data:
        print(f"模块一数据行数: {len(module1_data)}")
        
        # 比较数据
        differences = compare_data(excel_data, module1_data)
        
        if differences:
            print("\n发现差异:")
            for diff in differences:
                print(diff)
        else:
            print("\n模块一内容与Excel文件完全一致")
    else:
        print("无法解析模块一的内容")
    
    # 显示Excel文件的前几行作为参考
    print("\nExcel文件前10行内容:")
    for i in range(min(10, len(excel_data))):
        print(f"第{i+1}行: {excel_data[i]}")