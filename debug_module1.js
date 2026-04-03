// 调试模块一功能
console.log('开始调试模块一功能...');

// 检查数据文件是否存在
fetch('complete_excel.json')
    .then(response => {
        console.log('HTTP状态:', response.status, response.statusText);
        if (!response.ok) {
            throw new Error(`HTTP错误: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('数据加载成功:', data.length, '行');
        
        // 测试搜索功能
        const testSearch = "水稻";
        const found = data.filter(row => 
            (row.col1 && row.col1.includes(testSearch)) ||
            (row.col2 && row.col2.includes(testSearch)) ||
            (row.col3 && row.col3.includes(testSearch)) ||
            (row.col4 && row.col4.includes(testSearch))
        );
        console.log(`搜索"${testSearch}"结果:`, found.length, '个匹配');
        
        if (found.length > 0) {
            console.log('第一个匹配:', found[0]);
        }
    })
    .catch(error => {
        console.error('数据加载失败:', error.message);
    });