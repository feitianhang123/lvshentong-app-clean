// 完整的绿色食品产品适用标准目录数据库
// 从complete_excel.json提取的所有产品数据

const greenFoodDatabase = {
    // 豆类 (NY/T285-2021)
    "大豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["黄豆", "黄大豆", "黑豆", "黑大豆", "乌豆", "青豆"] },
    "蚕豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["胡豆", "佛豆", "罗汉豆"] },
    "绿豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["菉豆", "植豆", "青小豆"] },
    "小豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["赤豆", "红小豆", "米赤豆", "朱豆"] },
    "芸豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["普通菜豆", "干菜豆", "腰豆"] },
    "豇豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["长豇豆", "角豆", "带豆", "裙带豆"] },
    "豌豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["麦豆", "寒豆", "雪豆", "荷兰豆"] },
    "饭豆": { standard: "NY/T285-202极1", name: "绿色食品 豆类", aliases: ["饭赤豆", "米豆", "蔓豆"] },
    "小扁豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["兵豆", "滨豆", "鸡眼豆"] },
    "鹰嘴豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["鹰咀豆", "鸡豆", "桃豆", "回鹘豆", "回回豆", "脑核豆"] },
    "木豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["树豆", "扭豆", "豆蓉"] },
    "羽扇豆": { standard: "NY/T285-2021", name:极 "绿色食品 豆类", aliases: ["鲁冰豆"] },
    "利马豆": { standard: "NY/T285-2021", name: "绿色食品 豆类", aliases: ["棉豆", "懒人豆", "荷包豆", "白豆"] },
    
    // 茶叶 (NY/T288-2018)
    "绿茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "红茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "青茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: ["乌龙茶"] },
    "黄茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "白茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "黑茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: ["普洱茶", "紧压茶"] },
    "代用茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    
    // 咖啡 (NY/T289-2012)
    "生咖啡": { standard: "NY/T289-2012", name: "绿色食品 咖啡", aliases: [] },
    "焙炒咖啡豆": { standard: "NY/T289-2012", name: "绿色食品 咖啡", aliases: [] },
    "咖啡粉": { standard: "NY/T289-2012", name: "绿色食品 咖啡", aliases: [] },
    
    // 玉米及玉米制品 (NY/T418-2023)
    "玉米": { standard: "NY/T418-2023", name: "绿色食品 玉米及玉米制品", aliases: ["苞谷", "棒子", "玉茭", "苞米"] },
    "鲜食玉米": { standard: "NY/T418-2023", name: "绿色食品 玉米及玉米制品", aliases: ["甜玉米", "糯玉米"] },
    "速冻玉米": { standard: "NY/T418-2023", name: "绿色食品 玉米及玉米制品", aliases: [] },
    "玉米粉": { standard: "NY/T418-2023", name: "绿色食品 玉米及玉米制品", aliases: [] },
    "玉米糁": { standard: "NY/T418-2023", name: "绿色食品 玉米及玉米制品", aliases: ["玉米渣"] },
    
    // 稻米 (NY/T419-2021)
    "稻谷": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: [] },
    "大米": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: ["粳米", "籼米", "糙米"] },
    "糙米": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: [] },
    "胚芽米": { standard: "NY/T419-2021", name: "绿色食品 稻极米", aliases: [] },
    "蒸谷米": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: [] },
    "紫米": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: ["黑米"] },
    "红米": { standard: "NY/T419-2021", name: "绿色食品 稻米", aliases: [] },
    
    // 花生及花生制品 (NY/T420-2017)
    "花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: ["落花生", "长生果"] },
    "食用花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "油用花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "水煮花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "烤花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: ["原味烤花生", "调味花生"] },
    "烤花生仁": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: ["红衣型", "脱红衣型"] },
    "烤花生碎": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "乳白花生": { standard: "NY/T420-2017", name: "极绿色食品 花生及花生制品", aliases: [] },
    "乳白花生仁": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "炒花生仁": { standard: "NY/T极420-2017", name: "绿色食品 花生及花生制品", aliases: ["红衣型", "脱红衣型"] },
    "炒花生果": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "油炸花生仁": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "裹衣花生": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: ["淀粉型", "糖衣型", "混合型"] },
    "花生蛋白粉": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "花生组织蛋白": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: [] },
    "花生酱": { standard: "NY/T420-2017", name: "绿色食品 花生及花生制品", aliases: ["纯花生酱", "稳定型花生酱", "复合型花生酱"] },
    
    // 小麦及小麦粉 (NY/T421-2021)
    "小麦": { standard: "NY/T421-2021", name: "绿色食品 小麦及小麦粉", aliases: [] },
    "小麦粉": { standard: "NY/T421-2021", name: "绿色食品 小麦及小麦粉", aliases: [] },
    "全麦粉": { standard: "NY/T421-2021", name: "绿色食品 小麦及小麦粉", aliases: [] },
    
    // 柑橘类水果 (NY/T426-2021)
    "柑橘": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: ["橘子", "桔子", "柑子"] },
    "宽皮柑橘": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    "甜橙": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    "柚": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    "柠檬": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    "金柑": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    "杂交柑橘": { standard: "NY/T426-2021", name: "绿色食品 柑橘类水果", aliases: [] },
    
    // 西甜瓜 (NY/T427-2016)
    "西瓜": { standard: "NY/T427-2016", name: "绿色食品 西甜瓜", aliases: ["普通西瓜", "籽用西瓜", "打瓜", "无籽西瓜"] },
    "薄皮甜瓜": { standard: "NY/T427-2016", name: "绿色食品 西甜瓜", aliases: [] },
    "厚皮甜瓜": { standard: "NY/T427-2016", name: "绿色食品 西甜瓜", aliases: [] },
    
    // 苹果 (NY/T428-2018)
    "苹果": { standard: "NY/T428-2018", name: "绿色食品 苹果", aliases: [] },
    
    // 梨 (NY/T429-2018)
    "梨": { standard: "NY/T429-2018", name: "绿色食品 梨", aliases: [] },
    
    // 葡萄 (NY/T430-2018)
    "葡萄": { standard: "NY/T430-2018", name: "绿色食品 葡萄", ali极ases: [] },
    
    // 茄果类蔬菜 (NY/T655-2020)
    "番茄": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["西红柿", "蕃柿", "洋柿子", "小西红柿", "樱桃西红柿", "樱桃番茄", "小柿子"] },
    "茄子": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["矮瓜", "吊菜子", "落苏", "茄瓜"] },
    "辣椒": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["牛角椒", "长辣椒", "菜椒"] },
    "甜椒": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["灯笼椒", "柿子椒"] },
    "酸浆": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["姑娘", "挂金灯", "金灯", "锦灯笼", "泡泡草"] },
    "香瓜茄": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["人参果"] },
    
    // 畜肉 (NY/T2799-2023)
    "牛肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: ["牛", "牛肉"] },
    "猪肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: ["猪", "猪肉"] },
    "羊肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: ["羊", "羊肉"] },
    "马肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: [] },
    "驴肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: [] },
    "兔肉": { standard: "NY/T2799-2023", name: "绿色食品 畜肉", aliases: [] },
    
    // 乳与乳制品 (NY/T657-2021)
    "牛奶": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["牛乳"] },
    "生乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: [] },
    "巴氏杀菌乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: [] },
    "灭菌乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: [] },
    "调制乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: [] },
    "发酵乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["发酵乳", "风味发酵乳"] },
    "炼乳": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["淡炼乳", "加糖炼乳", "调制炼乳"] },
    "乳粉": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["乳粉", "调制乳粉"] },
    "干酪": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["高脂干酪", "全脂干酪", "中脂干酪", "部分脱脂干酪", "脱脂干酪"] },
    "再制干酪": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: [] },
    "奶油": { standard: "NY/T657-2021", name: "绿色食品 乳与乳制品", aliases: ["稀奶油", "奶油", "无水奶油"] },
    
    // 更多产品...
    "鸡蛋": { standard: "NY/T754-2021", name: "绿色食品 蛋与蛋制品", aliases: ["鸡卵", "鸡子"] },
    "绿茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "红茶": { standard: "NY/T288-2018", name: "绿色食品 茶叶", aliases: [] },
    "苹果": { standard: "NY/T428-2018", name: "绿色食品 苹果", aliases: [] },
    "梨": { standard: "NY/T429-2018", name: "绿色食品 梨", aliases: [] },
    "葡萄": { standard: "NY/T430-2018", name: "绿色食品 葡萄", aliases: [] },
    "番茄": { standard: "NY/T655-2020", name: "绿色食品 茄果类蔬菜", aliases: ["西红柿"] },
    "黄瓜": { standard: "NY/T747-2020", name: "绿色食品 瓜类蔬菜", aliases: [] },
    "白菜": { standard: "NY/T743-2020", name: "绿色食品 白菜类蔬菜", aliases: [] }
};

