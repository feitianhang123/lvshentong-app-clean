#!/usr/bin/env python3
"""
监控GitHub Actions APK构建进度
"""

import requests
import time
import json

def check_build_status():
    """检查构建状态"""
    url = "https://api.github.com/repos/feitianhang123/lvshentong-app-clean/actions/runs"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if "workflow_runs" in data and len(data["workflow_runs"]) > 0:
            latest_run = data["workflow_runs"][0]
            return {
                "id": latest_run["id"],
                "name": latest_run["name"],
                "status": latest_run["status"],
                "conclusion": latest_run.get("conclusion", "pending"),
                "created_at": latest_run["created_at"],
                "html_url": latest_run["html_url"]
            }
    except Exception as e:
        print(f"检查状态出错: {e}")
    
    return None

def main():
    """主函数"""
    print("监控GitHub Actions APK构建进度")
    print("=" * 50)
    
    # 初始检查
    status = check_build_status()
    if status:
        print(f"构建ID: {status['id']}")
        print(f"工作流: {status['name']}")
        print(f"状态: {status['status']}")
        print(f"开始时间: {status['created_at']}")
        print(f"详情页面: {status['html_url']}")
        print()
    
    # 持续监控
    print("开始监控构建进度...")
    print("预计构建时间: 5-15分钟")
    print("=" * 50)
    
    for i in range(30):  # 监控30次，每次间隔30秒
        status = check_build_status()
        if status:
            print(f"[{i+1}/30] 状态: {status['status']} - 结论: {status['conclusion']}")
            
            if status['status'] == 'completed':
                if status['conclusion'] == 'success':
                    print("✅ 构建成功完成!")
                    print("📦 APK文件可在GitHub Actions页面下载")
                    print(f"🔗 下载页面: {status['html_url']}")
                    break
                else:
                    print(f"❌ 构建失败: {status['conclusion']}")
                    break
        
        time.sleep(30)  # 等待30秒
    
    print("\n监控结束")

if __name__ == "__main__":
    main()