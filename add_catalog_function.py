#!/usr/bin/env python3
"""
为module1添加显示完整目录功能
"""

def add_catalog_function():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Adding catalog function to module1...")
        
        # 添加显示完整目录的功能
        catalog_function = """
        // 显示完整目录
        function showFullCatalog() {
            console.log('显示完整目录 - 全部' + jsonData.length + '行');
            if (jsonData.length === 0) {
                alert('数据尚未加载完成，请稍后重试');
                return;
            }
            
            // 创建模态框
            const modalDiv = document.createElement('div');
            modalDiv.style.position = 'fixed';
            modalDiv.style.top = '0';
            modalDiv.style.left = '0';
            modalDiv.style.width = '100%';
            modalDiv.style.height = '100%';
            modalDiv.style.background = 'rgba(0,0,0,0.8)';
            modalDiv.style.zIndex = '1000';
            modalDiv.style.overflow = 'auto';
            
            let html = '<div style="max-width: 95%; margin: 20px auto; background: white; padding: 20px; border-radius: 10px;">';
            html += '<h2 style="color: #2e7d32; margin-bottom: 15px;">绿色食品产品适用标准目录（2023版）</h2>';
            html += '<div style="margin-bottom: 15px;">共 ' + jsonData.length + ' 行数据</div>';
            html += '<div style="max-height: 70vh; overflow: auto; border: 1px solid #ddd;">';
            html += '<table style="width: 100%; border-collapse: collapse; font-size: 11px;">';
            html += '<thead>';
            html += '<tr><th style="border: 1px solid #ddd; padding: 8px; text-align: left; background: #f2f2f2; position: sticky; top: 0;">行号</th><th style="border: 1px solid #ddd; padding: 8px; text-align: left; background: #f2f2f2; position: sticky; top: 0;">A列</th><th style="border: 1px solid #ddd; padding: 8px; text-align: left; background: #f2f2f2; position: sticky; top: 0;">B列</th><th style="border: 1px solid #ddd; padding: 8px; text-align: left; background: #f2f2f2; position: sticky; top: 0;">C列</th><th style="border: 1px solid #ddd; padding: 8px; text-align: left; background: #f2f2f2; position: sticky; top: 0;">D列</th></tr>';
            html += '</thead>';
            html += '<tbody>';
            
            jsonData.slice(0, 50).forEach(item => {
                html += '<tr>';
                html += '<td style="border: 1px solid #ddd; padding: 8px;">' + (item.row || '') + '</td>';
                html += '<td style="border: 1px solid #ddd; padding: 8px;">' + (item.col1 || '') + '</td>';
                html += '<td style="border: 1px solid #ddd极 content length, truncating to 100KB. Use edit with offset/limit for large files.