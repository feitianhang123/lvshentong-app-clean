#!/usr/bin/env python3
"""
修复module1_fixed_final_v4.html的乱码
"""

def fix_module1_encoding():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 以二进制方式读取文件
        with open(file_path, 'rb') as f:
            content_bytes = f.read()
        
        # 尝试用不同编码解码
        try:
            content = content_bytes.decode('utf-8')
        except UnicodeDecodeError:
            try:
                content = content_bytes.decode('gbk')
            except UnicodeDecodeError:
                content = content_bytes.decode('latin-1')
        
        print("Fixing module1 file encoding...")
        
        # 修复乱码
        content = content.replace("Ԥ�������ݣ���������\"nan\"ֵ", "预处理数据：清理所有\"nan\"值")
        content = content.replace("�¼��������������", "事件监听器设置完成")
        content = content.replace("���ݼ���ʧ�ܣ���ˢ��ҳ��", "数据加载失败，请刷新页面")
        content = content.replace("��ʾ�������� - ȫ��", "显示完整数据 - 全部")
        content = content.replace("������δ������ɣ����Ժ�����", "数据尚未加载完成，请稍后重试")
        content = content.replace("����ģ̬��", "创建模态框")
        content = content.replace("�?", "")
        content = content.replace("�?", "")
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Fixed: Module1 file encoding issues")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    fix_module1_encoding()