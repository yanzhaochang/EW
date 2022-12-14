# 程序简介
在集团培训期间实在无聊，用PyQt加上JavaScript实现了国重项目中的前瞻预警软件的前端页面

# 所需第三方包
PyQt5，pyecharts，pandas

# 程序运行
命令行：python app_main.py

# 程序问题
存在绝对路径，环境变化需要修改

# 程序运行效果
<img width="955" alt="截图20220825164410" src="https://user-images.githubusercontent.com/60685547/186637725-32db36d0-c703-46b7-8f4b-f3bab2bde0f1.png">

# 页面操作
1) 最上方的柱子对应电网未来的安全状况，点击柱子，下方页面会根据未来的时刻来刷新
2) 中间为电网的页面，点击断面左侧的断面预警会刷新，点击线路则右侧的连锁故障链会刷新
3) 整个页面每5s访问一次数据库，刷新页面
4) 柱子红色部分越多，代表电网安全状况越差

# 程序框架
1) pyecharts生成初始的html图表
2) PyQt的QWebEngineView加载显示图表
3) runJavaScript方法将数据传入JS，刷新页面
4) QWebChannel将JS的返回值传给python
