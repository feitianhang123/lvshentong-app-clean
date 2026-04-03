#!/usr/bin/env python3
"""
修复module1_fixed_final_v4.html的完整乱码
"""

def fix_module1_complete():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
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
        
        print("Fixing module1 file encoding...")
        
        # 修复乱码
        content = content.replace("产品目录 - 绿色食品申报�?", "产品目录 - 绿色食品申报通")
        content = content.replace("请输入产品名�?..", "请输入产品名称...")
        content = content.replace("�?", "←")
        content = content.replace("�?找到匹配产品�?", "✅ 找到匹配产品！")
        content = content.replace("�?未找到产�?", "❌ 未找到产品")
        content = content.replace("返回主界�?", "返回主界面")
        content = content.replace("�?", "")
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Fixed: Module1 file encoding issues")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    fix_module1_complete()