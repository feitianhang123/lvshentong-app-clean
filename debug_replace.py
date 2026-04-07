def debug_replace():
    # 读取模板文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 找到数组开始和结束的位置
    array_start = template.find('const fullExcelData = [')
    array_end = template.find('];', array_start) + 2
    
    print(f'Array start: {array_start}')
    print(f'Array end: {array_end}')
    
    # 显示替换前后的内容
    print('Before replacement (array content):')
    print(template[array_start:array_start+500])
    
    # 测试替换
    test_content = template[:array_start] + 'const fullExcelData = [];' + template[array_end:]
    
    print('After replacement (test):')
    print(test_content[array_start:array_start+500])
    
    # 检查替换是否成功
    if 'const fullExcelData = [];' in test_content:
        print('Replacement successful!')
    else:
        print('Replacement failed!')

if __name__ == "__main__":
    debug_replace()