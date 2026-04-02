#!/usr/bin/env python3
"""
修复所有HTML文件中的乱码字符
"""
import os
import re

def fix_html_encoding(file_path):
    """修复单个HTML文件的乱码"""
    try:
        # 以二进制方式读取文件
        with open(file_path, 'rb') as f:
            content_bytes = f.read()
        
        # 尝试用不同编码解码
        try:
            content = content_bytes.decode('utf-8')
        except UnicodeDecodeError:
            try:
                content = content_bytes.decode('gbk')
            except UnicodeDecodeError:
                content = content_bytes.decode('latin-1')
        
        print(f"Fixing: {file_path}")
        
        # 修复常见的乱码模式
        content = re.sub(r'�\?', '←', content)  # 返回按钮
        content = re.sub(r'极', '', content)     # 删除乱码字符
        content = re.sub(r'�', '', content)      # 删除其他乱码
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed: {file_path}")
        return True
        
    except Exception as e:
        print(f"Failed {file_path}: {e}")
        return False

def main():
    """主函数"""
    www_dir = "android-project/app/src/main/assets/www"
    
    if not os.path.exists(www_dir):
        print(f"Directory not found: {www_dir}")
        return
    
    # 修复所有HTML文件
    html_files = []
    for file in os.listdir(www_dir):
        if file.endswith('.html'):
            html_files.append(os.path.join(www_dir, file))
    
    print(f"Found {len(html_files)} HTML files")
    
    success_count = 0
    for html_file in html_files:
        if fix_html_encoding(html_file):
            success_count += 1
    
    print(f"\nFixed: {success_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()