def simple_verify():
    # 读取模块一文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v16.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单的验证方法：统计[出现的次数
    count_brackets = content.count('[')
    count_closing_brackets = content.count(']')
    
    print(f'Opening brackets count: {count_brackets}')
    print(f'Closing brackets count: {count_closing_brackets}')
    
    # 每个有效的数组行应该有2个括号（一个[和一个]）
    # 减去数组定义本身的1对括号
    estimated_rows = (count_brackets - 1) // 2
    
    print(f'Estimated rows: {estimated_rows}')
    
    # 检查Excel文件行数
    import pandas as pd
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    excel_rows = len(df)
    print(f'Excel文件中的行数: {excel_rows}')
    
    if estimated_rows == excel_rows:
        print('行数一致: 修复成功!')
    else:
        print(f'行数不一致: 期望{excel_rows}行，实际{estimated_rows}行')

if __name__ == "__main__":
    simple_verify()