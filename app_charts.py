'''
生成charts图表
'''

import sys 
sys.path.append('.\\src')
import charts
import webbrowser
from pyecharts.charts import Geo, Pie, Gauge, Page



#bg_image = charts.generate_ew_background()

# 生成场景预警图
bar = charts.generate_ew_rank_bar()
bar.render(".\\conf\\ew_rank.html")  

#webbrowser.open('.\\conf\\ew_rank.html')
def insert_html(file):
    report = open(file, encoding='utf-8')
    line = []
    for i in report.readlines():
        line.append(i)
    report.close()
   
    line.insert(8, '    <script language="javascript" src="D:/code/ew/conf/qwebchannel.js"></script>')
    s = ''.join(line)
    reportnew = open(file, 'w', encoding='utf-8')
    reportnew.write(s)
    reportnew.close()    


# 生成地图
geo = charts.generate_ew_grid()
geo.render(".\\conf\\ew_grid.html")
#webbrowser.open('.\\conf\\ew_grid.html')
insert_html('.\\conf\\ew_grid.html')
insert_html('.\\conf\\ew_rank.html')

bar = charts.generate_ew_frequency_bar()
bar.render(".\\conf\\ew_frequency.html")  


gauge = charts.generate_ew_ttc_gauge()
gauge.render(".\\conf\\ew_ttc.html") 

tree = charts.generate_ew_cf_tree() 
tree.render(".\\conf\\ew_cf.html") 
#webbrowser.open('.\\conf\\ew_cf.html')


"""
page = Page(layout=Page.DraggablePageLayout)
page.add(bg_image, bar)
page.render(".\\conf\\init_ew.html")
webbrowser.open('.\\conf\\init_ew.html')
"""