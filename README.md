# 🌱 绿色食品标准查询系统

## 📋 项目概述

这是一个完整的绿色食品标准查询系统，包含四个主要模块，提供全面的标准查询、统计、对比功能。

## 🚀 功能模块

### 1. 🏠 主页 (index.html)
- **功能**: 系统主入口，提供所有模块的导航
- **特点**: 
  - 现代化UI设计，渐变背景
  - 响应式布局，支持移动端
  - 快速导航到各个功能模块

### 2. 📋 模块二：现行标准查询 (module2_current_standards.html)
- **功能**: 完整的143个绿色食品标准查询系统
- **特点**:
  - 🔍 智能实时搜索（标准名称、标准号）
  - 📂 分类浏览（所有标准、产品标准、准则标准）
  - 📥 一键下载官方标准文件
  - 📱 响应式设计，完美适配各种设备
  - 📊 实时统计信息显示

### 3. 📊 模块一：标准统计 (module1_fixed_final_v4.html)
- **功能**: 标准数据统计和可视化
- **特点**:
  - 标准数量统计
  - 分类统计图表
  - 数据导出功能

### 4. 🔍 模块三：标准对比 (module3_standard_comparison.html)
- **功能**: 标准详细对比工具
- **特点**:
  - 选择任意两个标准进行对比
  - 显示标准基本信息差异
  - 直接链接到官方下载
  - 差异高亮显示

### 5. ⏳ 模块四：标准修订追踪 (规划中)
- **功能**: 标准修订历史追踪
- **状态**: 预留位置，功能规划中

## 📊 数据统计

- **总标准数**: 143个
- **产品标准**: 129个
- **准则标准**: 14个

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (原生)
- **服务器**: Python HTTP Server (端口8080)
- **数据**: JSON格式标准数据
- **设计**: 响应式设计，现代化UI

## 🌐 访问方式

1. **启动服务器**: 
   ```bash
   python -m http.server 8080
   ```

2. **访问地址**:
   - 主页: http://localhost:8080/index.html
   - 模块二: http://localhost:8080/module2_current_standards.html
   - 模块三: http://localhost:8080/module3_standard_comparison.html
   - 模块一: http://localhost:8080/module1_fixed_final_v4.html
   - 测试页面: http://localhost:8080/test_all_modules.html

## 📁 文件结构

```
├── index.html              # 系统主页
├── module2_current_standards.html  # 模块二：现行标准查询
├── module3_standard_comparison.html # 模块三：标准对比
├── module1_fixed_final_v4.html      # 模块一：标准统计
├── test_all_modules.html   # 测试页面
├── standards_data.js       # 标准数据文件 (143个标准)
├── README.md              # 项目说明文档
└── 其他开发文件
```

## ✅ 完成状态

- [x] 主页设计和导航系统
- [x] 模块二：现行标准查询 (完整功能)
- [x] 模块三：标准对比功能
- [x] 模块一：标准统计页面
- [x] 所有143个标准数据整理
- [x] 响应式设计适配
- [ ] 模块四：标准修订追踪 (规划中)

## 🎯 使用说明

1. 确保Python环境已安装
2. 在项目根目录运行服务器
3. 打开浏览器访问 http://localhost:8080
4. 通过主页导航到各个功能模块

## 📞 技术支持

如有任何问题，请联系系统管理员。

---
**最后更新**: 2026-03-31