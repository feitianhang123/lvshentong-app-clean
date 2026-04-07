import pandas as pd

def check_excel_content():
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    print('Excel文件前10行:')
    for i in range(min(10, len(df))):
        row_data = []
        for col in range(4):
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            row_data.append(value)
        print(f'行{i+1}: {row_data}')
    
    print(f'\nExcel文件总行数: {len(df)}')
    print(f'Excel文件列数: {df.shape[1]}')

if __name__ == "__main__":
    check_excel_content()