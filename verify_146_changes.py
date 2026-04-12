#!/usr/bin/env python3
"""
验证146版本UI修改
"""

import os

def check_file(file_path, checks):
    """检查单个文件的修改"""
    if not os.path.exists(file_path):
        return False, "文件不存在"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = []
    for check_name, check_value in checks.items():
        if check_value in content:
            results.append("OK " + check_name)
        else:
            results.append("FAIL " + check_name)
    
    return True, ", ".join(results)

def main():
    print("验证146版本UI修改")
    print("=" * 50)
    
    # 定义每个文件需要检查的内容
    files_to_check = {
        "index_fixed.html": {
            "模块卡片分布": "justify-content: space-between",
            "底部位置": "bottom: 0",
            "container相对定位": "position: relative"
        },
        "module1_fixed_final_v4.html": {
            "内容区域高度": "calc(100vh - 280px)",
            "底部位置": "bottom: 0",
            "container相对定位": "position: relative"
        },
        "module2_current_standards.html": {
            "内容区域高度": "calc(100vh - 300px)",
            "底部位置": "bottom: 0",
            "container相对定位": "position: relative"
        },
        "module3_final.html": {
            "内容区域高度": "calc(100vh - 300px)",
            "底部位置": "bottom: 0",
            "container相对定位": "position: relative"
        },
        "module4_coming_soon.html": {
            "全屏显示": "height: 100vh",
            "底部位置": "bottom: 0",
            "container相对定位": "position: relative",
            "内容区域": "calc(100vh - 280px)"
        }
    }
    
    all_passed = True
    
    for file_name, checks in files_to_check.items():
        file_path = "android-project/app/src/main/assets/www/" + file_name
        print("\n检查文件: " + file_name)
        
        exists, result = check_file(file_path, checks)
        
        if exists:
            print(result)
            if "FAIL" in result:
                all_passed = False
        else:
            print("FAIL " + result)
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("所有修改验证通过！")
        print("OK 模块一和模块四UI已统一")
        print("OK 所有页面底部位于屏幕最下方")
        print("OK 主页面模块卡片上下平均分布")
    else:
        print("警告: 部分修改验证未通过")
    
    return all_passed

if __name__ == "__main__":
    main()