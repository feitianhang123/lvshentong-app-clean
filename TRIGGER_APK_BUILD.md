# 📦 触发APK构建指南

## 手动触发GitHub Action构建APK

由于自动触发需要GitHub Token，请按以下步骤手动触发：

### 方法一：通过GitHub网站
1. 访问仓库页面: https://github.com/feitianhang123/lvshentong-app-clean
2. 点击 "Actions" 标签
3. 选择 "Android APK Build" workflow
4. 点击 "Run workflow" 按钮
5. 选择构建类型（debug 或 release）
6. 点击 "Run workflow" 开始构建

### 方法二：通过Release触发
创建一个新的Release会自动触发构建：
1. 点击仓库页面的 "Releases"
2. 点击 "Draft a new release"
3. 填写版本号（如 v1.0.0）
4. 发布Release

## 📱 获取构建好的APK

构建完成后：
1. 回到 "Actions" 页面
2. 点击最新的构建运行
3. 在 "Artifacts" 部分下载 `green-food-app-apk`
4. 解压后获得APK文件

## 🔧 构建状态检查

- ✅ 代码已推送到GitHub
- ✅ GitHub Action配置已更新
- ✅ Android项目结构完整
- ✅ 最新的HTML文件已复制到assets

**现在可以手动触发GitHub Action来构建APK了！**