// 为模块一添加调试信息
const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'android-project', 'app', 'src', 'main', 'assets', 'www', 'module1_fixed_final_v4.html');

fs.readFile(filePath, 'utf8', (err, content) => {
    if (err) {
        console.error('读取文件失败:', err);
        return;
    }
    
    // 添加调试信息
    const debugCode = `
                // 调试信息
                console.log('数据文件路径:', window.location.href + 'complete_excel.json');
                console.log('数据加载状态: 开始加载');
    `;
    
    // 替换数据加载部分
    const newContent = content.replace(
        "fetch('complete_excel.json')",
        "fetch('complete_excel.json')" + debugCode
    );
    
    fs.writeFile(filePath, newContent, 'utf8', (err) => {
        if (err) {
            console.error('写入文件失败:', err);
            return;
        }
        console.log('调试信息添加成功');
    });
});