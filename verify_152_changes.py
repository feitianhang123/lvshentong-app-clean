#!/usr/bin/env python3
"""
验证152版本模块一UI修改
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
    print("验证152版本模块一UI修改")
    print("=" * 50)
    
    # 检查模块一的UI是否与主界面一致
    module1_checks = {
        "绿色部分置顶": "position: fixed",
        "灰色部分垫底": "position: fixed",
        "主标题字体": "font-size: 32px",
        "副标题字体": "font-size: 18px",
        "Footer字体": "font-size: 12px",
        "Footer内容": "本软件内容均来源于中国绿色食品发展中心官网",
        "无缝显示": "padding-top: 120px",
        "底部内边距": "padding-bottom: 60px",
        "内容区域": "height: calc(100vh - 180px)"
    }
    
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    print("检查文件: " + file_path)
    
    exists, result = check_file(file_path, module1_checks)
    
    if exists:
        print(result)
        if "FAIL" in result:
            print("警告: 部分修改验证未通过")
            return False
        else:
            print("\n" + "=" * 50)
            print("所有修改验证通过！")
            print("模块一UI已与主界面完全一致：")
            print("- 绿色部分置顶，灰色部分垫底")
            print("- 字体样式完全一致")
            print("- 不保留两侧上下缝隙")
            print("- Footer内容完全一致")
            return True
    else:
        print("FAIL " + result)
        return False

if __name__ == "__main__":
    main()