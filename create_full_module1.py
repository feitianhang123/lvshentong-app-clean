import pandas as pd
import json

def create_full_module1():
    # 读取Excel文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023 版）无标题_1775534555928_0c408e.xlsx', header=None)
    
    print(f"Excel文件总行数: {len(df)}")
    
    # 生成JavaScript数组
    js_array_lines = []
    js_array_lines.append('const excelData = [')
    
    for i in range(len(df)):
        row = []
        for col in range(df.shape[1]):
            value = df.iloc[i, col]
            if pd.isna(value):
                value = ''
            else:
                # 处理特殊字符
                value = str(value).replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"').replace("'", "\\'")
            row.append(value)
        
        # 生成JavaScript数组行
        js_row = f"    ['{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}']"
        if i < len(df) - 1:
            js_row += ','
        js_array_lines.append(js_row)
    
    js_array_lines.append('];')
    js_array = '\n'.join(js_array_lines)
    
    # 创建HTML模板
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>产品目录 - 绿色食品申报通</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%); 
            min-height: 100vh; 
            padding: 2%;
            color: #333;
        }}
        
        .container {{ 
            max-width: 95%; 
            width: 900px;
            margin: 0 auto; 
            background: white; 
            border-radius: 25px; 
            box-shadow: 0 10px 30px rgba(76, 175, 80, 0.15);
            overflow: hidden;
        }}
        
        .header {{ 
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%); 
            color: white; 
            padding: 30px; 
            text-align: center; 
        }}
        
        .main-title {{
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .sub-title {{
            font-size: 16px;
            opacity: 0.9;
        }}
        
        .search-section {{
            padding: 20px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .search-box {{
            display: flex;
            gap: 10px;
            max-width: 500px;
            margin: 0 auto;
        }}
        
        .search-input {{
            flex: 1;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
        }}
        
        .search-btn {{
            padding: 12px 25px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
        }}
        
        .search-btn:hover {{
            background: #45a049;
        }}
        
        .card-section {{
            padding: 20px;
        }}
        
        .directory-card {{
            background: #f8fff8;
            border: 2px solid #4CAF50;
            border-radius: 12px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 20px;
        }}
        
        .directory-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.2);
        }}
        
        .card-title {{
            font-size: 18px;
            font-weight: bold;
            color: #2e7d32;
            margin-bottom: 10px;
        }}
        
        .card-desc {{
            font-size: 14px;
            color: #666;
        }}
        
        .directory-view {{
            padding: 20px;
            display: none;
            max-height: 500px;
            overflow-y: auto;
        }}
        
        .directory-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }}
        
        .directory-table th {{
            background: #f5f5f5;
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
            font-weight: bold;
        }}
        
        .directory-table td {{
            padding: 8px;
            border: 1px solid #ddd;
            vertical-align: top;
        }}
        
        .directory-table tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        
        .result-section {{
            padding: 20px;
            display: none;
        }}
        
        .result-item {{
            background: #f8fff8;
            border: 1px solid #e8f5e8;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        
        .result-title {{
            font-weight: bold;
            color: #2e7d32;
            margin-bottom: 5px;
        }}
        
        .result-details {{
            font-size: 12px;
            color: #666;
        }}
        
        .footer {{
            background: #f5f5f5;
            padding: 15px 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
            border-top: 1px solid #eee;
        }}
        
        @media (max-width: 600px) {{
            .container {{ border-radius: 15px; margin: 0 auto; }}
            .header {{ padding: 20px; }}
            .main-title {{ font-size: 20px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="main-title">产品目录</div>
            <div class="sub-title">绿色食品产品适用标准目录（2023版）</div>
        </div>
        
        <div class="search-section">
            <div class="search-box">
                <input type="text" id="productInput" class="search-input" placeholder="请输入产品名称...">
                <button class="search-btn" onclick="searchProduct()">搜索</button>
            </div>
        </div>
        
        <div class="card-section">
            <div class="directory-card" onclick="showDirectory()">
                <div class="card-title">绿色食品产品适用标准目录（2023版）</div>
                <div class="card-desc">点击查看完整的标准目录内容</div>
            </div>
        </div>
        
        <div class="result-section" id="resultSection">
            <div id="searchResults"></div>
        </div>
        
        <div class="directory-view" id="directoryView">
            <div id="directoryTable"></div>
        </div>
        
        <div class="footer">
            <div>本软件内容均来源于中国绿色食品发展中心官网</div>
            <div>如果存在问题请联络作者：QQ:10780329</div>
        </div>
    </div>

    <script>
        // Excel数据（完整的{len(df)}行数据）
        {js_array}

        // 搜索产品
        function searchProduct() {{
            const productName = document.getElementById('productInput').value.trim();
            
            if (!productName) {{
                alert('请输入产品名称');
                return;
            }}
            
            const resultSection = document.getElementById('resultSection');
            const directoryView = document.getElementById('directoryView');
            
            resultSection.style.display = 'block';
            directoryView.style.display = 'none';
            
            // 搜索产品（从第2行开始搜索，跳过标题行）
            const foundProducts = [];
            for (let i = 2; i < excelData.length; i++) {{
                const row = excelData[i];
                if (row && row.length >= 3 && row[2]) {{
                    const productNameInExcel = row[2].toString().trim();
                    if (productNameInExcel && 
                        productNameInExcel.toLowerCase().includes(productName.toLowerCase())) {{
                        
                        foundProducts.push({{
                            name: productNameInExcel,
                            rowNumber: i + 1,
                            standard: row[1] || '',
                            description: row[3] || '',
                            originalRow: row
                        }});
                    }}
                }}
            }}
            
            if (foundProducts.length > 0) {{
                let resultsHTML = '<h3>搜索结果：</h3>';
                foundProducts.forEach(product => {{
                    resultsHTML += `
                        <div class="result-item">
                            <div class="result-title">${{product.name}}</div>
                            <div class="result-details">
                                <strong>标准：</strong>${{product.standard}}<br>
                                <strong>说明：</strong>${{product.description}}<br>
                                <strong>行号：</strong>第${{product.rowNumber}}行
                            </div>
                        </div>
                    `;
                }});
                document.getElementById('searchResults').innerHTML = resultsHTML;
            }} else {{
                document.getElementById('searchResults').innerHTML = 
                    '<div class="result-item"><div class="result-title">申报产品不在绿色食品使用标准目录内，暂时无法申报绿色食品。</div></div>';
            }}
        }}

        // 显示目录
        function showDirectory() {{
            const resultSection = document.getElementById('resultSection');
            const directoryView = document.getElementById('directoryView');
            
            resultSection.style.display = 'none';
            directoryView.style.display = 'block';
            
            let directoryHTML = '<h3>绿色食品产品适用标准目录（2023版）</h3>';
            directoryHTML += '<table class="directory-table">';
            directoryHTML += '<thead><tr><th>A列</th><th>B列</th><th>C列</th><th>D列</th></tr></thead><tbody>';
            
            // 显示所有数据
            excelData.forEach((row, index) => {{
                directoryHTML += '<tr>';
                for (let i = 0; i < 4; i++) {{
                    directoryHTML += `<td>${{row[i] || ''}}</td>`;
                }}
                directoryHTML += '</tr>';
            }});
            
            directoryHTML += '</tbody></table>';
            directoryHTML += '<p>完整数据包含{len(df)}行，与源Excel文件完全一致</p>';
            document.getElementById('directoryTable').innerHTML = directoryHTML;
        }}

        // 页面加载完成
        console.log('模块一页面加载完成，包含{len(df)}行完整Excel数据');
    </script>
</body>
</html>'''
    
    # 保存文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v31.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f'已生成完整模块一v31文件: {output_path}')
    print(f'Excel文件行数: {len(df)}')
    
    return output_path

if __name__ == "__main__":
    output_file = create_full_module1()