// 模块一修复补丁
// 解决数据加载和事件绑定问题

const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'android-project', 'app', 'src', 'main', 'assets', 'www', 'module1_fixed_final_v4.html');

fs.readFile(filePath, 'utf8', (err, content) => {
    if (err) {
        console.error('读取文件失败:', err);
        return;
    }
    
    console.log('修复模块一数据加载问题...');
    
    // 修复fetch调用，添加错误处理
    content = content.replace(
        "fetch('complete_excel.json')\n                .then(response => response.json())",
        "fetch('complete_excel.json')\n                .then(response => {\n                    if (!response.ok) {\n                        throw new Error('HTTP错误: ' + response.status);\n                    }\n                    return response.json();\n                })"
    );
    
    // 添加数据加载状态检查
    content = content.replace(
        "console.log('事件监听器设置完成');",
        "console.log('事件监听器设置完成');\n                    \n                    // 启用界面元素\n                    document.getElementById('searchBtn').disabled = false;\n                    document.getElementById('dataCard').style.cursor = 'pointer';\n                    document.getElementById('dataCard').style.opacity = '1';"
    );
    
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error('写入文件失败:', err);
            return;
        }
        console.log('模块一修复完成');
    });
});