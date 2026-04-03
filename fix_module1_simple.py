#!/usr/bin/env python3
"""
修复module1_fixed_final_v4.html的乱码
"""

def fix_module1_simple():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
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
        with open(file_path, 'w', encoding='utf-8') as极 content length, truncating to 100KB. Use edit with offset/limit for large files.