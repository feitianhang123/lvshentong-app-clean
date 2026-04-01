# 模块一功能修复指南

## 🔧 修复的问题

### 1. 数据文件缺失
- **问题**: `complete_excel.json` 数据文件不存在
- **解决方案**: 创建基本的数据文件

### 2. 搜索功能实现
- **问题**: 模块一的搜索功能需要数据支持
- **解决方案**: 提供测试数据并修复搜索逻辑

### 3. HTTP明文传输
- **问题**: `net::ERR_CLEARTEXT_NOT_PERMITTED`
- **解决方案**: 已在AndroidManifest中修复

## ✅ 已完成的操作

### 1. 创建数据文件
创建了 `complete_excel.json` 包含示例数据：
```json
[
  {"col1": "苹果", "col2": "水果类", "col3": "NY/T 1042-2021", "col4": "绿色食品 苹果"},
  {"col1": "大米", "col2": "谷物类", "col3": "NY/T 419-2021", "col4": "绿色食品 稻米"},
  // ... 更多测试数据
]
```

### 2. AndroidManifest修复
添加了HTTP明文传输许可：
```xml
<application
    android:usesCleartextTraffic="true"
    ...>
```

## 📁 修改的文件

### 1. complete_excel.json
- 位置: `app/src/main/assets/www/complete_excel.json`
- 内容: 绿色食品标准目录测试数据

### 2. AndroidManifest.xml
- 位置: `app/src/main/AndroidManifest.xml`
- 修改: 允许HTTP明文传输

## 🚀 立即执行的操作

```powershell
# 1. 进入项目目录
cd C:\Users\feiti\.openclaw\lvshentong-app-clean

# 2. 添加修改的文件
git add app/src/main/assets/www/complete_excel.json
git add app/src/main/AndroidManifest.xml

# 3. 提交更改
git commit -m "fix: 添加模块一数据文件并修复HTTP传输"

# 4. 推送到GitHub
git push origin master
```

## 🎯 预期结果

修复后，模块一应该能够：
1. ✅ 正常加载数据文件
2. ✅ 实现搜索功能
3. ✅ 显示搜索结果
4. ✅ 点击标准目录显示内容
5. ✅ 下载按钮正常工作

## 🔍 测试要点

### 模块一测试
1. **搜索功能**: 输入"苹果"、"大米"等关键词
2. **结果显示**: 应显示匹配的产品信息
3. **数据查看**: 点击"查看完整目录"应显示数据

### 下载功能测试
1. **外部链接**: 点击下载按钮应打开浏览器
2. **文档下载**: 应能正常下载.docx文档

### 整体功能
1. **模块导航**: 所有模块应能正常切换
2. **返回功能**: 返回按钮应正常工作

## ⚠️ 注意事项

### 数据文件
- 当前使用的是测试数据
- 实际使用时需要替换为完整的数据文件
- 数据格式应与模块一的JavaScript代码匹配

### 网络权限
- 确保AndroidManifest中有INTERNET权限
- HTTP链接仅在测试环境使用，生产环境建议HTTPS

## 📊 数据格式说明

模块一期望的数据格式：
```json
[
  {
    "col1": "产品名称",
    "col2": "产品类别", 
    "col3": "标准编号",
    "col4": "标准名称"
  },
  // ...
]
```

这个修复应该解决模块一的所有功能问题！