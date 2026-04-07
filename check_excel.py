import pandas as pd

df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
print(f'Excel行数: {len(df)}')
print('前5行:')
for i in range(5):
    row = []
    for col in range(4):
        value = df.iloc[i, col] if col < df.shape[1] else ''
        if pd.isna(value):
            value = ''
        row.append(str(value))
    print(row)