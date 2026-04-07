def verify_module1():
    # 读取模块一文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v14.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到数组
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
        if line.strip().startswith('[') and line.strip().endswith(']'):
            valid_rows += 1
    
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

if __name__ == "__main__":
    verify_module1()