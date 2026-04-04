// 绿色食品产品适用标准目录搜索功能
console.log('模块一功能已加载');

function searchProduct() {
    const searchTerm = document.getElementById('searchInput').value.trim();
    if (!searchTerm) {
        alert('请输入产品名称');
        return;
    }
    alert('搜索: ' + searchTerm);
}

function showStandardContent() {
    alert('正在打开绿色食品产品适用标准目录（2023版）');
}

function backToSearch() {
    document.getElementById('searchSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
}

function handleEnter(event) {
    if (event.key === 'Enter') {
        searchProduct();
    }
}