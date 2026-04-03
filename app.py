from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# 加载Excel文件
def load_excel_data():
    try:
        # 读取Excel文件
        df = pd.read_excel('standards.xlsx')
        print(f"成功加载Excel文件，共{len(df)}行数据")
        print("列名:", df.columns.tolist())
        return df
    except Exception as e:
        print(f"加载Excel文件失败: {e}")
        return None

# 搜索产品
def search_product(product_name, df):
    try:
        results = []
        
        # 先尝试精确匹配产品名称列（第三列）
        product_col_index = 2  # 第三列
        standard_col_index = 1  # 第二列
        
        for index, row in df.iterrows():
            product_value = str(row.iloc[product_col_index]) if len(row) > product_col_index else ""
            standard_value = str(row.iloc[standard_col_index]) if len(row) > standard_col_index else ""
            
            # 跳过表头和空行
            if product_value == 'nan' or not product_value.strip() or '适用产品名称' in product_value:
                continue
            
            # 检查是否包含搜索词（不区分大小写）
            if product_name.lower() in product_value.lower():
                results.append({
                    'row': index + 2,  # Excel行号（从1开始计数）
                    'product': product_value,
                    'standard': standard_value,
                    'full_row': {k: str(v) for k, v in row.to_dict().items()}
                })
        
        return results
    except Exception as e:
        print(f"搜索出错: {e}")
        return []

@app.route('/')
def home():
    return '绿色食品申报通后端服务器已启动'

@app.route('/api/search')
def search():
    product_name = request.args.get('q', '').strip()
    if not product_name:
        return jsonify({'error': '请输入产品名称'})
    
    df = load_excel_data()
    if df is None:
        return jsonify({'error': '无法加载标准目录文件'})
    
    results = search_product(product_name, df)
    
    if results:
        return jsonify({
            'success': True,
            'count': len(results),
            'results': results,
            'message': f'找到{len(results)}个匹配产品'
        })
    else:
        return jsonify({
            'success': False,
            'message': '申报产品不在绿色食品使用标准目录内，暂时无法申报绿色食品。'
        })

@app.route('/api/excel-info')
def excel_info():
    df = load_excel_data()
    if df is None:
        return jsonify({'error': '无法加载Excel文件'})
    
    return jsonify({
        'row_count': len(df),
        'columns': df.columns.tolist(),
        'first_few_rows': df.head().to_dict('records')
    })

if __name__ == '__main__':
    print("正在启动绿色食品申报通后端服务器...")
    print("尝试加载Excel文件...")
    
    # 检查文件是否存在
    if os.path.exists('standards.xlsx'):
        print("找到standards.xlsx文件")
        df = load_excel_data()
        if df is not None:
            print("Excel文件加载成功！")
        else:
            print("Excel文件加载失败")
    else:
        print("未找到standards.xlsx文件")
    
    print("服务器启动在 http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)