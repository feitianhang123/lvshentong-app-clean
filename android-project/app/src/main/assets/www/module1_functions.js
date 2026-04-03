// 模块一功能实现 - 独立JavaScript文件

// 全局数据变量
let excelData = [];

// 辅助函数：清理数据，去掉"nan"文字
function cleanData(value) {
    if (!value || value === 'nan' || value === 'NaN' || value.trim() === '') {
        return '';
    }
    return value;
}

// 辅助函数：检查是否有实际内容（非空且不是nan）
function hasContent(value) {
    return value && value !== 'nan' && value !== 'NaN' && value.trim() !== '';
}

// 加载数据函数
async function loadExcelData() {
    try {
        console.log('开始加载数据...');
        const response = await fetch('complete_excel.json');
        
        if (!response.ok) {
            throw new Error(`HTTP错误: ${response.status}`);
        }
        
        const data = await response.json();
        excelData = data;
        
        // 预处理数据：清理所有"nan"值
        excelData.forEach(row => {
            row.col1 = cleanData(row.col1);
            row.col2 = cleanData(row.col2);
            row.col3 = cleanData(row.col3);
            row.col4 = clean极 content length, truncating to 100KB. Use edit with offset/limit for large files.