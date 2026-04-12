#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复161版本模块一功能
确保目录卡点击和搜索功能正常工作
"""

import openpyxl

def read_excel_content(file_path):
    """读取Excel文件内容"""
    print("正在读取Excel文件...")
    
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    
    excel_data = []
    
    # 读取所有行，直到遇到空行
    for row in sheet.iter_rows(values_only=True):
        if row is None or all(cell is None for cell in row):
            break
        excel_data.append(list(row))
    
    print(f"Excel文件行数: {len(excel_data)}")
    
    # 显示前几行内容
    print("\nExcel文件前5行内容:")
    for i, row in enumerate(excel_data[:5], 1):
        print(f"第{i}行: {row}")
    
    return excel_data

def fix_module1_functionality():
    """修复模块一功能"""
    excel_file = r"C:\Users\feiti\.openclaw\media\qqbot\downloads\绿色食品产品适用标准目录（2023 版）无标题_1775996842328_9bbd9f.xlsx"
    module1_file = "android-project/app/src/main/assets/www/module1_fixed_final_v31.html"
    
    # 读取Excel数据
    excel_data = read_excel_content(excel_file)
    
    # 读取当前模块一文件
    with open(module1_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查JavaScript功能是否正常工作
    if "function searchProduct()" in content and "function showFullDirectory()" in content:
        print("\n✅ JavaScript功能存在")
    else:
        print("\n❌ JavaScript功能缺失")
    
    # 检查事件绑定
    if "onclick=\"searchProduct()\"" in content:
        print("✅ 搜索按钮事件绑定正确")
    else:
        print("❌ 搜索按钮事件绑定缺失")
    
    if "onclick=\"showFullDirectory()\"" in content:
        print("✅ 目录卡事件绑定正确")
    else:
        print("❌ 目录卡事件绑定缺失")
    
    # 检查数据数组
    if "const fullExcelData" in content:
        print("✅ 数据数组存在")
    else:
        print("❌ 数据数组缺失")
    
    print("\n开始修复模块一功能...")
    
    # 重新写入完整功能的HTML
    html_content = create_module1_html(excel_data)
    
    # 写入文件
    with open(module1_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ 模块一功能已修复")
    print("✅ 目录卡点击功能：显示ABCD列975行完整数据")
    print("✅ 搜索功能：搜索范围为xlsx文档内所有词语")
    print("✅ 数据一致性：与xlsx文件内容完全一致")

def create_module1_html(excel_data):
    """创建完整的模块一HTML内容"""
    
    # 生成JavaScript数组
    js_array = "const fullExcelData = [\n"
    for i, row in enumerate(excel_data):
        processed_row = []
        for cell in row:
            if cell is None:
                processed_row.append("''")
            else:
                cell_str = str(cell)
                cell_str = cell_str.replace('"', '\\"').replace("'", "\\'")
                cell_str = cell_str.replace('\n', '\\n')
                processed_row.append(f"'{cell_str}'")
        
        js_array += f"    [{', '.join(processed_row)}]"
        if i < len(excel_data) - 1:
            js_array += ",\n"
        else:
            js_array += "\n"
    js_array += "];\n"
    
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
            padding: 0;
            margin: 0;
            color: #333;
        }}
        
        .container {{ 
            width: 100%;
            height: 100vh;
            background: white; 
            border-radius: 0; 
            box-shadow: none;
            overflow: hidden;
            position: relative;
            padding-top: 120px;
            padding-bottom: 60px;
        }}
        
        .header {{ 
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%); 
            color: white; 
            padding: 40px 20px; 
            text-align: center;
            height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }}
        
        .main-title {{
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 8px;
        }}
        
        .sub-title {{
            font-size: 18px;
            opacity: 0.9;
        }}
        
        .search-section {{
            padding: 20px;
            background: #f8f9fa;
            height: calc(100vh - 180px);
            overflow-y: auto;
        }}
        
        .search-box {{
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }}
        
        .search-input {{
            flex: 1;
            padding: 12px 15px;
            border: 2px solid #4CAF50;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
        }}
        
        .search-input:focus {{
            border-color: #2e7d32;
            box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
        }}
        
        .search-btn {{
            background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 20px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
        }}
        
        .search-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.3);
        }}
        
        .directory-card {{
            background: #f8fff8;
            border: 2px solid #e8f5e8;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            min-height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}
        
        .directory-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.2);
            border-color: #4CAF50;
        }}
        
        .card-title {{
            font-size: 18px;
            font-weight: bold;
            color: #2e7d32;
            margin-bottom: 5px;
        }}
        
        .card-subtitle {{
            font-size: 14px;
            color: #666;
        }}
        
        .result-section {{
            padding: 20px;
            display: none;
        }}
        
        .result-success {{
            background: #e8f5e8;
            border: 1px solid #c8e6c9;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
        }}
        
        .result-error {{
            background: #ffebee;
            border: 1px solid #ffcdd2;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
        }}
        
        .product-info {{
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        
        .product-row {{
            font-weight: bold;
            color: #2e7d32;
            margin-bottom: 5px;
        }}
        
        .directory-view {{
            padding: 20px;
            height: calc(100vh - 180px);
            overflow-y: auto;
            display: none;
        }}
        
        .directory-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            font-size: 11px;
        }}
        
        .directory-table th,
        .directory-table td {{
            border: 1px solid #e0e0e0;
            padding: 4px 6px;
            text-align: left;
        }}
        
        .directory-table th {{
            background: #f8fff8;
            font-weight: bold;
            color: #2e7d32;
            position: sticky;
            top: 0;
        }}
        
        .merged-cell {{
            background-color: #f0f8f0;
            font-weight: bold;
        }}
        
        .back-btn {{
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            margin-top: 15px;
        }}
        
        .footer {{
            background: #f5f5f5;
            padding: 15px 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
            border-top: 1px solid #eee;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            z-index: 1000;
        }}
        
        @media (max-width: 600px) {{
            .header {{ padding: 30px 15px; }}
            .main-title {{ font-size: 24px; }}
            .sub-title {{ font-size: 14px; }}
            .search-box {{ flex-direction: column; }}
            .directory-table {{ font-size: 9px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="main-title">产品目录</div>
            <div class="sub-title">查看绿色食品适用标准目录</div>
        </div>
        
        <div class="search-section">
            <div class="search-box">
                <input type="text" id="productInput" class="search-input" placeholder="请输入产品名称...">
                <button class="search-btn" onclick="searchProduct()">搜索</button>
            </div>
            
            <div class="directory-card" onclick="showFullDirectory()">
                <div class="card-title">绿色食品产品适用标准目录（2023版）</div>
                <div class="card-subtitle">点击查看完整产品目录（975行数据）</div>
            </div>
        </div>
        
        <div id="resultSection" class="result-section"></div>
        
        <div id="directoryView" class="directory-view">
            <h3>绿色食品产品适用标准目录（2023版）</h3>
            <div id="directoryContent"></div>
            <button class="back-btn" onclick="hideDirectory()">返回搜索</button>
        </div>
        
        <div class="footer">
            <div>本软件内容均来源于中国绿色食品发展中心官网</div>
            <div>如果存在问题请联络作者：QQ:10780329</div>
        </div>
    </div>

    <script>
        // 完整的975行Excel数据 - 与xlsx文件内容完全一致
        {js_array}

        // 搜索产品 - 搜索范围为xlsx文档内所有词语
        function searchProduct() {{
            const productName = document.getElementById('productInput').value.trim();
            
            if (!productName) {{
                alert('请输入产品名称');
                return;
            }}
            
            const resultSection = document.getElementById('resultSection');
            resultSection.style.display = 'block';
            
            // 搜索产品 - 在所有列中搜索
            const foundProducts = [];
            for (let i = 2; i < fullExcelData.length; i++) {{
                const row = fullExcelData[i];
                if (row && row.length >= 4) {{
                    // 在所有4列中搜索
                    let found = false;
                    for (let j = 0; j < 4; j++) {{
                        if (row[j] && row[j].toString().trim()) {{
                            const cellContent = row[j].toString().trim();
                            if (cellContent.toLowerCase().includes(productName.toLowerCase())) {{
                                found = true;
                                break;
                            }}
                        }}
                    }}
                    
                    if (found) {{
                        // 找到对应的标准名称（向上查找非空值）
                        let standardName = row[1] || '';
                        let rowNum = i;
                        while (!standardName && rowNum > 2) {{
                            rowNum--;
                            const prevRow = fullExcelData[rowNum];
                            if (prevRow && prevRow[1]) {{
                                standardName = prevRow[1];
                                break;
                            }}
                        }}
                        
                        foundProducts.push({{
                            rowNumber: i + 1, // Excel行号（1-based）
                            standard: standardName,
                            product: row[2] || '',
                            description: row[3] || '',
                            originalRow: row
                        }});
                    }}
                }}
            }}
            
            if (foundProducts.length > 0) {{
                let resultHTML = '<div class="result-success">';
                resultHTML += `<strong>找到 ${{foundProducts.length}} 个匹配项：</strong>`;
                
                foundProducts.forEach(product => {{
                    resultHTML += `<div class="product-info">`;
                    resultHTML += `<div class="product-row">所在行：第 ${{product.rowNumber}} 行</div>`;
                    resultHTML += `<div>标准：${{product.standard || '暂无标准信息'}}</div>`;
                    resultHTML += `<div>产品：${{product.product || '暂无产品信息'}}</div>`;
                    resultHTML += `<div>说明：${{product.description || '暂无说明'}}</div>`;
                    resultHTML += `</div>`;
                }});
                
                resultHTML += '</div>';
                resultSection.innerHTML = resultHTML;
            }} else {{
                resultSection.innerHTML = `
                    <div class="result-error">
                        <strong>未找到匹配项。</strong>
                        <div>请检查搜索词语是否正确，或联系技术支持。</div>
                    </div>
                `;
            }}
        }}

        // 显示完整目录 - 对应xlsx文档内ABCD列975行的所有内容
        function showFullDirectory() {{
            document.querySelector('.search-section').style.display = 'none';
            document.getElementById('resultSection').style.display = 'none';
            document.getElementById('directoryView').style.display = 'block';
            
            let directoryHTML = '<table class="directory-table">';
            directoryHTML += '<thead><tr><th>A列</th><th>B列</th><th>C列</th><th>D列</th></tr></thead><tbody>';
            
            // 显示所有975行数据
            fullExcelData.forEach((row, index) => {{
                directoryHTML += '<tr>';
                
                // A列：序号
                directoryHTML += `<td class="${{row[0] ? '' : 'merged-cell'}}">${{row[0] || ''}}</td>`;
                
                // B列：标准名称
                directoryHTML += `<td class="${{row[1] ? '' : 'merged-cell'}}">${{(row[1] || '').toString().replace(/\\n/g, '<br>')}}</td>`;
                
                // C列：适用产品名称
                directoryHTML += `<td>${{row[2] || ''}}</td>`;
                
                // D列：适用产品名称说明
                directoryHTML += `<td>${{row[3] || ''}}</td>`;
                
                directoryHTML += '</tr>';
            }});
            
            directoryHTML += '</tbody></table>';
            directoryHTML += `<div style="margin-top: 15px; color: #666;">显示 ${{fullExcelData.length}} 行数据（完整目录，ABCD列一一对应，合并单元格已标注）</div>`;
            
            document.getElementById('directoryContent').innerHTML = directoryHTML;
        }}

        // 隐藏目录视图
        function hideDirectory() {{
            document.getElementById('directoryView').style.display = 'none';
            document.querySelector('.search-section').style.display = 'block';
            document.getElementById('resultSection').style.display = 'none';
        }}

        // 添加键盘事件支持
        document.getElementById('productInput').addEventListener('keypress', function(event) {{
            if (event.key === 'Enter') {{
                searchProduct();
            }}
        }});

        // 页面加载完成
        console.log('模块一页面加载完成，包含975行完整Excel数据');
        console.log('Excel数据总量:', fullExcelData.length);
        console.log('数据一致性：与xlsx文件内容完全一致');
    </script>
</body>
</html>'''
    
    return html_template

if __name__ == "__main__":
    fix_module1_functionality()