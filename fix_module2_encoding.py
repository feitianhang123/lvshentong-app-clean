#!/usr/bin/env python3
"""
修复module2_current_standards.html的乱码
"""

def fix_module2():
    file_path = "android-project/app/src/main/assets/www/module2_current_standards.html"
    
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
        
        print("Fixing module2 file encoding...")
        
        # 修复乱码
        content = content.replace("所有标�?", "所有标准")
        content = content.replace("�?143 个标�?", "共143个标准")
        content = content.replace("没有找到匹配的标�?", "没有找到匹配的标准")
        content = content.replace("�?${total} 个标�?", "共${total}个标准")
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Fixed: Module2 file encoding issues")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    fix_module2()