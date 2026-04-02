import pandas as pd
import json

# 读取Excel文件
excel_file = "android-project/app/src/main/assets/www/greenfood_standards_2023.xlsx"

# 读取第一个工作表
df = pd.read_excel(excel_file)

# 清理数据：去除NaN值，转换为字符串
df = df.fillna('')
df = df.astype(str)

# 转换为JSON格式
json_data = []
for index, row in df.iterrows():
    row_data = {
        "row": index + 1,
        "col1": row.iloc[0] if len(row) > 0 else '',
        "col2": row.iloc[1] if len(row) > 1 else '',
        "col3": row.iloc[2] if len(row) > 2 else '',
        "col4": row.iloc[3] if len(row) > 3 else ''
    }
    json_data.append(row_data)

# 保存为JSON文件
json_file = "android-project/app/src/main/assets/www/complete_excel.json"
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"Excel文件已成功转换为JSON，共 {len(json_data)} 行数据")
print(f"JSON文件保存位置: {json_file}")