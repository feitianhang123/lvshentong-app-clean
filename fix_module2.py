import re

# 读取模块二文件
with open('android-project/app/src/main/assets/www/module2_current_standards.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复移动端样式
content = re.sub(r'\.container\s*\{\s*border-radius:\s*15px;\s*margin:\s*10px;\s*\}', 
                 '.container { border-radius: 15px; margin: 0 auto; }', content)

# 写入修复后的文件
with open('android-project/app/src/main/assets/www/module2_current_standards.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("模块二移动端样式已修复")

# 修复模块四
with open('android-project/app/src/main/assets/www/module4_coming_soon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复移动端样式
content = re.sub(r'\.container\s*\{\s*border-radius:\s*15px;\s*margin:\s*10px;\s*\}', 
                 '.container { border-radius: 15px; margin: 0 auto; }', content)

# 写入修复后的文件
with open('android-project/app/src/main/assets/www/module4_coming_soon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("模块四移动端样式已修复")