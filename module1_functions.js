// 绿色食品产品适用标准目录搜索功能

// 产品数据库（从Excel文件转换而来）
const productDatabase = {
    "大豆": { row: 3, aliases: "黄豆、黄大豆、黑豆、黑大豆、乌豆、青豆等" },
    "蚕豆": { row: 4, aliases: "胡豆、佛豆、罗汉豆" },
    "绿豆": { row: 5, aliases: "菉豆、植豆、青小豆" },
    "小豆": { row: 6, aliases: "赤豆、红小豆、米赤豆、朱豆" },
    "芸豆": { row: 7, aliases: "普通菜豆、干菜豆、腰豆" },
    "豇豆": { row: 8, aliases: "长豇豆、角豆、带豆、裙带豆" },
    "豌豆": { row: 9, aliases: "麦豆、寒豆、雪豆、荷兰豆" },
    "饭豆": { row: 10, aliases: "饭赤豆、米豆、蔓豆" },
    "小扁豆": { row: 11, aliases: "兵豆、滨豆、鸡眼豆" },
    "鹰嘴豆": { row: 12, aliases: "鹰咀豆、鸡豆、桃豆、回鹘豆、回回豆、脑核豆" },
    "木豆": { row: 13, aliases: "树豆、扭豆、豆蓉" },
    "羽扇豆": { row: 14, aliases: "鲁冰豆" },
    "利马豆": { row: 15, aliases: "棉豆、懒人豆、荷包豆、白豆" },
    "绿茶": { row: 16, aliases: "" },
    "红茶": { row: 17, aliases: "" },
    "青茶": { row: 18, aliases: "乌龙茶" },
    "黄茶": { row: 19, aliases: "" },
    "白茶": { row: 20, aliases: "" },
    "黑茶": { row: 21, aliases: "普洱茶、紧压茶" },
    "代用茶": { row: 22, aliases: "" },
    "生咖啡": { row: 23, aliases: "" },
    "焙炒咖啡豆": { row: 24, aliases: "" },
    "咖啡粉": { row: 25, aliases: "" },
    "玉米": { row: 26, aliases: "苞谷、棒子、玉茭、苞米" },
    "鲜食玉米": { row: 27, aliases: "甜玉米、糯玉米" },
    "速冻玉米": { row: 28, aliases: "" },
    "玉米粉": { row: 29, aliases: "" },
    "玉米糁": { row: 30, aliases: "玉米渣" },
    "稻谷": { row: 31, aliases: "" },
    "大米": { row: 32, aliases: "粳米、籼米、糙米" },
    "糙米": { row: 33, aliases: "" },
    "胚芽米": { row: 34, aliases: "" },
    "蒸谷米": { row: 35, aliases: "" },
    "紫米": { row: 36, aliases: "黑米" },
    "红米": { row: 37, aliases: "" },
    "花生": { row: 38, aliases: "落花生、长生果" },
    "食用花生": { row: 39, aliases: "" },
    "油用花生": { row: 40, aliases: "" },
    "水煮花生": { row: 41, aliases: "" },
    "烤花生": { row: 42, aliases: "原味烤花生、调味花生" },
    "烤花生仁": { row: 43, aliases: "红衣型、脱红衣型" },
    "烤花生碎": { row: 44, aliases: "" },
    "乳白花生": { row: 45, aliases: "" },
    "乳白花生仁": { row: 46, aliases: "" },
    "炒花生仁": { row: 47, aliases: "红衣型、脱红衣型" },
    "炒花生果": { row: 48, aliases: "" },
    "油炸花生仁": { row: 49, aliases: "" },
    "裹衣花生": { row: 50, aliases: "淀粉型、糖衣型、混合型" },
    "花生蛋白粉": { row: 51, aliases: "" },
    "花生组织蛋白": { row: 52, aliases: "" },
    "花生酱": { row: 53, aliases: "纯花生酱、稳定型花生酱、复合型花生酱" },
    "小麦": { row: 54, aliases: "" },
    "小麦粉": { row: 55, aliases: "" },
    "全麦粉": { row: 56, aliases: "" },
    "柑橘": { row: 57, aliases: "橘子、桔子、柑子" },
    "宽皮柑橘": { row: 58, aliases: "" },
    "甜橙": { row: 59, aliases: "" },
    "柚": { row: 60, aliases: "" },
    "柠檬": { row: 61, aliases: "" },
    "金柑": { row: 62, aliases: "" },
    "杂交柑橘": { row: 63, aliases: "" },
    "西瓜": { row: 64, aliases: "普通西瓜、籽用西瓜、打瓜、无籽西瓜" },
    "薄皮甜瓜": { row: 65, aliases: "" },
    "厚皮甜瓜": { row: 66, aliases: "" },
    "苹果": { row: 67, aliases: "" },
    "梨": { row: 68, aliases: "" },
    "葡萄": { row: 69, aliases: "" },
    "番茄": { row: 70, aliases: "西红柿、蕃柿、洋柿子、小西红柿、樱桃西红柿、樱桃番茄、小柿子" },
    "茄子": { row: 71, aliases: "矮瓜、吊菜子、落苏、茄瓜" },
    "辣椒": { row: 72, aliases: "牛角椒、长辣椒、菜椒" },
    "甜椒": {极 row: 73, aliases: "灯笼椒、柿子椒" },
    "酸浆": { row: 74, aliases: "姑娘、挂金灯、金灯、锦灯笼、泡泡草" },
    "香瓜茄": { row: 75, aliases: "人参果" },
    "牛肉": { row: 76, aliases: "牛、牛肉" },
    "猪肉": { row: 77, aliases: "猪、猪肉" },
    "羊肉": { row: 78, aliases: "羊、羊肉" },
    "马肉": { row: 79, aliases: "" },
极 "驴肉": { row: 80, aliases: "" },
    "兔肉": { row: 81, aliases: "" },
    "牛奶": { row: 82, aliases: "牛乳" },
    "生乳": { row: 83, aliases: "" },
    "巴氏杀菌乳": { row: 84, aliases: "" },
    "灭菌乳": { row: 85, aliases: "" },
    "调制乳": { row: 86, aliases: "" },
    "发酵乳": { row: 87, aliases: "发酵乳、风味发酵乳" },
    "炼乳": { row: 88, aliases: "淡炼乳、加糖炼乳、调制炼乳" },
    "乳粉": { row: 89, aliases: "乳粉、调制极乳粉" },
    "干酪": { row: 90, aliases: "高脂干酪、全脂干酪、中脂干酪、部分脱脂干酪、脱脂干酪" },
    "再制干酪": { row: 91, aliases: "" },
    "奶油": { row: 92, aliases: "稀奶油、奶油、无水奶油" },
    "鸡蛋": { row: 93, aliases: "鸡卵、鸡子" }
};

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

    // 立即搜索
    setTimeout(() => {
        loading.style.display = 'none';
        
        // 精确匹配主名称
        if (productDatabase[searchTerm]) {
            const productInfo = productDatabase[searchTerm];
            successResult.style.display = 'block';
            errorResult.style.display = 'none';
            successDesc.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <strong>产品名称：</strong>${searchTerm}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>所在行数：</strong>第${productInfo.row}行
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>产品别名：</strong>${productInfo.aliases || '无'}
                </div>
                <div style="color: #666; font-size: 12px;">
                    详细信息请查阅完整的标准目录文件
                </div>
            `;
        } else {
            // 检查别名
            let foundInAliases = false;
            for (const [product, info] of Object.entries(productDatabase)) {
                if (info.aliases && info.aliases.includes(searchTerm)) {
                    successResult.style.display = 'block';
                    errorResult.style.display = 'none';
                    successDesc.innerHTML = `
                        <div style="margin-bottom: 10px;">
                            <strong>搜索别名：</strong>${searchTerm}
                        </div>
                        <div style="margin-bottom: 10px;">
                            <strong>对应产品：</strong>${product}
                        </div>
                        <div style="margin-bottom: 10px;">
                            <strong>所在行数：</strong>第${info.row}行
                        </div>
                        <div style="margin-bottom: 10px;">
                            <strong>产品别名：</strong>${info.aliases}
                        </div>
                        <div style="color: #666; font-size: 12px;">
                            详细信息请查阅完整的标准目录文件
                        </div>
                    `;
                    foundInAliases = true;
                    break;
                }
            }
            
            if (!foundInAliases) {
                successResult.style.display = 'none';
                errorResult.style.display = 'block';
                errorDesc.textContent = '申报产品不在绿色食品使用标准目录内，暂时无法申报绿色食品。';
            }
        }
    }, 100);
}

// 显示标准目录内容
function showStandardContent() {
    // 创建下载链接
    const link = document.createElement('a');
    link.href = '绿色食品产品适用标准目录（2023版）.xlsx';
    link.download = '绿色食品产品适用标准目录（2023版）.xlsx';
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    alert('正在下载绿色食品产品适用标准目录（2023版）.xlsx');
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

console.log('模块一功能已加载，包含', Object.keys(productDatabase).length, '个产品');