import pandas as pd
import re
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

# 读取Excel文件
df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
print(f'Excel文件总行数: {len(df)}')
print('Excel前5行内容:')
for i in range(5):
    row = []
    for j in range(4):
        value = df.iloc[i, j] if j < df.shape[1] else ''
        if pd.isna(value):
            value = ''
        row.append(str(value))
    print(f'第{i+1}行: {row}')

# 读取模块一文件
with open('android-project/app/src/main/assets/www/module1_fixed_final_v5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 检查是否包含完整的Excel数据
if 'fullExcelData' in content:
    print('\n模块一文件包含fullExcelData数组')
    
    # 检查数组长度
    array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
    if array_matches:
        array_content = array_matches[0]
        # 计算数组中的行数
        row_count = array_content.count('[')
        print(f'模块一中的数组行数: {row_count}')
        
        if row_count == len(df):
            print('✅ 模块一与Excel文件行数一致')
        else:
            print(f'❌ 行数不一致: Excel有{len(df)}行，模块一有{row_count}行')
else:
    print('❌ 模块一文件不包含fullExcelData数组')