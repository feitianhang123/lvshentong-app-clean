import pandas as pd

def create_exact_module1():
    # 读取Excel文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    
    # 生成HTML文件模板
    template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>产品目录 - 绿色食品申报通</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%); 
            min-height: 100vh; 
            padding: 2%;
            color: #333;
        }
        
        .container { 
            max-width: 95%; 
            width: 900px;
            margin: 0 auto; 
            background: white; 
            border-radius: 25px; 
            box-shadow: 0 10px 30px rgba(76, 175, 80, 0.15);
            overflow: hidden;
        }
        
        .header { 
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
            color: white; 
            padding: 30px 20px; 
            text-align: center; 
        }
        
        .main-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        
        .sub-title {
            font-size: 16px;
            opacity: 0.9;
        }
        
        .search-section {
            padding: 20px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }
        
        .search-box {
            display: flex;
            gap: 10px;
            max-width: 500px;
            margin: 0 auto;
        }
        
        .search-input {
            flex: 1;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
        }
        
        .search-btn {
            padding: 12px 25px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
        }
        
        .search-btn:hover {
            background: #45a049;
        }
        
        .result-section {
            padding: 20px;
            display: none;
        }
        
        .result-item {
            background: #f8fff8;
            border: 1px solid #e8f5e8;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
        }
        
        .result-title {
            font-weight: bold;
            color: #2e7d32;
            margin-bottom: 5px;
        }
        
        .result-details {
            font-size: 12px;
            color: #666;
        }
        
        .directory-view {
            padding: 20px;
            display: none;
        }
        
        .directory-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
        }
        
        .directory-table th {
            background: #f5f5f5;
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
            font-weight: bold;
        }
        
        .directory-table td {
            padding: 8px;
            border: 1px solid #ddd;
            vertical-align: top;
        }
        
        .directory-table tr:nth-child(even) {
            background: #f9f9f9;
        }
        
        .view-toggle {
            text-align: center;
            padding: 15px;
            background: #f8f9fa;
        }
        
        .toggle-btn {
            padding: 8px 20px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 0 5px;
        }
        
        .toggle-btn:hover {
            background: #45a049;
        }
        
        .toggle-btn.active {
            background: #2e7d32;
        }
        
        .footer {
            background: #f5f5f5;
            padding: 15px 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
            border-top: 1px solid #eee;
        }
        
        .footer a {
            color: #4CAF50;
            text-decoration: none;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
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
        
        <div class="view-toggle">
            <button class="toggle-btn active" onclick="showSearchView()">搜索模式</button>
            <button class="toggle-btn" onclick="showFullDirectory()">完整目录</button>
        </div>
        
        <div class="footer">
            <div>本软件内容均来源于中国绿色食品发展中心官网</div>
            <div>如果存在问题请联络作者：QQ:10780329</div>
        </div>
    </div>

    <script>
        // 基于Excel文件实际内容的完整976行产品目录
        const fullExcelData = '''
    
    # 生成JavaScript数组
    js_array = '['
    for i in range(len(df)):
        row_data = '['
        for col in range(4):  # ABCD列
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            else:
                value = str(value).replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"').replace("'", "\\'")
            row_data += f"'{value}'"
            if col < 3:
                row_data += ', '
        row_data += ']'
        if i < len(df) - 1:
            row_data += ','
        js_array += '\n            ' + row_data
    js_array += '\n        ];'
    
    # 生成JavaScript函数
    js_functions = '''
        // 生成完整的976行Excel数据（基于实际文件内容）
        function generateFullExcelData() {
            return fullExcelData;
        }

        // 搜索产品
        function searchProduct() {
            const productName = document.getElementById('productInput').value.trim();
            
            if (!productName) {
                alert('请输入产品名称');
                return;
            }
            
            const resultSection = document.getElementById('resultSection');
            resultSection.style.display = 'block';
            
            // 搜索产品（从第3行开始搜索，跳过标题行）
            const foundProducts = [];
            for (let i = 2; i < fullExcelData.length; i++) {
                const row = fullExcelData[i];
                if (row && row.length >= 3 && row[2]) { // 检查C列（适用产品名称）
                    const productNameInExcel = row[2].toString().trim();
                    if (productNameInExcel && 
                        productNameInExcel.toLowerCase().includes(productName.toLowerCase())) {
                        
                        // 找到对应的标准名称（向上查找非空值）
                        let standardName = row[1] || '';
                        let rowNum = i;
                        while (!standardName && rowNum > 2) {
                            rowNum--;
                            const prevRow = fullExcelData[rowNum];
                            if (prevRow && prevRow[1]) {
                                standardName = prevRow[1];
                                break;
                            }
                        }
                        
                        foundProducts.push({
                            name: productNameInExcel,
                            rowNumber: i + 1, // Excel行号（1-based）
                            standard: standardName,
                            description: row[3] || '',
                            originalRow: row
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

        // 显示搜索视图
        function showSearchView() {
            document.querySelector('.search-section').style.display = 'block';
            document.getElementById('resultSection').style.display = 'none';
            document.getElementById('directoryView').style.display = 'none';
            
            // 更新按钮状态
            document.querySelectorAll('.toggle-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }

        // 显示完整目录
        function showFullDirectory() {
            document.querySelector('.search-section').style.display = 'none';
            document.getElementById('resultSection').style.display = 'none';
            document.getElementById('directoryView').style.display = 'block';
            
            let directoryHTML = '<table class="directory-table">';
            directoryHTML += '<thead><tr><th>A列</th><th>B列</th><th>C列</th><th>D列</th></tr></thead><tbody>';
            
            // 显示所有976行数据
            fullExcelData.forEach((row, index) => {
                directoryHTML += '<tr>';
                for (let i = 0; i < 4; i++) {
                    directoryHTML += `<td>${row[i] || ''}</td>`;
                }
                directoryHTML += '</tr>';
            });
            
            directoryHTML += '</tbody></table>';
            document.getElementById('directoryTable').innerHTML = directoryHTML;
            
            // 更新按钮状态
            document.querySelectorAll('.toggle-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }

        // 页面加载完成
        console.log('模块一页面加载完成，包含976行完整Excel数据');
        console.log('Excel数据总量:', fullExcelData.length);
        console.log('ABCD列对应关系：');
        console.log('A列：序号（包括合并单元格）');
        console.log('B列：标准名称（包括合并单元格）');
        console.log('C列：适用产品名称');
        console.log('D列：适用产品名称说明');
        
        // 初始化显示搜索视图
        showSearchView();
    </script>
</body>
</html>'''
    
    # 组合完整的HTML文件
    full_html = template + js_array + js_functions
    
    # 保存文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v21.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f'已生成准确模块一v21文件: {output_path}')
    print(f'Excel文件行数: {len(df)}')
    
    # 验证生成结果
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查数组行数
    array_start = content.find('const fullExcelData = [')
    array_end = content.find('];', array_start)
    
    if array_start == -1 or array_end == -1:
        print('未找到数组')
        return None
    
    array_content = content[array_start:array_end+2]
    
    # 计算有效的行数
    lines = array_content.split('\n')
    valid_rows = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('[') and stripped.endswith(']'):
            valid_rows += 1
    
    print(f'生成文件中的有效行数: {valid_rows}')
    
    if valid_rows == len(df):
        print('生成成功: 行数一致')
    else:
        print(f'生成失败: 期望{len(df)}行，实际{valid_rows}行')
    
    return output_path

if __name__ == "__main__":
    output_file = create_exact_module1()
    
    if output_file:
        print(f'准确模块一文件生成完成: {output_file}')
        
        # 更新主页面链接
        with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
            index_content = f.read()
        
        # 替换模块一链接
        index_content = index_content.replace('module1_fixed_final_v19.html', 'module1_fixed_final_v21.html')
        
        with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print('主页面链接已更新为v21')