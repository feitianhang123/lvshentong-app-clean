import pandas as pd

def create_simple_module1():
    # 读取新的xlsx文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023 版）无标题_1775534555928_0c408e.xlsx', header=None)
    
    print(f"Excel文件总行数: {len(df)}")
    
    # 创建简单的HTML文件
    html_content = f'''<!DOCTYPE html>
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
        
        .directory-view {{
            padding: 20px;
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
        
        .footer {{
            background: #f5f5f5;
            padding: 15px 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
            border-top: 1px solid #eee;
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
        // Excel数据（直接嵌入）
        const excelData = '''
    
    # 添加表格内容
    html_content += '<table class="directory-table">'
    html_content += '<thead><tr><th>A列</th><th>B列</th><th>C列</th><th>D列</th></tr></thead><tbody>'
    
    # 添加所有Excel数据
    for i in range(len(df)):
        html_content += '<tr>'
        for col in range(df.shape[1]):
            value = df.iloc[i, col]
            if pd.isna(value):
                value = ''
            else:
                value = str(value)
            html_content += f'<td>{value}</td>'
        html_content += '</tr>'
    
    html_content += '</tbody></table>'
    
    # 添加JavaScript部分
    html_content += '''
    </script>

    <script>
        // 搜索产品
        function searchProduct() {
            const productName = document.getElementById('productInput').value.trim();
            
            if (!productName) {
                alert('请输入产品名称');
                return;
            }
            
            const resultSection = document.getElementById('resultSection');
            const directoryView = document.getElementById('directoryView');
            
            resultSection.style.display = 'block';
            directoryView.style.display = 'none';
            
            // 搜索产品（从第2行开始搜索，跳过标题行）
            const table = document.querySelector('.directory-table');
            const rows = table.querySelectorAll('tr');
            const foundProducts = [];
            
            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].querySelectorAll('td');
                if (cells.length >= 3) {
                    const productNameInTable = cells[2].textContent.trim();
                    if (productNameInTable && 
                        productNameInTable.toLowerCase().includes(productName.toLowerCase())) {
                        
                        foundProducts.push({
                            name: productNameInTable,
                            standard: cells[1].textContent.trim(),
                            description: cells[3].textContent.trim(),
                            rowNumber: i + 1
                        });
                    }
                }
            }
            
            if (foundProducts.length > 0) {
                let resultsHTML = '<h3>搜索结果：</h3>';
                foundProducts.forEach(product => {
                    resultsHTML += `
                        <div class="result-item">
                            <div class="result-title">${product.name}</div>
                            <div class="result-details">
                                <strong>标准：</strong>${product.standard}<br>
                                <strong>说明：</strong>${product.description}<br>
                                <strong>行号：</strong>第${product.rowNumber}行
                            </div>
                        </div>
                    `;
                });
                document.getElementById('searchResults').innerHTML = resultsHTML;
            } else {
                document.getElementById('searchResults').innerHTML = 
                    '<div class="result-item"><div class="result-title">未找到匹配的产品</div></div>';
            }
        }

        // 页面加载完成
        console.log('模块一页面加载完成，包含{len(df)}行完整Excel数据');
    </script>
</body>
</html>'''
    
    # 保存文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v28.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'已生成简单模块一v28文件: {output_path}')
    print(f'Excel文件行数: {len(df)}')
    
    # 更新主页面链接
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 替换模块一链接
    index_content = index_content.replace('module1_fixed_final_v27.html', 'module1_fixed_final_v28.html')
    
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print('主页面链接已更新为v28')

if __name__ == "__main__":
    create_simple_module1()