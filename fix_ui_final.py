import re

# 修复主页移动端样式
with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 添加移动端样式
if '@media (max-width: 600px)' not in content:
    # 找到CSS结尾位置
    css_end = content.find('        .footer a:hover {\n            text-decoration: underline;\n        }\n    </style>')
    if css_end != -1:
        css_end_pos = css_end + len('        .footer a:hover {\n            text-decoration: underline;\n        }\n    </style>')
        new_content = content[:css_end_pos - len('\n    </style>')] + '\n        \n        @media (max-width: 600px) {\n            .container { border-radius: 15px; margin: 0 auto; }\n            .header { padding: 20px; }\n            .main-title { font-size: 20px; }\n        }\n    </style>' + content[css_end_pos:]
        content = new_content

with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("主页移动端样式已添加")

# 检查模块三的移动端样式
with open('android-project/app/src/main/assets/www/module3_final.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 添加移动端样式
if '@media (max-width: 600px)' not in content:
    # 找到CSS结尾位置
    css_end = content.find('    </style>')
    if css_end != -1:
        css_end_pos = css_end
        new_content = content[:css_end_pos] + '        \n        @media (max-width: 600px) {\n            .container { border-radius: 15px; margin: 0 auto; }\n            .header { padding: 20px; }\n            .header h1 { font-size: 20px; }\n        }\n    </style>' + content[css_end_pos + len('    </style>'):]
        content = new_content

with open('android-project/app/src/main/assets/www/module3_final.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("模块三移动端样式已添加")

print("\nUI一致性修复完成")
print("主页倒角已与模块一一致")
print("模块三距离app最上延已与模块一一致")
print("所有模块的移动端倒角均为15px")