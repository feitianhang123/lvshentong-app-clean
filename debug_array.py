import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
print(f'Excel文件总行数: {len(df)}')

# 读取模块一文件
with open('android-project/app/src/main/assets/www/module1_fixed_final_v8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到数组内容
array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
if array_matches:
    array_content = array_matches[0]
    
    # 分割成行
    lines = array_content.strip().split('\n')
    print(f'数组总行数: {len(lines)}')
    
    # 显示前10行
    print('\n前10行:')
    for i in range(min(10, len(lines))):
        print(f'第{i+1}行: {lines[i]}')
    
    # 显示最后10行
    print('\n最后10行:')
    for i in range(max(0, len(lines)-10), len(lines)):
        print(f'第{i+1}行: {lines[i]}')
    
    # 检查是否有空行或格式问题
    empty_lines = [i for i, line in enumerate(lines) if line.strip() == '']
    if empty_lines:
        print(f'发现空行: {empty_lines}')
    
    # 检查行格式
    valid_rows = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('[') and line.strip().endswith(']'):
            valid_rows += 1
        else:
            print(f'第{i+1}行格式异常: {line}')
    
    print(f'有效行数: {valid_rows}')
else:
    print('未找到fullExcelData数组')