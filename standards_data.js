const standardsData = [
  {
    "name": "绿色食品 啤酒",
    "code": "NYT273-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613556947348435.doc"
  },
  {
    "name": "绿色食品 葡萄酒",
    "code": "NYT274-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613556784751016.docx"
  },
  {
    "name": "绿色食品 豆类",
    "code": "NYT285-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613556619030978.doc"
  },
  {
    "name": "绿色食品 茶叶",
    "code": "NYT288-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613556432253002.doc"
  },
  {
    "name": "绿色食品 咖啡",
    "code": "NYT289-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617466464166934.doc"
  },
  {
    "name": "绿色食品 玉米及其制品",
    "code": "NYT418-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613556053310945.doc"
  },
  {
    "name": "绿色食品 稻米",
    "code": "NYT419-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613555843673345.doc"
  },
  {
    "name": "绿色食品 花生及制品",
    "code": "NYT420-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613555669431309.doc"
  },
  {
    "name": "绿色食品 小麦及小麦粉",
    "code": "NYT421-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613555498436836.doc"
  },
  {
    "name": "绿色食品 食用糖",
    "code": "NYT422-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613555257477646.doc"
  },
  {
    "name": "绿色食品 柑橘类水果",
    "code": "NYT426-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613555085955153.doc"
  },
  {
    "name": "绿色食品 西甜瓜",
    "code": "NYT427-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613554903539699.doc"
  },
  {
    "name": "绿色食品 果（蔬）酱",
    "code": "NYT431-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613554714279588.doc"
  },
  {
    "name": "绿色食品 白酒",
    "code": "NYT432-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613554535670387.doc"
  },
  {
    "name": "绿色食品 植物蛋白饮料",
    "code": "NYT433-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613554362198568.doc"
  },
  {
    "name": "绿色食品 果蔬汁及其饮料",
    "code": "NYT434-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617467045977389.docx"
  },
  {
    "name": "绿色食品 水果、蔬菜脆片",
    "code": "NYT435-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613553688065391.doc"
  },
  {
    "name": "绿色食品 蜜饯",
    "code": "NYT436-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613553484272316.doc"
  },
  {
    "name": "绿色食品 酱腌菜",
    "code": "NYT437-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613553304358696.doc"
  },
  {
    "name": "绿色食品 白菜类蔬菜",
    "code": "NYT654-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613553048766720.doc"
  },
  {
    "name": "绿色食品 茄果类蔬菜",
    "code": "NYT655-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613552846590884.doc"
  },
  {
    "name": "绿色食品 乳与乳制品",
    "code": "NYT657-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613552625038619.docx"
  },
  {
    "name": "绿色食品 绿叶类蔬菜",
    "code": "NYT743-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613552456885616.doc"
  },
  {
    "name": "绿色食品 葱蒜类蔬菜",
    "code": "NYT744-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613552257546486.doc"
  },
  {
    "name": "绿色食品 根菜类蔬菜",
    "code": "NYT745-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613552063944873.doc"
  },
  {
    "name": "绿色食品 甘蓝类蔬菜",
    "code": "NYT746-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613551854178941.doc"
  },
  {
    "name": "绿色食品 瓜类蔬菜",
    "code": "NYT747-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613551652008838.doc"
  },
  {
    "name": "绿色食品 豆类蔬菜",
    "code": "NYT748-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613551461028411.doc"
  },
  {
    "name": "绿色食品 食用菌",
    "code": "NYT749-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230714375746190376.doc"
  },
  {
    "name": "绿色食品 热带、亚热带水果",
    "code": "NYT750-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613550692813900.doc"
  },
  {
    "name": "绿色食品 食用植物油",
    "code": "NYT751-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613550488067132.doc"
  },
  {
    "name": "绿色食品 蜂产品",
    "code": "NYT752-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613550283761272.doc"
  },
  {
    "name": "绿色食品 禽肉",
    "code": "NYT753-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613550094181861.docx"
  },
  {
    "name": "绿色食品 蛋及蛋制品",
    "code": "NYT754-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613549845117975.doc"
  },
  {
    "name": "绿色食品 虾",
    "code": "NYT840-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613549644999128.doc"
  },
  {
    "name": "绿色食品 蟹",
    "code": "NYT841-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613549460526159.doc"
  },
  {
    "name": "绿色食品 鱼",
    "code": "NYT842-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613549216297734.docx"
  },
  {
    "name": "绿色食品 畜禽肉制品",
    "code": "NYT843-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613548779243589.doc"
  },
  {
    "name": "绿色食品 温带水果",
    "code": "NYT844-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613548538212657.doc"
  },
  {
    "name": "绿色食品 大麦及大麦粉",
    "code": "NYT891-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617477110211018.doc"
  },
  {
    "name": "绿色食品 燕麦及燕麦粉",
    "code": "NYT892-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617468565686721.docx"
  },
  {
    "name": "绿色食品 粟、黍、稷及其制品",
    "code": "NYT893-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613547379550150.doc"
  },
  {
    "name": "绿色食品 荞麦及荞麦粉",
    "code": "NYT894-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617468291165480.docx"
  },
  {
    "name": "绿色食品 高粱及高粱米",
    "code": "NYT895-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613546957009732.doc"
  },
  {
    "name": "绿色食品 黄酒",
    "code": "NYT897-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613546722965936.doc"
  },
  {
    "name": "绿色食品 含乳饮料",
    "code": "NYT898-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613546498536722.doc"
  },
  {
    "name": "绿色食品 冷冻饮品",
    "code": "NYT899-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613546289315213.doc"
  },
  {
    "name": "绿色食品 发酵调味品",
    "code": "NYT900-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613546028417590.doc"
  },
  {
    "name": "绿色食品 香辛料及其制品",
    "code": "NYT901-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613545805326672.docx"
  },
  {
    "name": "绿色食品 瓜籽",
    "code": "NYT902-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613545578622409.doc"
  },
  {
    "name": "绿色食品 淀粉及淀粉制品",
    "code": "NYT1039-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617466252073569.doc"
  },
  {
    "name": "绿色食品 食用盐",
    "code": "NYT1040-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613545119155588.doc"
  },
  {
    "name": "绿色食品 干果",
    "code": "NYT1041-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613544924849407.doc"
  },
  {
    "name": "绿色食品 坚果",
    "code": "NYT1042-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613544683846276.doc"
  },
  {
    "name": "绿色食品 人参和西洋参",
    "code": "NYT1043-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613544436015948.doc"
  },
  {
    "name": "绿色食品 藕及其制品",
    "code": "NYT1044-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613544220772954.doc"
  },
  {
    "name": "绿色食品 脱水蔬菜",
    "code": "NYT1045-2014",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613543884731743.doc"
  },
  {
    "name": "绿色食品 焙烤食品",
    "code": "NYT1046-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613543687611215.doc"
  },
  {
    "name": "绿色食品 水果蔬菜罐头",
    "code": "NYT1047-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613543475322695.doc"
  },
  {
    "name": "绿色食品 笋及笋制品",
    "code": "NYT1048-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613543262547200.doc"
  },
  {
    "name": "绿色食品 薯芋类蔬菜",
    "code": "NYT1049-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613543068133720.doc"
  },
  {
    "name": "绿色食品 龟鳖类",
    "code": "NYT1050-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613542818739981.doc"
  },
  {
    "name": "绿色食品 枸杞及枸杞制品",
    "code": "NYT1051-2014",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613542580785512.doc"
  },
  {
    "name": "绿色食品 豆制品",
    "code": "NYT1052-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617465527572766.doc"
  },
  {
    "name": "绿色食品 味精",
    "code": "NY-T1053-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613542165673413.doc"
  },
  {
    "name": "绿色食品 固体饮料",
    "code": "NYT1323-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613541838448675.doc"
  },
  {
    "name": "绿色食品 芥菜类蔬菜",
    "code": "NYT1324-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613541603255878.doc"
  },
  {
    "name": "绿色食品 芽苗类蔬菜",
    "code": "NYT1325-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613541283731438.doc"
  },
  {
    "name": "绿色食品 多年生蔬菜",
    "code": "NYT1326-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613541023522021.doc"
  },
  {
    "name": "绿色食品 鱼糜制品",
    "code": "NYT1327-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613540785060615.doc"
  },
  {
    "name": "绿色食品 鱼罐头",
    "code": "NYT1328-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613539635257373.doc"
  },
  {
    "name": "绿色食品 海水贝",
    "code": "NYT1329-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613533986379392.doc"
  },
  {
    "name": "绿色食品 方便主食品",
    "code": "NYT1330-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613522174722977.doc"
  },
  {
    "name": "绿色食品 水生蔬菜",
    "code": "NYT1405-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613521858739363.docx"
  },
  {
    "name": "绿色食品 速冻蔬菜",
    "code": "NYT1406-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613520947832771.doc"
  },
  {
    "name": "绿色食品 速冻预包装面米食品",
    "code": "NYT1407-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613520724610792.doc"
  },
  {
    "name": "绿色食品 食用花卉",
    "code": "NYT1506-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613519696628045.doc"
  },
  {
    "name": "绿色食品 山野菜",
    "code": "NYT1507-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613517088536359.doc"
  },
  {
    "name": "绿色食品 果酒",
    "code": "NYT1508-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613516599483466.doc"
  },
  {
    "name": "绿色食品 芝麻及其制品",
    "code": "NYT1509-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613515877869292.doc"
  },
  {
    "name": "绿色食品 麦片和麦芽",
    "code": "NYT1510-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617471195738040.doc"
  },
  {
    "name": "绿色食品 膨化食品",
    "code": "NYT1511-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613515132440701.doc"
  },
  {
    "name": "绿色食品 生面食米粉制品",
    "code": "NYT1512-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613514902864997.docx"
  },
  {
    "name": "绿色食品 畜禽可食用副产品",
    "code": "NYT1513-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613514597529139.doc"
  },
  {
    "name": "绿色食品 海参及制品",
    "code": "NYT1514-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613514338708784.doc"
  },
  {
    "name": "绿色食品 海蜇制品",
    "code": "NYT1515-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613514106868533.doc"
  },
  {
    "name": "绿色食品 蛙类及其制品",
    "code": "NYT1516-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613505277777865.doc"
  },
  {
    "name": "绿色食品 藻类及其制品",
    "code": "NYT1709-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613505000489336.doc"
  },
  {
    "name": "绿色食品 水产调味品",
    "code": "NYT1710-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613504728505824.doc"
  },
  {
    "name": "绿色食品 辣椒制品",
    "code": "NYT1711-2020",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613504423473595.doc"
  },
  {
    "name": "绿色食品 干制水产品",
    "code": "NYT1712-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613503686501074.doc"
  },
  {
    "name": "绿色食品 茶饮料",
    "code": "NYT1713-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613503336016375.doc"
  },
  {
    "name": "绿色食品 即食谷粉",
    "code": "NYT1714-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613503083628815.doc"
  },
  {
    "name": "绿色食品 果蔬粉",
    "code": "NYT1884-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613502568163707.doc"
  },
  {
    "name": "绿色食品 米酒",
    "code": "NYT1885-2017",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613502291421462.doc"
  },
  {
    "name": "绿色食品 复合调味料",
    "code": "NYT1886-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613501583106118.doc"
  },
  {
    "name": "绿色食品 乳清制品",
    "code": "NYT1887-2010",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613477494599912.doc"
  },
  {
    "name": "绿色食品 软体动物休闲食品",
    "code": "NYT1888-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613477272441901.doc"
  },
  {
    "name": "绿色食品 烘炒食品",
    "code": "NYT1889-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613477060671625.doc"
  },
  {
    "name": "绿色食品 蒸制类糕点",
    "code": "NYT1890-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613476170368514.doc"
  },
  {
    "name": "绿色食品 配制酒",
    "code": "NYT2104-2018",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613475919824067.doc"
  },
  {
    "name": "绿色食品 汤类罐头",
    "code": "NYT2105-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613475640334297.doc"
  },
  {
    "name": "绿色食品 谷物类罐头",
    "code": "NYT2106-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613475411583495.doc"
  },
  {
    "name": "绿色食品 食品馅料",
    "code": "NYT2107-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613475171311094.doc"
  },
  {
    "name": "绿色食品 熟粉及熟米制糕点",
    "code": "NYT2108-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613474928397631.doc"
  },
  {
    "name": "绿色食品 鱼类休闲食品",
    "code": "NYT2109-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613474663193992.doc"
  },
  {
    "name": "绿色食品 淀粉糖和糖浆",
    "code": "NYT2110-2011",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613474368287485.doc"
  },
  {
    "name": "绿色食品 调味油",
    "code": "NYT2111-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613466050519709.doc"
  },
  {
    "name": "绿色食品 代用茶",
    "code": "NYT2140-2015",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613465778327323.doc"
  },
  {
    "name": "绿色食品 畜肉",
    "code": "NYT2799-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613462551278338.doc"
  },
  {
    "name": "绿色食品 啤酒花及其制品",
    "code": "NYT2973-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613462174774943.doc"
  },
  {
    "name": "绿色食品 杂粮米及杂粮米碾磨加工品",
    "code": "NYT2974-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617470448108250.docx"
  },
  {
    "name": "绿色食品 头足类水产品",
    "code": "NYT2975-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613461616950356.doc"
  },
  {
    "name": "绿色食品 冷藏、速冻调制水产品",
    "code": "NYT2976-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617467347373213.doc"
  },
  {
    "name": "绿色食品 薏仁及薏仁粉",
    "code": "NYT2977-2025",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020250617469744995667.docx"
  },
  {
    "name": "绿色食品 天然矿泉水",
    "code": "NYT2979-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613457613885663.doc"
  },
  {
    "name": "绿色食品 包装饮用水",
    "code": "NYT2980-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613457371462859.doc"
  },
  {
    "name": "绿色食品 魔芋及其制品",
    "code": "NYT2981-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613456640808349.doc"
  },
  {
    "name": "绿色食品 油菜籽",
    "code": "NYT2982-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613456335326678.doc"
  },
  {
    "name": "绿色食品 速冻水果",
    "code": "NYT2983-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613456049844079.doc"
  },
  {
    "name": "绿色食品 淀粉类蔬菜粉",
    "code": "NYT2984-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613455827777988.doc"
  },
  {
    "name": "绿色食品 低聚糖",
    "code": "NYT2985-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613455598804543.doc"
  },
  {
    "name": "绿色食品 糖果",
    "code": "NYT2986-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613455325901182.doc"
  },
  {
    "name": "绿色食品 果醋饮料",
    "code": "NYT2987-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613455056712337.doc"
  },
  {
    "name": "绿色食品 湘式挤压糕点",
    "code": "NYT2988-2016",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613454781463974.doc"
  },
  {
    "name": "绿色食品 可食用鱼副产品及其制品",
    "code": "NYT3899-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613454516243187.doc"
  },
  {
    "name": "绿色食品 豆类罐头",
    "code": "NYT3900-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613454226079798.doc"
  },
  {
    "name": "绿色食品 谷物饮料",
    "code": "NYT3901-2021",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613421875316023.doc"
  },
  {
    "name": "绿色食品 冲调类方便食品",
    "code": "NYT4268-2023",
    "type": "product",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxcplbz/202306/P020230613421625720442.doc"
  },
  {
    "name": "绿色食品 肥料使用准则",
    "code": "NYT394-2023",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020231228386427915134.doc"
  },
  {
    "name": "绿色食品 渔药使用准则",
    "code": "NYT755-2022",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612538510462406.docx"
  },
  {
    "name": "绿色食品 兽药使用准则",
    "code": "NYT472-2022",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612538231090793.docx"
  },
  {
    "name": "绿色食品 储藏运输准则",
    "code": "NYT1056-2021",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/P020230612541901462901.doc"
  },
  {
    "name": "绿色食品 产地环境调查、监测与评价规范",
    "code": "NYT1054-2021",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612538722095970.doc"
  },
  {
    "name": "绿色食品 _产地环境质量",
    "code": "NYT391-2021",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612534346735046.doc"
  },
  {
    "name": "绿色食品 食品添加剂使用准则",
    "code": "NYT392-2023",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/U020230612534752330776.doc"
  },
  {
    "name": "绿色食品 海洋捕捞水产品生产管理规范",
    "code": "NYT1891-2010",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/U020230612542349135408.doc"
  },
  {
    "name": "绿色食品 农药使用准则",
    "code": "NYT393-2020",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612535799866162.doc"
  },
  {
    "name": "绿色食品 饲料及饲料添加剂使用准则",
    "code": "NYT471-2023",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202306/P020230612539715071251.doc"
  },
  {
    "name": "绿色食品 畜禽卫生防疫准则",
    "code": "NYT473-2016",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/P020230612542110641101.doc"
  },
  {
    "name": "绿色食品 产品检验规则",
    "code": "NYT1055-2015",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/P020230612541693645428.doc"
  },
  {
    "name": "绿色食品 包装通用准则",
    "code": "NYT658-2015",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/P020230612539937941964.doc"
  },
  {
    "name": "绿色食品 产品抽样准则",
    "code": "NYT896-2015",
    "type": "guideline",
    "url": "http://www.greenfood.agri.cn/ywzn/lssp/txbz/xxbz/xxzzlbz/202303/P020230612541055813109.doc"
  }
];

// 统计信息
const totalStandards = standardsData.length;
const productStandards = standardsData.filter(s => s.type === 'product').length;
const guidelineStandards = standardsData.filter(s => s.type === 'guideline').length;

console.log('标准数据加载完成');
console.log('总标准数:', totalStandards);
console.log('产品标准:', productStandards);
console.log('准则标准:', guidelineStandards);
