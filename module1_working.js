// 绿色食品产品数据库
const greenFoodDatabase = {
    "大豆": { standard: "NY/T 285", name: "绿色食品 豆类" },
    "牛肉": { standard: "NY/T 279", name: "绿色食品 畜肉" },
    "牛奶": { standard: "NY/T 657", name: "绿色食品 乳制品" },
    "绿茶": { standard: "NY/T 288", name: "绿色食品 茶叶" },
    "苹果": { standard: "NY/T 428", name: "绿色食品 苹果" }
};

const EXCEL_FILE_URL = "http://www.greenfood.agri.cn/ywzn/lssp/txbz/lsspcpsybzml/202306/P020230608368777204927.xlsx";

// 搜索产品函数
function searchProduct() {
    console.log('搜索函数被调用');
    
    const searchTerm = document.getElementById('searchInput').value.trim();
    console.log('搜索词:', searchTerm);
    
    if (!searchTerm) {
        alert('请输入产品名称');
        return;
    }

    const searchSection = document.getElementById('searchSection');
    const resultSection = document.getElementById('resultSection');
    const successResult = document.getElementById('successResult');
    const errorResult = document.getElementById('errorResult');
    const successDesc = document.getElementById('successDesc');

    console.log('DOM元素检查:', searchSection, resultSection, successResult, errorResult, successDesc);

    // 显示加载中
    if (searchSection) searchSection.style.display = 'none';
    if (resultSection) resultSection.style.display = 'block';
    if (successResult) successResult.style.display = 'none';
    if (errorResult) errorResult.style.display = 'none';
    if (successDesc) successDesc.textContent = '搜索中...';

    // 立即搜索
    setTimeout(() => {
        const results = [];
        
        // 精确匹配
        if (greenFoodDatabase[searchTerm]) {
            results.push({
                product: searchTerm,
                standard: greenFoodDatabase[searchTerm].standard,
                name: greenFoodDatabase[searchTerm].name
            });
        }
        
        // 模糊匹配
        for (const [product, info] of Object.entries(greenFoodDatabase)) {
            if (product.includes(searchTerm) && !results.some(r => r.product === product)) {
                results.push({
                    product: product,
                    standard: info.standard,
                    name: info.name
                });
            }
        }

        console.log('搜索结果:', results);

        if (results.length > 0 && successResult && successDesc) {
            successResult.style.display = 'block';
            if (errorResult) errorResult.style.display = 'none';
            
            if (results.length === 1) {
                const result = results[0];
                successDesc.innerHTML = `
                    <div style="margin-bottom: 10px;">
                        <strong>找到产品：</strong>${result.product}
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>标准名称：</strong>${result.name}
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>标准号：</strong>${result.standard}
                    </div>
                `;
            } else {
                successDesc.innerHTML = `<div style="margin-bottom: 10px;"><strong>找到${results.length}个匹配产品：</strong></div>`;
                results.forEach((result, index) => {
                    successDesc.innerHTML += `
                        <div style="margin-bottom: 8px; padding-left: 10px; border-left: 3px solid #4CAF50;">
                            <strong>${index + 1}. ${极result.product}</strong><br>
                            <small>标准：${result.name} (${result.standard})</small>
                        </div>
                    `;
                });
            }
        } else if (errorResult) {
            if (successResult) successResult.style.display = 'none';
            errorResult.style.display = 'block';
            const errorDesc = errorResult.querySelector('.result-desc');
            if (errorDesc) {
                errorDesc.textContent = 
                    '此产品不在绿色食品产品适用标准目录（2023版）之内，如果为别名可重试其他名称或下载目录自行核对。';
            }
        }
    }, 100);
}

// 下载Excel文件
function downloadExcelFile() {
    console.log('下载函数被调用');
    
    try {
        const link = document.createElement('a');
        link.href = EXCEL_FILE_URL;
        link.download = '绿色食品产品适用标准目录(2023版).xlsx';
        
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        alert('正在下载绿色食品产品适用标准目录(2023版).xlsx');
        
    } catch (error) {
        console.error('下载出错:', error);
        alert('下载失败: ' + error.message);
    }
}

// 显示标准目录
function showStandardContent() {
    console.log('显示标准内容函数被调用');
    downloadExcelFile();
}

// 返回搜索
function backToSearch() {
    const searchSection = document.getElementById('searchSection');
    const resultSection = document.getElementById('resultSection');
    const searchInput = document.getElementById('searchInput');
    
    if (searchSection) searchSection.style.display = 'block';
    if (resultSection) resultSection.style.display = 'none';
    if (searchInput) searchInput.value = '';
}

console.log('模块一JavaScript已加载');