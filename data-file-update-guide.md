# 数据文件更新指南

## 🔧 修复的问题

### 1. 使用正确的数据文件
- **之前**: 使用测试数据（10条记录）
- **现在**: 使用完整的数据文件（167,926字节，完整数据）

### 2. 文件位置确认
- **源文件**: `C:\Users\feiti\.openclaw\workspace\complete_excel.json`
- **目标位置**: `C:\Users\feiti\.openclaw\lvshentong-app-clean\app\src\main\assets\www\complete_excel.json`

## ✅ 已完成的操作

### 1. 文件复制
将正确的数据文件从workspace复制到Android项目：
```powershell
Copy-Item "C:\Users\feiti\.openclaw\workspace\complete_excel.json" "C:\Users\feiti\.openclaw\lvshentong-app-clean\app\src\main\assets\www\complete_excel.json" -Force
```

### 2. 文件验证
- **文件大小**: 167,926字节（完整数据）
- **文件位置**: `app/src/main/assets/www/complete_excel.json`

## 📁 文件状态

### 当前使用的文件
```
app/src/main/assets/www/
├── complete_excel.json      # 完整数据文件 (167KB)
├── index_fixed.html         # 主页
├── module1_fixed_final_v4.html  # 模块一
├── module2_current_standards.html  # 模块二
├── module3_final.html       # 模块三
└── standards_data.js        # 模块二数据
```

## 🚀 立即执行的操作

```powershell
# 1. 进入项目目录
cd C:\Users\feiti\.openclaw\lvshentong-app-clean

# 2. 添加正确的数据文件
git add app/src/main/assets/www/complete_excel.json

# 3. 提交更改
git commit -m "fix: 使用正确的complete_excel.json数据文件"

# 4. 推送到GitHub
git push origin master
```

## 🎯 预期结果

使用完整数据文件后，模块一应该能够：
1. ✅ 加载完整的标准目录数据
2. ✅ 实现准确的搜索功能
3. ✅ 显示真实的产品信息
4. ✅ 提供完整的标准目录内容

## 🔍 测试要点

### 模块一功能测试
1. **搜索测试**: 尝试搜索真实的产品名称
2. **数据验证**: 确认显示的信息与数据文件匹配
3. **性能测试**: 确保大数据量下的搜索性能

### 整体功能验证
1. **数据完整性**: 所有产品都应能被搜索到
2. **功能完整性**: 搜索、显示、导航功能正常
3. **用户体验**: 界面响应流畅

## ⚠️ 注意事项

### 数据文件维护
- 保持数据文件与源代码同步
- 定期更新数据文件内容
- 确保数据格式与代码兼容

### 性能考虑
- 大数据文件可能影响加载性能
- 考虑数据分页或懒加载优化
- 监控实际运行性能

## 📊 数据文件信息

- **文件大小**: 167,926字节
- **记录数量**: 完整的数据记录
- **数据格式**: JSON数组格式
- **内容**: 绿色食品标准目录完整数据

现在模块一将使用完整的数据文件，所有功能应该都能正常工作了！