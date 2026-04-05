import pandas as pd
import json

try:
    # 读取Excel文件
    df = pd.read_excel('green_food_standards.xlsx')
    
    print("Excel文件形状:", df.shape)
    print("\n列名:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {repr(col)}")
    
    print("\n前10行数据:")
    print(df.head(10))
    
    print("\n数据信息:")
    print(df.info())
    
    # 检查是否有中文编码问题
    print("\n尝试检测编码:")
    for col in df.columns:
        if 'Unnamed' not in str(col):
            print(f"主要列: {col}")
            
    # 保存为JSON以便查看
    df.head(20).to_json('excel_sample.json', force_ascii=False, orient='records')
    print("\n已保存样本数据到 excel_sample.json")
    
except Exception as e:
    print(f"错误: {e}")
    print("尝试使用不同的编码...")
    
    try:
        df = pd.read_excel('green_food_standards.xlsx', header=None)
        print("\n无标题读取:")
        print(df.head(10))
    except Exception as e2:
        print(f"再次错误: {e2}")