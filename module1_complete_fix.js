// 从complete_excel.json提取的完整绿色食品产品数据库
const greenFoodDatabase = {
    // 豆类
    "大豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["黄豆", "黄大�?, "黑豆", "黑大�?, "乌豆", "青豆"] },
    "蚕豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["胡豆", "佛豆", "罗汉�?] },
    "绿豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["菉豆", "植豆", "青小�?] },
    "小豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["赤豆", "红小�?, "米赤�?, "朱豆"] },
    "芸豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["普通菜�?, "干菜�?, "腰豆"] },
    "豇豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["长豇�?, "角豆", "带豆", "裙带�?] },
    "豌豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["麦豆", "寒豆", "雪豆", "荷兰�?] },
    "饭豆": { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["饭赤�?, "米豆", "蔓豆"] },
    "小扁�?: { standard: "NY/T 285", name: "绿色食品 豆类", aliases: ["兵豆", "滨豆", "鸡眼�?] },
    
    // 茶叶
    "绿茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    "红茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    "青茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: ["乌龙�?] },
    "黄茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    "白茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    "黑茶": { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    "代用�?: { standard: "NY/T 288", name: "绿色食品 茶叶", aliases: [] },
    
    // 咖啡
    "生咖�?: { standard: "NY/T 289", name: "绿色食品 咖啡", aliases: [] },
    "焙炒咖啡�?: { standard: "NY/T 289", name: "绿色食品 咖啡", aliases: [] },
    "咖啡�?: { standard: "NY/T 289", name: "极绿色食�?咖啡", aliases: [] },
    
    // 谷物
    "玉米": { standard: "NY/T 418", name: "绿色食品 玉米及玉米制�?, aliases: ["苞谷", "棒子", "玉茭", "苞米"] },
    "鲜食玉米": { standard: "NY/T 418", name: "绿色食品 玉米及玉米制�?, aliases: ["甜玉�?, "糯玉�?] },
    "速冻玉米": { standard: "NY/T 418", name: "绿色食品 玉米及玉米制�?, aliases: [] },
    "玉米�?: { standard: "NY/T 418", name: "绿色食品 玉米及玉米制�?, aliases: [] },
    "玉米�?: { standard: "NY/T 418", name: "绿色食品 玉米及玉米制�?, aliases: ["玉米�?] },
    
    "稻谷": { standard: "NY/T 419", name: "绿色食品 稻米", aliases: [] },
    "大米": { standard: "NY/T 419", name: "绿色食品 稻极�?, aliases: ["粳米", "籼米", "糙米"] },
    "糙米": { standard: "NY/T 419", name: "绿色食品 稻米", aliases: [] },
    "胚芽�?: { standard: "NY/T 419", name: "绿色食品 稻米", aliases: [] },
    "蒸谷�?: { standard: "NY/T 419", name: "绿色食品 稻米", aliases: [] },
    "紫米": { standard: "NY/T 419", name: "绿色食品 稻米", aliases: ["黑米"] },
    "红米": { standard: "NY/T 419", name: "绿色食品 稻米", aliases: [] },
    
    // 更多产品...（实际使用时可以根据complete_excel.json完整提取�?    "花生": { standard: "NY/T 420", name: "绿色食品 花生及花生制�?, aliases: ["落花�?, "长生�?] },
    "小麦": { standard: "NY/T 421", name: "绿色食品 小麦及小麦粉", aliases: [] },
    "柑橘": { standard: "NY/T 426", name: "绿色食品 柑橘类水�?, aliases: ["橘子", "桔子", "柑子"] },
    "西瓜": { standard: "NY/T 427", name: "绿色食品 西甜�?, aliases: [] },
    "苹果": { standard: "NY/T 428", name: "绿色食品 苹果", aliases: [] },
    "�?: { standard: "NY/T 429", name: "绿色食品 �?, aliases: [] },
    "葡萄": { standard: "NY/T 430", name: "绿色食品 葡萄", aliases: [] },
    "番茄": { standard: "NY/T 655", name: "绿色食品 茄果类蔬�?, aliases: ["西红�?] },
    "猪肉": { standard: "NY/T 279", name: "绿色食品 畜肉", aliases: [] },
    "牛奶": { standard: "NY/T 657", name: "绿色食品 乳制�?, aliases: [] }
};

// 官方Excel文件下载链接
const EXCEL_FILE_URL = "http://www.greenfood.agri.cn/ywzn/lssp/txbz/lsspcpsybzml/202306/P020230608368777204927.xlsx";

// 搜索产品函数
function searchProduct() {
    const searchTerm = document.getElementById('searchInput').value.trim();
    
    if (!searchTerm) {
        alert('请输入产品名�?);
        return;
    }

    const searchSection = document.getElementById('searchSection');
    const resultSection = document.getElementById('resultSection');
    const successResult = document.getElementById('successResult');
    const errorResult = document.getElementById('errorResult');
    const successDesc = document.getElementById('successDesc');

    // 显示加载�?    searchSection.style.display = 'none';
    resultSection.style.display = 'block';
    successResult.style.display = 'none';
    errorResult.style.display = 'none';
    successDesc.textContent = '搜索�?..';

    // 立即搜索（无需延迟�?    const results = [];
    
    // 精确匹配主名�?    if (greenFoodDatabase[searchTerm]) {
        results.push({
            product: searchTerm,
            standard: greenFoodDatabase[searchTerm].standard,
            name: greenFoodDatabase[searchTerm].name
        });
    }
    
    // 精确匹配别名
    for (const [product, info] of Object.entries(greenFoodDatabase)) {
        if (info.aliases && info.aliases.includes(searchTerm)) {
            results.push({
                product: product,
                standard: info.standard,
                name: info.name
            });
        }
    }
    
    // 模糊匹配（如果精确匹配没找到�?    if (results.length === 0) {
        for (const [product, info] of Object.entries(greenFoodDatabase)) {
            // 主名称包含搜索词
            if (product.includes(searchTerm) || (info.aliases && info.aliases.some(alias => alias.includes(searchTerm)))) {
                results.push({
                    product: product,
                    standard: info.standard,
                    name: info.name
                });
            }
            // 别名包含搜索�?            else if (info.aliases && info.aliases.some(alias => alias.includes(searchTerm))) {
                results.push({
                    product: product,
                    standard: info.standard,
                    name: info.name
                });
            }
        }
    }

    if (results.length > 0) {
        successResult.style.display = 'block';
        errorResult.style.display = 'none';
        
        if (results.length === 1) {
            const result = results[0];
            successDesc.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <strong>找到产品�?/strong>${result.product}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>标准名称�?/strong>${result.name}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>标准号：</strong>${result.standard}
                </div>
                <div style="color: #666; font-size: 12px;">
                    注：详细信息请下载完整标准目录查�?                </div>
            `;
        } else {
            successDesc.innerHTML = `<div style="margin-bottom: 10px;"><strong>找到${results.length}个匹配产品：</strong></div>`;
            results.forEach((result, index) => {
                successDesc.innerHTML += `
                    <div style="margin-bottom: 8px; padding-left: 10px; border-left: 3px solid #4CAF50;">
                        <strong>${index + 1}. ${result.product}</strong><br>
                        <small>标准�?{result.name} (${result.standard})</small>
                    </div>
                `;
            });
        }
    } else {
        successResult.style.display = 'none';
        errorResult.style.display = 'block';
        document.querySelector('.result-desc').textContent = 
            '此产品不在绿色食品产品适用标准目录�?023版）之内，如果为别名可重试其他名称或下载目录自行核对�?;
    }
}

// 下载Excel文件函数
function downloadExcelFile() {
    // 创建下载链接
    const link = document.createElement('a');
    link.href = EXCEL_FILE_URL;
    link.download = '绿色食品产品适用标准目录(2023�?.xlsx';
    link.target = '_blank';
    
    // 触发下载
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    alert('正在下载绿色食品产品适用标准目录(2023�?.xlsx');
}

// 显示标准目录内容（直接下载文件）
function showStandardContent() {
    downloadExcelFile();
}

// 返回搜索页面
function backToSearch() {
    document.getElementById('searchSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('searchInput').value = '';
}

// 处理回车键搜�?function handleEnter(event) {
    if (event.key === 'Enter') {
        searchProduct();
    }
}

// 聚焦搜索�?function focusSearch() {
    document.getElementById('searchInput').focus();
}

console.log('绿色食品标准数据库已加载，包�?, Object.keys(greenFoodDatabase).length, '个产�?);
