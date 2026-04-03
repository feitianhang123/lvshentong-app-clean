// 标准数据提取工具
const fs = require('fs');
const path = require('path');

// 读取标准文本文件
const textContent = fs.readFileSync(
    'C:\\Users\\feiti\\.openclaw\\media\\qqbot\\downloads\\1903527544\\CF252E5B029422FD7EBABE9FE5D83DBE\\db31ca35-0e2c-42f5-ab16-c0e7bc5a454e.txt', 
    'utf8'
);

// 提取标准信息
function extractStandards(content) {
    const standards = [];
    const lines = content.split('\n');
    
    const pattern = /《(.+?)》（(.+?)）下载地址(.+)/;
    
    lines.forEach(line => {
        line = line.trim();
        if (line && line.includes('下载地址')) {
            const match = line.match(pattern);
            if (match) {
                const name = match[1].trim();
                const code = match[2].trim();
                let url = match[3].trim();
                
                // 清理URL
                url = url.replace(/^[：:\s]+/, '');
                
                // 确定类型
                let type = 'product';
                if (name.includes('准则') || name.includes('规范') || name.includes('规则')) {
                    type = 'guideline';
                }
                
                standards.push({
                    name,
                    code,
                    type,
                    url
                });
            }
        }
    });
    
    return standards;
}

// 提取标准数据
const standards = extractStandards(textContent);

// 统计信息
const productStandards = standards.filter(s => s.type === 'product');
const guidelineStandards = standards.filter(s => s.type === 'guideline');

console.log(`总共提取标准: ${standards.length}`);
console.log(`产品标准: ${productStandards.length}`);
console.log(`准则标准: ${guidelineStandards.length}`);

// 生成JavaScript数据文件
const jsContent = `const standardsData = ${JSON.stringify(standards, null, 2)};

// 统计信息
const totalStandards = standardsData.length;
const productStandards = standardsData.filter(s => s.type === 'product').length;
const guidelineStandards = standardsData.filter(s => s.type === 'guideline').length;

console.log('标准数据加载完成');
console.log('总标准数:', totalStandards);
console.log('产品标准:', productStandards);
console.log('准则标准:', guidelineStandards);
`;

// 保存数据文件
fs.writeFileSync('standards_data.js', jsContent);

console.log('数据文件已生成: standards_data.js');

// 显示前几个标准作为示例
console.log('\n示例数据:');
standards.slice(0, 5).forEach((standard, index) => {
    console.log(`${index + 1}. ${standard.name} (${standard.code}) - ${standard.type}`);
});