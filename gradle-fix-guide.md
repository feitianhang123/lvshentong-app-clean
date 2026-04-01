# Gradle 构建修复指南

## 🔧 修复的问题

### 1. Gradle版本兼容性问题
**原错误**: 
```
Build was configured to prefer settings repositories over project repositories 
but repository 'Google' was added by build file 'build.gradle'
```

**原因**:
- Gradle 8.x引入了新的仓库管理模式
- `settings.gradle` 中的 `repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)` 会阻止在build.gradle中定义仓库

**解决方案**:
将 `FAIL_ON_PROJECT_REPOS` 改为 `PREFER_PROJECT`：
```gradle
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.PREFER_PROJECT)
    repositories {
        google()
        mavenCentral()
    }
}
```

### 2. 构建命令问题
**原错误**: 直接在根目录构建失败

**解决方案**:
使用模块化构建命令：
```bash
gradle :app:assembleDebug
```

## ✅ 更新后的配置

### settings.gradle
```gradle
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.PREFER_PROJECT)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "GreenFoodApp"
include ':app'
```

### GitHub Actions配置
```yaml
- name: Build APK with Gradle
  run: |
    # 在项目根目录构建
    gradle :app:assembleDebug
```

## 🚀 立即执行的操作

```powershell
# 1. 进入项目目录
cd C:\Users\feiti\.openclaw\lvshentong-app-clean

# 2. 添加所有修改的文件
git add .github/workflows/android-ci.yml

git add settings.gradle

# 3. 提交更改
git commit -m "fix: 修复Gradle构建配置和GitHub Actions"

# 4. 推送到GitHub
git push origin master
```

## 📊 技术细节

### Gradle仓库管理模式
- **FAIL_ON_PROJECT_REPOS**: 阻止在build.gradle中定义仓库（严格模式）
- **PREFER_SETTINGS_REPOS**: 优先使用settings.gradle中的仓库
- **PREFER_PROJECT_REPOS**: 优先使用build.gradle中的仓库（宽松模式）

### 构建命令说明
- `gradle assembleDebug`: 构建所有模块的debug版本
- `gradle :app:assembleDebug`: 只构建app模块的debug版本

## 🎯 预期结果

修复后，构建应该能够：
1. ✅ 正确解析依赖仓库
2. ✅ 成功构建Android应用
3. ✅ 生成APK文件
4. ✅ 上传APK为artifact

## ⚠️ 注意事项

- 确保Android SDK版本兼容
- 确保所有依赖库可用
- 如果仍有问题，查看详细的构建日志