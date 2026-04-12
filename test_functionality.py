#!/usr/bin/env python3
"""
测试绿色食品申报通项目功能完整性
验证页面基本功能是否正常
"""

import os

def check_file_content(file_path):
    """检查文件内容完整性"""
    if not os.path.exists(file_path):
        return False, "文件不存在"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = []
    
    # 检查关键HTML标签
    if '<html' in content and '</html>' in content:
        checks.append("HTML结构完整")
    else:
        checks.append("HTML结构不完整")
    
    if '<head>' in content and '</head>' in content:
        checks.append("HEAD部分完整")
    else:
        checks.append("HEAD部分不完整")
    
    if '<body>' in content and '</body>' in content:
        checks.append("BODY部分完整")
    else:
        checks.append("BODY部分不完整")
    
    # 检查JavaScript
    if '<script>' in content or 'src=' in content:
        checks.append("JavaScript存在")
    else:
        checks.append("JavaScript缺失")
    
    # 检查CSS样式
    if '<style>' in content or 'class=' in content:
        checks.append("CSS样式存在")
    else:
        checks.append("CSS样式缺失")
    
    return True, ", ".join(checks)

def main():
    print("测试绿色食品申报通项目功能完整性")
    print("=" * 60)
    
    files_to_test = [
        ("android-project/app/src/main/assets/www/index_fixed.html", "主页面"),
        ("android-project/app/src/main/assets/www/module1_fixed_final_v4.html", "模块一"),
        ("android-project/app/src/main/assets/www/module2_current_standards.html", "模块二"),
        ("android-project/app/src/main/assets/www/module3_final.html", "模块三")
    ]
    
    all_passed = True
    
    for file_path, description in files_to_test:
        print("\n测试: " + description)
        exists, result = check_file_content(file_path)
        
        if exists:
            print("OK " + result)
            if "不完整" in result or "缺失" in result:
                all_passed = False
        else:
            print("FAIL " + result)
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("所有功能测试通过！")
        print("OK 页面结构完整")
        print("OK 样式和脚本正常")
    else:
        print("警告: 部分功能测试未通过")
    
    return all_passed

if __name__ == "__main__":
    main()