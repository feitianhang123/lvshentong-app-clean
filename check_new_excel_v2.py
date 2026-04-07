import pandas as pd

def check_new_excel():
    # 读取新的xlsx文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023 版）无标题_1775534555928_0c408e.xlsx', header=None)
    
    print("新Excel文件基本信息：")
    print(f"总行数: {len(df)}")
    print(f"总列数: {df.shape[1]}")
    
    print("\n前20行内容预览：")
    for i in range(min(20, len(df))):
        row_data = []
        for col in range(df.shape[1]):
            value = df.iloc[i, col]
            if pd.isna(value):
                value = ''
            else:
                value = str(value)
            row_data.append(value)
        print(f"行{i+1}: {row_data}")
    
    print("\n列名检查：")
    print(f"第1行内容: {list(df.iloc[0]) if len(df) > 0 else '空文件'}")
    
    # 检查数据完整性
    non_empty_rows = 0
    for i in range(len(df)):
        row_has_data = False
        for col in range(df.shape[1]):
            if not pd.isna(df.iloc[i, col]) and str(df.iloc[i, col]).strip():
                row_has_data = True
                break
        if row_has_data:
            non_empty_rows += 1
    
    print(f"\n包含数据的行数: {non_empty_rows}")
    
    # 保存前100行数据用于测试
    sample_data = []
    for i in range(min(100, len(df))):
        row_data = []
        for col in range(df.shape[1]):
            value = df.iloc[i, col]
            if pd.isna(value):
                value = ''
            else:
                value = str(value)
            row_data.append(value)
        sample_data.append(row_data)
    
    return df, sample_data

if __name__ == "__main__":
    df, sample_data = check_new_excel()