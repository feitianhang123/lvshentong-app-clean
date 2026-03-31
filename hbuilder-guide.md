# 📱 HBuilder 打包指南 - 绿申通

## 🎯 为什么推荐 HBuilder？
- ✅ **全中文界面** - 无需担心语言问题
- ✅ **国内服务器** - 下载速度快
- ✅ **一键云打包** - 无需配置复杂环境
- ✅ **免费使用** - 基础功能完全免费

## 🚀 详细步骤

### 第一步：下载安装
1. 访问: https://www.dcloud.io/hbuilderx.html
2. 下载 Windows 版本
3. 安装并打开 HBuilderX

### 第二步：打开项目
1. 点击菜单 "文件" → "打开目录"
2. 选择 `cordova-project` 文件夹
3. 点击 "选择文件夹"

### 第三步：云打包
1. 点击顶部菜单 "发行"
2. 选择 "原生App-云打包"
3. 在弹出的窗口中设置：
   - **应用名称**: 绿申通
   - **AppID**: com.lvshentong.app
   - **版本号**: 1.0.0
   - **Android包名**: com.lvshentong.app
4. 点击 "打包"

### 第四步：等待并下载
1. 等待云端打包完成（约5-10分钟）
2. 打包完成后点击 "下载"
3. 获得 `绿申通_1.0.0.apk`

## ⚙️ 配置说明

### 基本配置
```json
{
  "name": "绿申通",
  "appid": "com.lvshentong.app", 
  "versionName": "1.0.0",
  "versionCode": 1
}
```

### 权限配置（可选）
```json
{
  "permissions": {
    "Android": [
      "<uses-permission android:name=\"android.permission.INTERNET\"/>",
      "<uses-permission android:name=\"android.permission.ACCESS_NETWORK_STATE\"/>"
    ]
  }
}
```

## 📋 文件准备

确保 `cordova-project` 文件夹包含：
```
www/
├── index.html              # 主页
├── module1_fixed_final_v4.html    # 模块一
├── module2_current_standards.html # 模块二
├── module3_final.html      # 模块三
└── standards_data.js       # 数据文件
```

## 🎨 应用图标

如果你想自定义图标：
1. 在 HBuilder 中右键项目
2. 选择 "manifest.json"
3. 在 "图标配置" 中上传你的图标

## 📞 常见问题

### Q: 打包失败怎么办？
A: 检查网络连接，或尝试重新打包

### Q: 如何更新应用？
A: 修改版本号后重新云打包

### Q: 支持iOS打包吗？
A: 支持，但需要苹果开发者账号

## 💡 提示
- 第一次使用可能需要注册 DCloud 账号
- 云打包是完全在云端完成的，不需要本地环境
- 打包完成后可以扫码直接在手机上安装测试

---
**使用 HBuilder 是最简单的方式，特别适合不熟悉英文界面的用户！** 🎯