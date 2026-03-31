// 测试脚本 - 验证产品搜索功能
console.log('=== 产品搜索功能测试 ===');

// 加载产品数据
fetch('full_products_data.json')
    .then(response => response.json())
    .then(products => {
        console.log('总产品数量:', products.length);
        
        // 测试搜索功能
        const testSearches = ['肉', '蛋', '菠萝', '酒', '芒果', '葡萄'];
        
        testSearches.forEach(term => {
            const found = products.filter(p => 
                p.name.includes(term) || term.includes(p.name)
            );
            console.log(`搜索"${term}": 找到${found.length}个产品`);
            
            if (found.length > 0) {
                found.slice(0, 3).forEach(p => {
                    console.log(`  - ${p.name} (${p.standard})`);
                });
                if (found.length > 3) {
                    console.log(`  - ... 还有${found.length-3}个`);
                }
            }
        });
    })
    .catch(error => {
        console.error('加载数据失败:', error);
    });
