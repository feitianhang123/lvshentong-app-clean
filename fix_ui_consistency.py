import re

# 修复主页移动端样式
with open('android-project/app/src/main/assets/www/index_fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在CSS结尾添加移动端样式
if '@media (max-width: 600px)' not in content:
    content = content.replace(
        '        .footer a:hover {\n            text-decoration: underline;\n        }\n    </style>',
        '        .footer a:hover {\n            text-decoration: underline;\n        }\n        \n        @media (max-width: 600px) {\n            .container { border-radius: 15px; margin: 0 auto; }\n            .header { padding: 20px; }\n            .main-title { font-size: 20px; }\n        }\n    </style>'
    )

with open('android-project/app/src/main/assets/www/index_fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("主页移动端样式已添加")

# 为模块三添加移动端样式
with open('android-project/app/src/main/assets/www/module3_final.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在CSS结尾添加移动端样式
if '@media (max-width: 600px)' not in content:
    # 找到CSS结尾
    css_end_pattern = r'(\}\s*\}\s*\}\s*\}\s*\}\s*\}\s*</style>)'
    if re.search(css_end_pattern, content):
        content = re.sub(
            css_end_pattern,
            '        }\n        }\n        }\n        }\n        }\n        }\n        \n        @media (max-width: 600px) {\n            .container { border-radius: 15px; margin: 0 auto; }\n            .header { padding: 20px; }\n            .header h1 { font-size: 20px; }\n        }\n    </style>',
            content
        )

with open('android-project/app/src/main/assets/www/module3_final.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("模块三移动端样式已添加")

print("UI一致性修复完成")