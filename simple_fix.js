// 简单修复：添加完善错误处理
const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'android-project', 'app', 'src', 'main', 'assets', 'www', 'module1_fixed_final_v4.html');

fs.readFile(filePath, 'utf8', (err, content) => {
    if (err) {
        console.error('读取文件失败:', err);
        return;
    }
    
    // 添加完善的错误处理
    content = content.replace(
        "fetch('complete_excel.json')\n                .then(response => response.json())",
        "fetch('complete_excel.json')\n                .then(response => {\n                    if (!response.ok) {\n                        throw new Error('数据加载失败: ' + response.status);\n                    }\n                    return response.json();\n                })"
    );
    
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error('写入文件失败:', err);
            return;
        }
        console.log('错误处理添加完成');
    });
});