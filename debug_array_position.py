def debug_array_position():
    # 读取v6文件
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到数组开始和结束的位置
    array_start = content.find('const fullExcelData = [')
    print(f'数组开始位置: {array_start}')
    
    if array_start == -1:
        print('未找到数组开始位置')
        return
    
    array_end = content.find('];', array_start)
    print(f'数组结束位置: {array_end}')
    
    if array_end == -1:
        print('未找到数组结束位置')
        return
    
    array_end += 2  # 包含];
    
    # 显示数组前后的内容
    print('数组前10个字符:')
    print(content[array_start-10:array_start])
    print('数组开始:')
    print(content[array_start:array_start+100])
    print('数组结尾:')
    print(content[array_end-50:array_end])
    print('数组后10个字符:')
    print(content[array_end:array_end+10])

if __name__ == "__main__":
    debug_array_position()