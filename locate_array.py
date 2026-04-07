def locate_array():
    with open('android-project/app/src/main/assets/www/module1_fixed_final_v6.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start = content.find('const fullExcelData = [')
    end = content.find('];', start) + 2
    
    print(f'Start: {start}')
    print(f'End: {end}')
    print(f'Length: {end - start}')
    
    # 显示数组的开始部分
    print('Array start:')
    print(content[start:start+200])
    
    # 显示数组的结束部分
    print('Array end:')
    print(content[end-200:end])

if __name__ == "__main__":
    locate_array()