#!/usr/bin/env python3
"""
修复模块一的数据加载部分
"""

def fix_data_loading():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Fixing data loading section...")
        
        # 添加错误处理
        old_pattern = "fetch('complete_excel.json')\\n                .then(response => response.json())"
        new_code = """fetch('complete_excel.json')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('数据加载失败: ' + response.status);
                    }
                    return response.json();
                })