def accurate_verify():
    # 读取模块一文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v15.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到数组开始和结束的位置
    array_start = content.find('const fullExcelData = [')
    array_end = content.find('];', array_start)
    
    print(f'Array start: {array_start}')
    print(f'Array end: {array_end}')
    
    if array_start == -1 or array_end == -1:
        print('未找到数组')
        return
    
    array_content = content[array_start:array_end+2]
    
    # 更准确的验证方法：统计所有以[开头以]结尾的行
    lines = array_content.split('\n')
    valid_rows = 0
    
    print('Checking lines...')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('[') and stripped.endswith(']'):
            valid_rows += 1
            if valid_rows <= 5:  # 只显示前5行
                print(f'Row {valid_rows}: {stripped[:50]}...')
    
    print(f'模块一文件中的有效行数: {valid_rows}')
    
    # 检查Excel文件行数
    import pandas as pd
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    excel_rows = len(df)
    print(f'Excel文件中的行数: {excel_rows}')
    
    if valid_rows == excel_rows:
        print('行数一致: 修复成功!')
    else:
        print(f'行数不一致: 期望{excel_rows}行，实际{valid_rows}行')
        
        # 显示数组的总行数
        print(f'Array total lines: {len(lines)}')
        
        # 显示数组的前后内容
        print('Array start content:')
        print(array_content[:500])
        print('Array end content:')
        print(array_content[-500:])

if __name__ == "__main__":
    accurate_verify()