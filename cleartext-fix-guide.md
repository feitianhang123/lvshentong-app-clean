# HTTP明文传输修复指南

## 🔧 修复的问题

### 1. HTTP明文传输被阻止
**错误信息**:
```
net::ERR_CLEARTEXT_NOT_PERMITTED
```

**原因**:
- Android 9.0+ (API 28+) 默认阻止HTTP明文传输
- 需要显式允许HTTP访问

### 2. 模块一链接问题
虽然链接已修复为相对路径，但可能还有其他问题

## ✅ 解决方案

### 1. 允许HTTP明文传输
在 `AndroidManifest.xml` 中添加：
```xml
<application
    android:usesCleartextTraffic="true"
    ...>
```

### 2. 网络安全性配置（可选）
创建网络安全配置文件：

**res/xml/network_security_config.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">greenfood.agri.cn</domain>
    </domain-config>
    <base-config cleartextTrafficPermitted="true" />
</network-security-config>
```

**AndroidManifest.xml**
```xml
<application
    android:networkSecurityConfig="@xml/network_security_config"
    ...>
```

## 📁 修改的文件

### 1. AndroidManifest.xml
```xml
<application
    android:usesCleartextTraffic="true"
    android:allowBackup="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:theme="@android:style/Theme.Material.Light">
```

## 🚀 立即执行的操作

```powershell
# 1. 进入项目目录
cd C:\Users\feiti\.openclaw\lvshentong-app-clean

# 2. 添加修改的文件
git add app/src/main/AndroidManifest.xml

# 3. 提交更改
git commit -m "fix: 允许HTTP明文传输解决CLEARTEXT_NOT_PERMITTED错误"

# 4. 推送到GitHub
git push origin master
```

## 📊 Android网络安全策略

### Android 9.0+ 变化
- **默认阻止HTTP**: 保护用户数据安全
- **需要显式允许**: `android:usesCleartextTraffic="true"`
- **或使用HTTPS**: 推荐使用加密连接

### 适用场景
- 访问政府网站（很多仍使用HTTP）
- 内部网络资源
- 测试环境

## 🎯 预期结果

修复后，应用应该能够：
1. ✅ 正常打开HTTP链接
2. ✅ 下载标准文档
3. ✅ 访问所有外部资源
4. ✅ 不再出现CLEARTEXT_NOT_PERMITTED错误

## ⚠️ 注意事项

### 安全性考虑
- HTTP传输不安全，可能被窃听
- 建议最终使用HTTPS链接
- 仅用于测试或内部网络

### 兼容性
- Android 9.0+ 需要此配置
- Android 8.1及以下版本默认允许HTTP

## 🔍 测试要点

1. **模块一测试**: 点击"产品目录"
2. **下载测试**: 点击任意标准的"下载标准"按钮
3. **外部链接**: 所有HTTP链接都应正常工作

这个修复应该解决所有网络访问问题！