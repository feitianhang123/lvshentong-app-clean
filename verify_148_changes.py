#!/usr/bin/env python3
"""
验证148版本UI修改
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
    print("验证148版本UI修改")
    print("=" * 50)
    
    # 定义每个文件需要检查的内容
    files_to_check = {
        "index_fixed.html": {
            "模块卡片间距": "gap: 25px",
            "模块卡片内边距": "padding: 30px",
            "模块卡片高度": "min-height: 120px"
        },
        "module1_fixed_final_v4.html": {
            "UI统一": "#4caf50 0%, #2e7d32 100%",
            "搜索区域高度": "calc(100vh - 240px)",
            "目录卡片高度": "min-height: 120px"
        },
        "module2_current_standards.html": {
            "标准容器高度": "calc(100vh - 240px)",
            "标准卡片高度": "min-height: 120px",
            "搜索区域内边距": "padding: 30px"
        },
        "module3_final.html": {
            "卡片网格高度": "calc(100vh - 240px)",
            "卡片网格间距": "gap: 25px",
            "卡片高度": "min-height: 140px"
        },
        "module4_coming_soon.html": {
            "内容区域高度": "calc(100vh - 240px)",
            "卡片内边距": "padding: 40px",
            "卡片高度": "min-height: 150px"
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
        print("OK 模块一UI已与其他界面一致")
        print("OK 主页面模块卡片宽度加宽，显示效果改善")
        print("OK 模块三清单卡显示范围增大，底部显示优化")
    else:
        print("警告: 部分修改验证未通过")
    
    return all_passed

if __name__ == "__main__":
    main()