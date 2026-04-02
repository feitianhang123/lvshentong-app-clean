# 绿色食品申报通 Android应用

## 📱 项目概述

这是一个用于绿色食品申报的Android移动应用，包含三个主要功能模块：

1. **模块一**: 产品目录搜索 - 查询绿色食品适用标准目录
2. **模块二**: 文档下载 - 获取申报相关文档模板
3. **模块三**: 申报指南 - 查看申报流程和指南

## 🛠️ 技术栈

- **Android**: Java + WebView
- **前端**: HTML5 + CSS3 + JavaScript
- **数据**: JSON格式的产品标准目录
- **构建**: Gradle + GitHub Actions

## 📦 项目结构

```
lvshentong-app-clean/
├── android-project/          # Android项目目录
│   ├── app/
│   │   └── src/main/assets/www/
│   │       ├── module1_fixed_final_v4.html  # 修复后的模块一
│   │       ├── complete_excel.json          # 产品标准数据
│   │       └── ...其他模块文件
│   └── build.gradle
├── app.py                   # Flask后端API服务器
├── build.sh                 # Linux构建脚本
├── build.bat                # Windows构建脚本
├── .github/workflows/       # GitHub Actions配置
└── README.md
```

## 🚀 快速开始

### 本地构建

**Linux/Mac:**
```bash
chmod +x build.sh
./build.sh
```

**Windows:**
```
build.bat
```

### GitHub Actions自动构建

每次推送到 `master` 分支时，GitHub Actions会自动：
1. ✅ 检查代码
2. ✅ 设置Android环境
3. ✅ 构建Debug APK
4. ✅ 上传构建产物

## 🔧 模块一修复说明

### 问题原因
原始问题："JSON加载失败 - Failed to fetch"
- HTML文件使用 `http://localhost:5001/api/search` 调用API
- 在浏览器环境中localhost指向客户端而非服务器
- 导致跨域访问失败

### 解决方案
1. ✅ **移除API依赖**: 改为直接使用本地JSON文件
2. ✅ **修复乱码字符**: 清理HTML文件中的显示问题
3. ✅ **优化搜索功能**: 在前端直接处理搜索逻辑
4. ✅ **数据验证**: 975行标准数据，924个有效产品

### 功能验证
- ✅ 搜索"苹果": 找到2个产品
- ✅ 搜索"肉": 找到23个产品
- ✅ 搜索"茶": 找到22个产品
- ✅ 错误处理: 未找到产品时显示友好提示

## 📊 数据格式

产品标准JSON文件 (`complete_excel.json`) 包含975行数据，格式如下：

```json
[
  {
    "row": 1,
    "col1": "一、种植业产品标准",
    "col2": "",
    "col3": "",
    "col4": ""
  },
  {
    "row": 3,
    "col1": "1",
    "col2": "绿色食品标准\nNY/T285-2021",
    "col3": "豆",
    "col4": "蚕豆、饭豆、扁豆、芸豆、绿豆、赤豆"
  }
]
```

## 📝 开发说明

### 后端服务器 (可选)
```bash
python app.py
```
服务器运行在: http://localhost:5001
- `/api/search?q=产品名称` - 搜索产品
- `/api/excel-info` - 获取数据信息

### 测试页面
项目包含多个测试文件用于验证功能：
- `test_final.html` - 完整功能测试
- `test_json_direct.html` - JSON加载测试
- `diagnose.py` - 数据诊断脚本

## 🤝 贡献指南

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目基于 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 绿色食品标准数据来源: 农业农村部相关标准目录
- 技术支持: OpenClaw AI助手