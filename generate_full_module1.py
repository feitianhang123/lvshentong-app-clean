import pandas as pd
import re

def read_excel_file():
    """读取Excel文件并返回完整内容"""
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

def generate_full_module1():
    """生成包含完整976行数据的模块一文件"""
    excel_data = read_excel_file()
    print(f'Excel文件总行数: {len(excel_data)}')
    
    # 读取模板文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 生成完整的JavaScript数组
    js_array = 'const fullExcelData = [\n'
    for i, row in enumerate(excel_data):
        js_row = '    ['
        for j, cell in enumerate(row):
            # 转义特殊字符
            cell_escaped = cell.replace('\n', '\\n').replace('"', '\\"').replace("'", "\\'")
            js_row += f"'{cell_escaped}'"
            if j < len(row) - 1:
                js_row += ', '
        js_row += ']'
        if i < len(excel_data) - 1:
            js_row += ','
        js_array += js_row + '\n'
    js_array += '];\n'
    
    # 替换数组定义
    # 查找原有的数组定义
    pattern = r'const fullExcelData = generateFullExcelData\(\);'
    new_content = re.sub(pattern, js_array, template)
    
    # 替换generateFullExcelData函数
    func_pattern = r'function generateFullExcelData\(\) \{[\s\S]*?\}'
    new_function = 'function generateFullExcelData() {\n    return fullExcelData;\n}'
    new_content = re.sub(func_pattern, new_function, new_content)
    
    # 更新注释中的行数
    new_content = new_content.replace('完整975行产品目录', f'完整{len(excel_data)}行产品目录')
    new_content = new_content.replace('975行完整Excel数据', f'{len(excel_data)}行完整Excel数据')
    
    # 保存新文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v8.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'已生成模块一v8文件: {output_path}')
    
    # 验证生成结果
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 检查数组行数
    array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
    if array_matches:
        array_content = array_matches[0]
        row_count = array_content.count('[')
        print(f'生成文件中的数组行数: {row_count}')
        
        if row_count == len(excel_data):
            print('生成成功: 行数一致')
        else:
            print(f'生成失败: 期望{len(excel_data)}行，实际{row_count}行')
    
    return output_path

if __name__ == "__main__":
    output_file = generate_full_module1()
    print(f'模块一文件生成完成: {output_file}')