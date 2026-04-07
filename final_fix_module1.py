import pandas as pd

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

def create_correct_module1():
    """创建正确的模块一文件"""
    excel_data = read_excel_file()
    print(f'Excel文件总行数: {len(excel_data)}')
    
    # 读取v6文件的模板
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 生成完整的JavaScript数组
    js_array_lines = ['const fullExcelData = [']
    
    for i, row in enumerate(excel_data):
        js_row = '    ['
        for j, cell in enumerate(row):
            # 转义特殊字符
            cell_escaped = cell.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"').replace("'", "\\'")
            js_row += f"'{cell_escaped}'"
            if j < len(row) - 1:
                js_row += ', '
        js_row += ']'
        if i < len(excel_data) - 1:
            js_row += ','
        js_array_lines.append(js_row)
    
    js_array_lines.append('];')
    js_array = '\n'.join(js_array_lines)
    
    # 找到数组开始和结束的位置
    array_start = template.find('const fullExcelData = [')
    array_end = template.find('];', array_start) + 2
    
    # 替换数组内容
    new_content = template[:array_start] + js_array + template[array_end:]
    
    # 更新注释中的行数
    new_content = new_content.replace('完整975行产品目录', f'完整{len(excel_data)}行产品目录')
    new_content = new_content.replace('975行完整Excel数据', f'{len(excel_data)}行完整Excel数据')
    
    # 保存新文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v9.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'已生成模块一v9文件: {output_path}')
    
    # 验证生成结果
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查数组行数
    array_start = content.find('const fullExcelData = [')
    array_end = content.find('];', array_start)
    array_content = content[array_start:array_end+2]
    
    # 计算有效的行数
    lines = array_content.split('\n')
    valid_rows = 0
    for line in lines:
        if line.strip().startswith('[') and line.strip().endswith(']'):
            valid_rows += 1
    
    print(f'生成文件中的有效行数: {valid_rows}')
    
    if valid_rows == len(excel_data):
        print('生成成功: 行数一致')
    else:
        print(f'生成失败: 期望{len(excel_data)}行，实际{valid_rows}行')
    
    return output_path

if __name__ == "__main__":
    output_file = create_correct_module1()
    
    if output_file:
        print(f'模块一文件修复完成: {output_file}')
        
        # 更新主页面链接
        with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
            index_content = f.read()
        
        # 替换模块一链接
        index_content = index_content.replace('module1_fixed_final_v6.html', 'module1_fixed_final_v9.html')
        
        with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print('主页面链接已更新为v9')