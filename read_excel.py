import pandas as pd
import json

def read_excel_file():
    """读取Excel文件并返回内容"""
    try:
        # 读取Excel文件
        df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
        
        # 获取总行数
        total_rows = len(df)
        
        # 获取前几行数据
        data = []
        for i in range(min(total_rows, 100)):  # 只读取前100行
            row_data = []
            for col in range(4):  # ABCD列
                value = df.iloc[i, col] if col < df.shape[1] else ''
                if pd.isna(value):
                    value = ''
                row_data.append(str(value))
            data.append(row_data)
        
        return {
            'total_rows': total_rows,
            'data': data,
            'columns': ['A', 'B', 'C', 'D']
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    result = read_excel_file()
    print(json.dumps(result, ensure_ascii=False, indent=2))