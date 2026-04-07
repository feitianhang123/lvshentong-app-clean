# 绿色食品申报通 - 源代码文档

## 软件基本信息
- **软件名称**: 绿色食品申报通
- **版本号**: V1.0
- **开发完成日期**: 2026年4月
- **著作权人**: [您的姓名]
- **软件类型**: Android应用软件

## 源代码结构

### 1. 主页面 (index_fixed.html)
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>绿色食品申报通</title>
    <style>
        /* CSS样式代码 */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #f8fff8 0%, #e8f5e8 100%);
            min-height: 100vh;
            padding: 2%;
            color: #333;
        }
        .container { 
            max-width: 95%; 
            width: 900px;
            margin: 0 auto; 
            background: white; 
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(76, 175, 80, 0.15);
            overflow: hidden;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- 页面内容 -->
    </div>
</body>
</html>
```

### 2. 模块一：产品目录 (module1_fixed_final_v31.html)
包含完整的绿色食品产品适用标准目录搜索功能。

### 3. 模块二：现行标准 (module2_current_standards.html)
提供绿色食品产品标准和准则标准查询功能。

### 4. 模块三：材料清单 (module3_final.html)
提供绿色食品申报所需的6类材料清单。

### 5. 模块四：预审核 (module4_coming_soon.html)
待开发功能模块。

## 技术特点

### 前端技术
- HTML5 + CSS3 + JavaScript
- 响应式设计，适配移动端
- 渐变背景和圆角设计

### 数据处理
- 基于Excel数据的标准目录查询
- 实时搜索功能
- 数据验证和错误处理

### UI设计
- 统一的视觉风格
- 一致的交互体验
- 友好的用户界面

## 文件清单
- index_fixed.html - 主页面
- module1_fixed_final_v31.html - 产品目录模块
- module2_current_standards.html - 现行标准模块  
- module3_final.html - 材料清单模块
- module4_coming_soon.html - 预审核模块

[源代码前30页和后30页内容...]