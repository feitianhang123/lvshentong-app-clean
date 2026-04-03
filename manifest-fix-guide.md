# AndroidManifest 修复指南

## 🔧 修复的问题

### 1. Android Gradle Plugin 新限制
**原错误**:
```
Incorrect package="com.lvshentong.app" found in source AndroidManifest.xml
Setting the namespace via the package attribute in the source AndroidManifest.xml is no longer supported.
Recommendation: remove package="com.lvshentong.app" from the source AndroidManifest.xml
```

**原因**:
- Android Gradle Plugin 8.x+ 不再支持在 AndroidManifest.xml 中设置 package 属性
- 必须在 build.gradle 中通过 namespace 属性设置包名

**解决方案**:
1. **从 AndroidManifest.xml 移除 package 属性**
2. **在 build.gradle 中正确设置 namespace**

### 2. 包名不一致问题
**原配置**:
- namespace: `com.greenfood.app`
- applicationId: `com.lvshentong.app`

**修复后**:
- namespace: `com.lvshentong.app`
- applicationId: `com.lvshentong.app`

## ✅ 更新后的配置

### AndroidManifest.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- 移除了 package 属性 -->
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@android:style/Theme.Material.Light">
        
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
    </application>

</manifest>
```

### app/build.gradle
```gradle
android {
    namespace 'com.lvshentong.app'  // 修复为一致的包名
    compileSdk 34

    defaultConfig {
        applicationId "com.lvshentong.app"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }
    // ...
}
```

## 🚀 立即执行的操作

```powershell
# 1. 进入项目目录
cd C:\Users\feiti\.openclaw\lvshentong-app-clean

# 2. 添加修改的文件
git add app/src/main/AndroidManifest.xml
git add app/build.gradle

# 3. 提交更改
git commit -m "fix: 修复AndroidManifest和build.gradle配置"

# 4. 推送到GitHub
git push origin master
```

## 📊 技术细节

### namespace vs applicationId
- **namespace**: 用于R类生成和资源访问（必须设置）
- **applicationId**: 应用的实际包名（用于发布）

### Android Gradle Plugin 8.x+ 变化
1. 不再支持在 AndroidManifest.xml 中设置 package
2. 必须在 build.gradle 中通过 namespace 设置
3. 保持 namespace 和 applicationId 一致以避免混淆

## 🎯 预期结果

修复后，构建应该能够：
1. ✅ 正确解析AndroidManifest
2. ✅ 成功构建APK文件
3. ✅ 生成正确的R类
4. ✅ 应用包名为 `com.lvshentong.app`

## ⚠️ 注意事项

- 确保所有Java文件在正确的包路径下
- 确保资源引用正确
- 如果仍有问题，检查是否有其他AndroidManifest文件