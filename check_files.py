import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
print(f'Excel文件总行数: {len(df)}')

# 检查模块一文件
with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 检查数组行数
array_matches = re.findall(r'const fullExcelData = \[(.*?)\];', content, re.DOTALL)
if array_matches:
    array_content = array_matches[0]
    row_count = array_content.count('[')
    print(f'模块一v6中的数组行数: {row_count}')
    
    if row_count == len(df):
        print('模块一与Excel文件行数一致')
    else:
        print(f'行数不一致: Excel有{len(df)}行，模块一有{row_count}行')
else:
    print('未找到fullExcelData数组')

# 检查主页面链接
with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

if "module1_fixed_final_v5.html" in index_content:
    print('主页面模块一链接已更新为v5')
else:
    print('主页面模块一链接未更新')

# 检查UI样式一致性
if 'background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);' in index_content:
    print('主页面头部样式正确')
else:
    print('主页面头部样式可能有问题')

if 'background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);' in content:
    print('模块一头部样式正确') 
else:
    print('模块一头部样式可能有问题')