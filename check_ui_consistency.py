#!/usr/bin/env python3
"""
检查绿色食品申报通项目UI一致性
验证所有页面是否已实现全屏显示和统一的UI样式
"""

import os

# 需要检查的文件列表
FILES_TO_CHECK = [
    "android-project/app/src/main/assets/www/index_fixed.html",
    "android-project/app/src/main/assets/www/module1_fixed_final_v4.html", 
    "android-project/app/src/main/assets/www/module2_current_standards.html",
    "android-project/app/src/main/assets/www/module3_final.html"
]

# 检查的关键CSS属性
KEY_CSS_PROPERTIES = {
    "body-padding": "padding: 0",
    "body-margin": "margin: 0", 
    "container-width": "width: 100%",
    "container-height": "height: 100vh",
    "container-border-radius": "border-radius: 0",
    "container-box-shadow": "box-shadow: none",
    "header-height": "height: 120px",
    "header-padding": "padding: 40px 20px",
    "header-flex": "display: flex",
    "main-title-font-size": "font-size: 32px",
    "sub-title-font-size": "font-size: 18px"
}

def check_file(file_path):
    """检查单个文件的UI一致性"""
    if not os.path.exists(file_path):
        return False, "文件不存在: " + file_path
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = []
    for prop_name, prop_value in KEY_CSS_PROPERTIES.items():
        if prop_value in content:
            results.append("OK " + prop_name + ": " + prop_value)
        else:
            results.append("FAIL " + prop_name + ": " + prop_value + " - 未找到")
    
    return True, "\n".join(results)

def main():
    print("检查绿色食品申报通项目UI一致性")
    print("=" * 60)
    
    all_passed = True
    
    for file_path in FILES_TO_CHECK:
        print("\n检查文件: " + file_path)
        exists, result = check_file(file_path)
        
        if exists:
            print(result)
            # 检查是否所有属性都通过
            if "FAIL" in result:
                all_passed = False
        else:
            print("FAIL " + result)
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("所有文件UI一致性检查通过！")
        print("OK 所有页面已实现全屏显示")
        print("OK 顶部绿色部分大小保持一致")
        print("OK 字体大小和样式完全统一")
    else:
        print("警告: UI一致性检查未完全通过，请检查上述问题")
    
    return all_passed

if __name__ == "__main__":
    main()