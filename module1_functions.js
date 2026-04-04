// 绿色食品产品适用标准目录搜索功能

// Excel文件数据结构常量
const EXCEL_FILE_PATH = "绿色食品产品适用标准目录（2023版）.xlsx";

// 搜索产品函数
function searchProduct() {
    const searchTerm = document.getElementById('searchInput').value.trim();
    
    if (!searchTerm) {
        alert('请输入产品名称');
        return;
    }

    const searchSection = document.getElementById('searchSection');
    const resultSection = document.getElementById('resultSection');
    const loading = document.getElementById('loading');
    const successResult = document.getElementById('successResult');
    const errorResult = document.getElementById('errorResult');
    const successDesc = document.getElementById('successDesc');
    const errorDesc = document.getElementById('errorDesc');

    // 显示加载中
    searchSection.style.display = 'none';
    resultSection.style.display = 'block';
    successResult.style.display = 'none';
    errorResult.style.display = 'none';
    loading.style.display = 'block';

    // 模拟Excel文件搜索（实际实现需要后端支持）
    setTimeout(() => {
        loading.style.display = 'none';
        
        // 这里应该是实际的Excel搜索逻辑
        // 由于浏览器无法直接读取本地Excel文件，这里使用模拟数据
        const found = simulateExcelSearch(searchTerm);
        
        if (found) {
            successResult.style.display = 'block';
            errorResult.style.display = 'none';
            successDesc.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <strong>产品名称：</strong>${searchTerm}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>所在行数：</strong>第${found.row}行
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>标准名称：</strong>${found.standardName}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>标准号：</strong>${found.standardNumber}
                </div>
                <div style="color: #666; font-size: 12px;">
                    详细信息请查阅完整的标准目录文件
                </div>
            `;
        } else {
            successResult.style.display = 'none';
            errorResult.style.display = 'block';
            errorDesc.textContent = '申报产品不在绿色食品使用标准目录内，暂时无法申报绿色食品。';
        }
    }, 1000);
}

// 模拟Excel搜索函数（实际应用中需要后端处理Excel文件）
function simulateExcelSearch(productName) {
    // 模拟一些常见产品的搜索结果
    const productDatabase = {
        "大豆": { row: 3, standardName: "绿色食品 豆类", standardNumber: "NY/T285-2021" },
        "玉米": { row: 18, standardName: "绿色食品 玉米及玉米制品", standardNumber: "NY/T418-2023" },
        "大米": { row: 24, standardName: "绿色食品 稻米", standardNumber: "NY/T419-2021" },
        "花生": { row: 30, standardName: "绿色食品 花生及花生制品", standardNumber: "NY/T420-2017" },
        "小麦": { row: 36, standardName: "绿色食品 小麦及小麦粉", standardNumber: "NY/T421-2021" },
        "绿茶": { row: 42, standardName: "绿色食品 茶叶", standardNumber: "NY/T288-2018" },
        "红茶": { row: 48, standardName: "绿色食品 茶叶", standardNumber: "NY/T288-2018" },
        "苹果": { row: 54, standardName: "绿色食品 苹果", standardNumber: "NY/T428-2018" },
        "梨": { row: 60, standardName: "绿色食品 梨", standardNumber: "NY/T429-2018" },
        "葡萄": { row: 66, standardName: "绿色食品 葡萄", standardNumber: "NY/T430-2018" },
        "番茄": { row: 72, standardName: "绿色食品 茄果类蔬菜", standardNumber: "NY/T655-2020" },
        "黄瓜": { row: 78, standardName: "绿色食品 瓜类蔬菜", standardNumber: "NY/T747-2020" },
        "白菜": { row: 84, standardName: "绿色食品 白菜类蔬菜", standardNumber: "NY/T743-2020" },
        "牛肉": { row: 90, standardName: "绿色食品 畜肉", standardNumber: "NY/T2799-2023" },
        "猪肉": { row: 96, standardName: "绿色食品 畜肉", standardNumber: "NY/T2799-2023" },
        "羊肉": { row: 102, standardName: "绿色食品 畜肉", standardNumber: "NY/T2799-2023" },
        "牛奶": { row: 108, standardName: "绿色食品 乳与乳制品", standardNumber: "NY/T657-2021" },
        "鸡蛋": { row: 114, standardName: "绿色食品 蛋与蛋制品", standardNumber: "NY/T754-2021" }
    };
    
    return productDatabase[productName] || null;
}

// 显示标准目录内容
function showStandardContent() {
    alert('正在打开绿色食品产品适用标准目录（2023版）...\n\n由于技术限制，请手动打开Excel文件进行查看。');
    
    // 在实际应用中，这里应该打开Excel文件
    // 由于浏览器安全限制，无法直接打开本地Excel文件
    // 需要用户手动操作或使用专门的Excel查看器
}

// 返回搜索页面
function backToSearch() {
    document.getElementById('searchSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('searchInput').value = '';
}

// 处理回车键
function handleEnter(event) {
    if (event.key === 'Enter') {
        searchProduct();
    }
}

console.log('模块一功能已加载');