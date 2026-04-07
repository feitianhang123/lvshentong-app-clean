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

def generate_correct_module1():
    """生成正确的模块一文件"""
    excel_data = read_excel_file()
    print(f'Excel文件总行数: {len(excel_data)}')
    
    # 读取模块一的模板文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 生成正确的JavaScript数组
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
    
    # 查找并替换generateFullExcelData函数
    func_start = template_content.find('function generateFullExcelData()')
    if func_start != -1:
        func_end = template_content.find('function searchProduct()', func_start)
        if func_end != -1:
            # 替换整个函数
            new_function = '''function generateFullExcelData() {
    return fullExcelData;
}
'''
            template_content = template_content[:func_start] + new_function + template_content[func_end:]
    
    # 查找并替换数组定义
    # 查找注释位置
    comment_pos = template_content.find('// 基于Excel文件实际内容的完整975行产品目录')
    if comment_pos != -1:
        # 查找const fullExcelData的位置
        array_start = template_content.find('const fullExcelData = generateFullExcelData();', comment_pos)
        if array_start != -1:
            array_end = template_content.find('\n', array_start)
            # 替换数组定义
            template_content = template_content[:array_start] + js_array + template_content[array_end+1:]
    
    # 更新注释中的行数
    template_content = template_content.replace('完整975行产品目录', f'完整{len(excel_data)}行产品目录')
    template_content = template_content.replace('975行完整Excel数据', f'{len(excel_data)}行完整Excel数据')
    
    # 保存新文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v9.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print(f'已生成模块一v9文件: {output_path}')
    
    # 验证生成结果
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 检查数组行数
    array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
    if array_matches:
        array_content = array_matches[0]
        # 计算有效的行数（以[开头的行）
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
    else:
        print('未找到fullExcelData数组')
    
    return output_path

if __name__ == "__main__":
    output_file = generate_correct_module1()
    print(f'模块一文件生成完成: {output_file}')
    
    # 更新主页面链接
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 替换模块一链接
    index_content = index_content.replace('module1_fixed_final_v6.html', 'module1_fixed_final_v9.html')
    
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print('主页面链接已更新为v9')