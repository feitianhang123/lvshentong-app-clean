import pandas as pd

def verify_content():
    # 读取Excel文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    excel_data = []
    for i in range(len(df)):
        row_data = []
        for col in range(4):
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            else:
                value = str(value)
            row_data.append(value)
        excel_data.append(row_data)
    
    print(f'Excel文件行数: {len(excel_data)}')
    
    # 读取模块一文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v19.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查数组内容
    array_start = content.find('const fullExcelData = [')
    array_end = content.find('];', array_start)
    
    if array_start == -1 or array_end == -1:
        print('未找到数组')
        return
    
    array_content = content[array_start:array_end+2]
    
    # 计算有效的行数
    lines = array_content.split('\n')
    valid_rows = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('[') and stripped.endswith(']'):
            valid_rows += 1
    
    print(f'模块一文件中的有效行数: {valid_rows}')
    
    # 比较前10行内容
    print('\n前10行内容比较:')
    print('Excel文件前10行:')
    for i in range(min(10, len(excel_data))):
        print(f'行{i+1}: {excel_data[i]}')
    
    # 检查模块一文件的前10行
    print('\n模块一文件前10行:')
    for i in range(min(10, len(lines))):
        line = lines[i]
        if line.strip().startswith('['):
            print(f'行{i+1}: {line.strip()}')
    
    # 检查文件大小
    import os
    file_size = os.path.getsize('android-project/app/src/main/assets/www/module1_fixed_final_v19.html')
    print(f'\n模块一文件大小: {file_size} bytes')
    
    if valid_rows == len(excel_data):
        print('行数一致: 内容匹配成功!')
    else:
        print(f'行数不一致: 期望{len(excel_data)}行，实际{valid_rows}行')

if __name__ == "__main__":
    verify_content()