import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
print(f'Excel文件总行数: {len(df)}')

# 读取模块一文件
with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到数组内容
array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
if array_matches:
    array_content = array_matches[0]
    
    # 计算行数
    row_count = array_content.count('[')
    print(f'当前模块一数组行数: {row_count}')
    
    # 如果行数不一致，修复数组
    if row_count != len(df):
        print(f'需要修复: 期望{len(df)}行，实际{row_count}行')
        
        # 重新生成正确的数组
        excel_data = []
        for i in range(len(df)):
            row_data = []
            for col in range(4):  # ABCD列
                value = df.iloc[i, col] if col < df.shape[1] else ''
                if pd.isna(value):
                    value = ''
                row_data.append(str(value))
            excel_data.append(row_data)
        
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
        
        # 替换数组
        new_content = re.sub(r'const fullExcelData = \[.*?\];', js_array, content, flags=re.DOTALL)
        
        # 保存修复后的文件
        with open('android-project/app/src/main/assets/www/module1_fixed_final_v7.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print('已生成修复后的模块一v7文件')
        
        # 验证修复结果
        with open('android-project/app/src/main/assets/www/module1_fixed_final_v7.html', 'r', encoding='utf-8') as f:
            new_content_check = f.read()
            
        array_matches_new = re.findall(r'const fullExcelData = \[(.*?)\];', new_content_check, re.DOTALL)
        if array_matches_new:
            array_content_new = array_matches_new[0]
            row_count_new = array_content_new.count('[')
            print(f'修复后模块一数组行数: {row_count_new}')
            
            if row_count_new == len(df):
                print('✅ 修复成功: 行数一致')
            else:
                print('❌ 修复失败: 行数仍不一致')
    else:
        print('✅ 模块一行数正确，无需修复')
else:
    print('❌ 未找到fullExcelData数组')