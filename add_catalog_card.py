#!/usr/bin/env python3
"""
为module1添加标准目录卡片
"""

def add_catalog_card():
    file_path = "android-project/app/src/main/assets/www/module1_fixed_final_v4.html"
    
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Adding catalog card to module1...")
        
        # 在搜索框后添加标准目录卡片
        catalog_card = """
            </div>
            
            <div class="standard-catalog-card" onclick="showFullCatalog()" style="background: white; border: 2px solid #e8f5e8; border-radius: 8px; padding: 15px; margin-bottom: 15px; cursor: pointer; transition: all 0.3s ease;">
                <div style="font-size: 16px; font-weight: bold; color: #2e7d32; margin-bottom: 8px;">绿色食品产品适用标准目录（2023版）</div>
                <div style="font-size: 12px; color: #666;">点击查看完整的标准目录内容</div>
            </div>
        </div>"""
        
        # 替换搜索部分的结束标签
        content = content.replace("            </div>\n        </div>", catalog_card)
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Added: Catalog card to module1")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    add_catalog_card()