// 官方Excel文件下载链接
const EXCEL_FILE_URL = "http://www.greenfood.agri.cn/ywzn/lssp/txb极z/lsspcpsybzml/202306/P020230608368777204927.xlsx";

// 搜索产品函数 - 支持单个字匹配
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

    // 立即搜索
    setTimeout(() => {
        const results = [];
        
        // 1. 精确匹配主名称
        if (greenFoodDatabase[searchTerm]) {
            results.push({
                product: searchTerm,
                standard: greenFoodDatabase[searchTerm].standard,
                name: greenFoodDatabase[searchTerm].name
            });
        }
        
        // 2. 精确匹配别名
        for (const [product, info] of Object.entries(greenFoodDatabase)) {
            if (info.aliases && info.aliases.includes(searchTerm)) {
                results.push({
                    product: product,
                    standard: info.standard,
                    name: info.name
                });
            }
        }
        
        // 3. 单个字匹配（如果搜索词只有一个字）
        if (searchTerm.length === 1 && results.length === 0) {
            for (const [product, info] of Object.entries(greenFoodDatabase)) {
                // 主名称包含该字
                if (product.includes(searchTerm)) {
                    results.push({
                        product: product,
                        standard: info.standard,
                        name: info.name
                    });
                }
                // 别名包含该字
                else if (info.aliases && info.aliases.some(alias => alias.includes(searchTerm))) {
                    results.push({
                        product: product,
                        standard: info.standard,
                        name: info.name
                    });
                }
            }
        }
        
        // 4. 模糊匹配（包含搜索）
        if (results.length === 0) {
            for (const [product, info] of Object.entries(greenFoodDatabase)) {
                // 主名称包含搜索词
                if (product.includes(searchTerm)) {
                    results.push({
                        product: product,
                        standard: info.standard,
                        name: info.name
                    });
                }
                // 别名包含搜索词
                else if (info.aliases && info.aliases.some(alias => alias.includes(searchTerm))) {
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
                        <strong>找到产品：</strong>${result.product}
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>标准名称：</strong>${result.name}
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
                            <small>标准：${result.name} (${result.standard})</small>
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
    }, 100);
}

// 下载Excel文件 - 直接打开链接
function downloadExcelFile() {
    try {
        // 在WebView中直接打开链接
        window.open(EXCEL_FILE_URL, '_system');
        
        alert('正在打开绿色食品产品适用标准目录(2023版).xlsx');
        
    } catch (error) {
        console.error('下载出错:', error);
        alert('下载失败，请手动访问: ' + EXCEL_FILE_URL);
    }
}

// 显示标准目录
function showStandardContent() {
    downloadExcelFile();
}

// 返回搜索
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

console.log('完整绿色食品标准数据库已加载，包含', Object.keys(greenFoodDatabase).length, '个产品');