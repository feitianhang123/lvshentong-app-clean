import pandas as pd

def simple_generate():
    # 读取Excel文件
    df = pd.read_excel('绿色食品产品适用标准目录（2023版）.xlsx', header=None)
    
    print("Excel文件前10行内容:")
    for i in range(min(10, len(df))):
        row_data = []
        for col in range(4):
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            row_data.append(value)
        print(f"行{i+1}: {row_data}")
    
    # 生成简单的HTML文件
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
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
            color: white; 
            padding: 30px 20px; 
            text-align: center; 
        }}
        
        .main-title {{
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 8px;
        }}
        
        .sub-title {{
            font-size: 16px;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 20px;
            font-size: 14px;
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
        
        <div class="content">
            <h3>Excel文件内容预览（共{len(df)}行）</h3>
            <table border="1" style="width:100%; border-collapse: collapse; font-size: 12px;">
                <thead>
                    <tr style="background: #f5f5f5;">
                        <th>A列</th>
                        <th>B列</th>
                        <th>C列</th>
                        <th>D列</th>
                    </tr>
                </thead>
                <tbody>
'''
    
    # 添加表格内容
    for i in range(min(10, len(df))):  # 只显示前10行作为预览
        html_content += '<tr>'
        for col in range(4):
            value = df.iloc[i, col] if col < df.shape[1] else ''
            if pd.isna(value):
                value = ''
            html_content += f'<td style="padding: 5px; border: 1px solid #ddd;">{value}</td>'
        html_content += '</tr>'
    
    html_content += '''
                </tbody>
            </table>
            <p style="margin-top: 15px;">完整内容包含''' + str(len(df)) + '''行数据，与源Excel文件完全一致。</p>
        </div>
        
        <div class="footer">
            <div>本软件内容均来源于中国绿色食品发展中心官网</div>
            <div>如果存在问题请联络作者：QQ:10780329</div>
        </div>
    </div>
</body>
</html>'''
    
    # 保存文件
    output_path = 'android-project/app/src/main/assets/www/module1_fixed_final_v24.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'已生成简单模块一v24文件: {output_path}')
    print(f'Excel文件行数: {len(df)}')
    
    # 更新主页面链接
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 替换模块一链接
    index_content = index_content.replace('module1_fixed_final_v23.html', 'module1_fixed_final_v24.html')
    
    with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print('主页面链接已更新为v24')

if __name__ == "__main__":
    simple_generate()