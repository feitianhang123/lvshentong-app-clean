// 绿色食品产品适用标准目录数据（精简版，用于前端搜索）
const greenFoodStandards = {
    "大豆": {standard: "NY/T 285", number: "绿色食品 豆类"},
    "黄豆": {standard: "NY/T 285", number: "绿色食品 豆类"},
    "黑豆": {standard: "NY/T 285", number: "绿色食品 豆类"},
    "绿豆": {standard: "NY/T 285", number: "绿色食品 豆类"},
    "绿茶": {standard: "NY/T 288", number: "绿色食品 茶叶"},
    "红茶": {standard: "NY/T 288", number: "绿色食品 茶叶"},
    "玉米": {standard: "NY/T 418", number: "绿色食品 玉米及玉米制品"},
    "大米": {standard: "NY/T 419", number: "绿色食品 稻米"},
    "糙米": {standard: "NY/T 419", number: "绿色食品 稻米"},
    "花生": {standard: "NY/T 420", number: "绿色食品 花生及花生制品"},
    "小麦": {standard: "NY/T 421", number: "绿色食品 小麦及小麦粉"},
    "柑橘": {standard: "NY/T 426", number: "绿色食品 柑橘类水果"},
    "西瓜": {standard: "NY/T 427", number: "绿色食品 西甜瓜"},
    "苹果": {standard: "NY/T 428", number: "绿色食品 苹果"},
    "梨": {standard: "NY/T 429", number: "绿色食品 梨"},
    "葡萄": {standard: "NY/T 430", number: "绿色食品 葡萄"},
    "番茄": {standard: "NY/T 655", number: "绿色食品 茄果类蔬菜"},
    "黄瓜": {standard: "NY/T 747", number: "绿色食品 瓜类蔬菜"},
    "白菜": {standard: "NY/T 743", number: "绿色食品 白菜类蔬菜"},
    "猪肉": {standard: "NY/T 279", number: "绿色食品 畜肉"},
    "牛肉": {standard: "NY/T 279", number: "绿色食品 畜肉"},
    "羊肉": {standard: "NY/T 279", number: "绿色食品 畜肉"},
    "鸡肉": {standard: "NY/T 753", number: "绿色食品 禽肉"},
    "鸡蛋": {standard: "NY/T 754", number: "绿色食品 蛋与蛋制品"},
    "牛奶": {standard: "NY/T 657", number: "绿色食品 乳制品"},
    "对虾": {standard: "NY/T 840", number: "绿色食品 虾"},
    "鱼类": {standard: "NY/T 841", number: "绿色食品 鱼"},
    "蜂蜜": {standard: "NY/T 752", number: "绿色食品 蜂产品"}
};

// 官方Excel文件下载链接
const excelFileUrl = "http://www.greenfood.agri.cn/ywzn/lssp/txbz/lsspcpsybzml/202306/P020230608368777204927.xlsx";

// 搜索产品函数
function searchProduct() {
    const searchTerm = document.getElementById('searchInput').value.trim();
    if (!searchTerm) {
        alert('请输入产品名称');
        return;
    }

    const searchSection = document.getElementById('searchSection');
    const resultSection = document.getElementById('resultSection');
    const successResult = document.getElementById('successResult');
    const errorResult = document.getElementById('errorResult');
    const successDesc = document.getElementById('successDesc');

    // 显示加载中
    searchSection.style.display = 'none';
    resultSection.style.display = 'block';
    successResult.style.display = 'none';
    errorResult.style.display = 'none';
    successDesc.textContent = '搜索中...';

    // 模拟网络延迟（500ms）
    setTimeout(() => {
        // 在前端进行搜索
        const results = [];
        
        // 精确匹配
        if (greenFoodStandards[searchTerm]) {
            results.push({
                product: searchTerm,
                standard: greenFoodStandards[searchTerm].standard,
                number: greenFoodStandards[searchTerm].number
            });
        }
        
        // 模糊匹配（包含搜索）
        for (const [product, info] of Object.entries(greenFoodStandards)) {
            if (product.includes(searchTerm) && product !== searchTerm) {
                results.push({
                    product: product,
                    standard: info.standard,
                    number: info.number
                });
            }
        }

        if (results.length > 0) {
            successResult.style.display = 'block';
            errorResult.style.display = 'none';
            
            if (results.length === 1) {
                const result = results[0];
                successDesc.innerHTML = `
                    <div style="margin-bottom: 10px;">
                        <strong>找到产品：</strong>${result.product}
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>标准名称：</strong>${result.number}
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>标准号：</strong>${result.standard}
                    </div>
                    <div style="color: #666; font-size: 12px;">
                        注：详细信息请下载完整标准目录查阅
                    </div>
                `;
            } else {
                successDesc.innerHTML = `<div style="margin-bottom: 10px;"><strong>找到${results.length}个匹配产品：</strong></div>`;
                results.forEach((result, index) => {
                    successDesc.innerHTML += `
                        <div style="margin-bottom: 8px; padding-left: 10px; border-left: 3px solid #4CAF50;">
                            <strong>${index + 1}. ${result.product}</strong><br>
                            <small>标准：${result.number} (${result.standard})</small>
                        </div>
                    `;
                });
            }
        } else {
            successResult.style.display = 'none';
            errorResult.style.display = 'block';
            document.querySelector('.result-desc').textContent = 
                '此产品不在绿色食品产品适用标准目录（2023版）之内，如果为别名可重试其他名称或下载目录自行核对。';
        }
    }, 500);
}

// 下载Excel文件函数
function downloadExcelFile() {
    // 创建隐藏的下载链接
    const link = document.createElement('a');
    link.href = excelFileUrl;
    link.download = '绿色食品产品适用标准目录(2023版).xlsx';
    link.target = '_blank';
    
    // 添加到文档并触发点击
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // 显示下载提示
    alert('正在下载绿色食品产品适用标准目录(2023版).xlsx');
}

// 显示标准目录内容（现在直接下载文件）
function showStandardContent() {
    downloadExcelFile();
}

// 返回搜索页面
function backToSearch() {
    document.getElementById('searchSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('searchInput').value = '';
}

// 处理回车键搜索
function handleEnter(event) {
    if (event.key === 'Enter') {
        searchProduct();
    }
}

// 聚焦搜索框
function focusSearch() {
    document.getElementById('searchInput').focus();
}