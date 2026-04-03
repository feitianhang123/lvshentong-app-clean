# Android 项目结构检查清单

## 📁 必需的文件结构
```
android-project/
├── gradlew
├── gradlew.bat
├── build.gradle
├── settings.gradle
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties
└── app/
    ├── build.gradle
    ├── src/
    │   └── main/
    │       ├── AndroidManifest.xml
    │       ├── java/com/lvshentong/app/MainActivity.java
    │       ├── res/layout/activity_main.xml
    │       └── assets/www/ (所有网页文件)
    └── build/outputs/apk/debug/app-debug.apk
```

## 🔧 关键配置文件内容

### 1. gradle-wrapper.properties
```properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.7-bin.zip
```

### 2. build.gradle (项目级)
```gradle
plugins {
    id 'com.android.application' version '8.2.0' apply false
}
```

### 3. app/build.gradle
```gradle
android {
    compileSdk 34
    defaultConfig {
        applicationId "com.lvshentong.app"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }
}
```

### 4. AndroidManifest.xml
```xml
<manifest package="com.lvshentong.app">
    <uses-permission android:name="android.permission.INTERNET" />
    <application android:theme="@style/Theme.AppCompat.Light">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

## 🚀 GitHub Actions 构建流程

1. **推送代码到 master 分支**
2. **GitHub 自动触发构建**
3. **在 Actions 标签页查看进度**
4. **构建完成后下载 APK**

## 🔍 常见问题排查

- **Gradle 版本问题**: 更新 gradle-wrapper.properties
- **SDK 版本问题**: 检查 compileSdk/targetSdk 版本
- **权限问题**: 确保 gradlew 有执行权限
- **路径问题**: 确认文件路径正确

## 📊 构建状态检查
构建完成后，在 GitHub 仓库的 Actions 标签页查看：
- ✅ 绿色: 构建成功
- ❌ 红色: 构建失败（查看日志）
- ⏳ 黄色: 构建进行中