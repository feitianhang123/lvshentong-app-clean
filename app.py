from flask import Flask, request, jsonify
import pandas as pd
import os
import json

app = Flask(__name__)

# 加载JSON数据
def load_json_data():
    try:
        json_file = 'android-project/app/src/main/assets/www/complete_excel.json'
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"成功加载JSON文件，共{len(data)}行数据")
        return data
    except Exception as e:
        print(f"加载JSON文件失败: {e}")
        return None

# 搜索产品
def search_product(product_name, data):
    try:
        results = []
        
        for item in data:
            product_value = item.get('col3', '')  # 第三列是产品名称
            standard_value = item.get('col2', '')  # 第二列是标准名称
            
            # 跳过表头和空行
            if product_value == 'nan' or not product_value.strip() or '适用产品名称' in product_value:
                continue
            
            # 检查是否包含搜索词（不区分大小写）
            if product_name.lower() in product_value.lower():
                results.append({
                    'row': item.get('row', 0),
                    'product': product_value,
                    'standard': standard_value,
                    'full_row': item
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
    
    data = load_json_data()
    if data is None:
        return jsonify({'error': '无法加载标准目录文件'})
    
    results = search_product(product_name, data)
    
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
    data = load_json_data()
    if data is None:
        return jsonify({'error': '无法加载JSON文件'})
    
    return jsonify({
        'row_count': len(data),
        'columns': ['col1', 'col2', 'col3', 'col4'],
        'first_few_rows': data[:5]
    })

if __name__ == '__main__':
    print("正在启动绿色食品申报通后端服务器...")
    print("尝试加载JSON数据...")
    
    # 检查文件是否存在
    json_file = 'android-project/app/src/main/assets/www/complete_excel.json'
    if os.path.exists(json_file):
        print("找到JSON文件")
        data = load_json_data()
        if data is not None:
            print("JSON文件加载成功！")
        else:
            print("JSON文件加载失败")
    else:
        print("未找到JSON文件")
    
    print("服务器启动在 http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)