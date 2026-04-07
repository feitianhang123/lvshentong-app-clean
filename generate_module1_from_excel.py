import pandas as pd
import json

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

def generate_module1_html():
    """基于Excel文件生成模块一的HTML内容"""
    excel_data = read_excel_file()
    
    # 生成JavaScript数组
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
    
    # 读取模块一的模板
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 替换JavaScript部分
    # 查找generateFullExcelData函数
    func_start = template_content.find('function generateFullExcelData()')
    func_end = template_content.find('function searchProduct()', func_start)
    
    if func_start != -1 and func_end != -1:
        # 替换整个函数
        new_function = '''function generateFullExcelData() {
    return fullExcelData;
}
'''
        template_content = template_content[:func_start] + new_function + template_content[func_end:]
        
        # 在函数定义之前插入数组定义
        insert_pos = template_content.find('// 基于Excel文件实际内容的完整975行产品目录')
        if insert_pos != -1:
            insert_pos = template_content.find('const fullExcelData = generateFullExcelData();', insert_pos)
            if insert_pos != -1:
                # 删除原有的数组定义
                end_pos = template_content.find('\n', insert_pos)
                template_content = template_content[:insert_pos] + js_array + template_content[end_pos+1:]
    
    return template_content

if __name__ == "__main__":
    print("开始生成新的模块一文件...")
    
    # 生成新的HTML内容
    new_content = generate_module1_html()
    
    # 保存新文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v5.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"新的模块一文件已生成: {output_path}")
    print(f"Excel文件总行数: {len(read_excel_file())}")
    
    # 验证生成的内容
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if 'fullExcelData' in content:
            print("成功插入了Excel数据")
        else:
            print("警告: 可能没有正确插入Excel数据")