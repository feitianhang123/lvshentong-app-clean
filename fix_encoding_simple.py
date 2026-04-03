#!/usr/bin/env python3
"""
修复module1_fixed_final_v4.html的乱码
"""

def fix_encoding_simple():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Fixing module1 file encoding...")
        
        # 修复乱码
        content = content.replace("请输入产品名�?..", "请输入产品名称...")
        content = content.replace("绿色食品产品适用标准目录�?023版）", "绿色食品产品适用标准目录（2023版）")
        content = content.replace("点击查看完整的标准目录内�?", "点击查看完整的标准目录内容")
        content = content.replace("�?找到匹配产品�?", "✅ 找到匹配产品！")
        content = content.replace("�?未找到产�?", "❌ 未找到产品")
        content = content.replace("�?", "←")
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
    fix_encoding_simple()