# 修复HTML文件中的乱码字符

# 以二进制方式读取文件
with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'rb') as f:
    content_bytes = f.read()

# 尝试用不同编码解码
try:
    content = content_bytes.decode('utf-8')
except UnicodeDecodeError:
    try:
        content = content_bytes.decode('gbk')
    except UnicodeDecodeError:
        content = content_bytes.decode('latin-1')

print(f"成功读取文件，长度: {len(content)} 字符")

# 修复乱码字符（使用实际的乱码字符）
content = content.replace('产品目录 - 绿色食品申报�?', '产品目录 - 绿色食品申报通')
content = content.replace('请输入产品名�?..', '请输入产品名称...')

# 查找并替换其他乱码字符
import re
content = re.sub(r'�\?', '←', content)  # 返回按钮
content = re.sub(r'�\?找到匹配产品�\?', '✅ 找到匹配产品！', content)
content = re.sub(r'�\?未找到产�\?', '❌ 未找到产品', content)

# 写入修复后的内容
with open('android-project/app/src/main/assets/www/module1_fixed_final_v4.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("文件修复完成！")