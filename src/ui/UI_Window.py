import sys
sys.path.append('.\\src')
import apis 
import algorithm 
import basic

from PyQt5 import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('电网安全预警前端页面') 
        self.setWindowIcon(QIcon("./img/sdu.png"))

        self.resize(1921, 1084)  
        #self.setWindowFlags(Qt.CustomizeWindowHint)  # 去掉标题栏的代码
        
        basic.init_database()
        
        self.label = QLabel('断面时刻')
        self.label.move(0, 100)
        self.init_global_layout()
        self.setBackground()

        self.timer = QTimer()
        self.timer.timeout.connect(self.analog_realtime_data)
        self.timer.start(5000)
    
    def setBackground(self):
        palette = QPalette()
        pix = QPixmap("./img/background.png")
        pix = pix.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)#自适应图片大小
        palette.setBrush(self.backgroundRole(), QBrush(pix))# 设置背景图片
        self.setPalette(palette)

    def init_global_layout(self):
        self.ew_rank = QWebEngineView()
        url = 'file:///D:/code/ew/conf/ew_rank.html'
        self.ew_rank.load(QUrl(url))      
        self.ew_rank.loadFinished.connect(self.display_ew_rank_data)
        self.ew_rank.page().setBackgroundColor(Qt.transparent)
        self.ew_rank.setFixedHeight(220)

        self.ew_grid = QWebEngineView()
        url = 'file:///D:/code/ew/conf/ew_grid.html'
        self.ew_grid.load(QUrl(url)) 
        self.ew_grid.loadFinished.connect(self.display_grid_data)
        self.ew_grid.page().setBackgroundColor(Qt.transparent)
        self.ew_grid.setFixedWidth(900)

        self.lower_widget = QWidget()
        self.lower_left_widget = QWidget()
        self.lower_right_widget = QWidget()

        self.lower_widget_layout = QHBoxLayout() 
        self.lower_widget_layout.addWidget(self.lower_left_widget)
        self.lower_widget_layout.addWidget(self.ew_grid)
        self.lower_widget_layout.addWidget(self.lower_right_widget)
        self.lower_widget_layout.setSpacing(0)
        self.lower_widget.setLayout(self.lower_widget_layout)

        self.ew_ttc = QWebEngineView()
        url = 'file:///D:/code/ew/conf/ew_ttc.html'
        self.ew_ttc.load(QUrl(url)) 
        self.ew_ttc.page().setBackgroundColor(Qt.transparent)
        self.ew_ttc.loadFinished.connect(self.display_ew_ttc_data)
        self.ew_ttc.setFixedWidth(360)
    
        self.ew_frequency = QWebEngineView()
        url = 'file:///D:/code/ew/conf/ew_frequency.html'
        self.ew_frequency.load(QUrl(url)) 
        self.ew_frequency.page().setBackgroundColor(Qt.transparent)
        self.ew_frequency.setFixedWidth(360)
        self.ew_frequency.loadFinished.connect(self.display_ew_frequency_initial_data)

        self.lower_left_layout = QVBoxLayout()
        self.lower_left_layout.addWidget(self.ew_ttc)
        self.lower_left_layout.addWidget(self.ew_frequency)
        self.lower_left_layout.setSpacing(0)
        self.lower_left_widget.setLayout(self.lower_left_layout)
        
        self.ew_cf = QWebEngineView()
        url = 'file:///D:/code/ew/conf/ew_cf.html'
        self.ew_cf.load(QUrl(url)) 
        self.ew_cf.page().setBackgroundColor(Qt.transparent)
        self.ew_cf.loadFinished.connect(self.display_ew_cf_data)

        self.lower_right_layout = QVBoxLayout()
        self.lower_right_layout.addWidget(self.ew_cf)
        self.lower_right_layout.setSpacing(0)
        self.lower_right_widget.setLayout(self.lower_right_layout)

        self.windowlayout = QVBoxLayout()
        self.windowlayout.addWidget(self.ew_rank)
        self.windowlayout.addWidget(self.lower_widget)
        self.windowlayout.setSpacing(0)
        self.setLayout(self.windowlayout)                           
        
    def display_ew_rank_data(self):   
        js_code = apis.get_js_code('ew_rank')
        self.ew_rank.page().runJavaScript(js_code)         
        self.update_ew_rank_data() 
    
    def display_ew_ttc_data(self):
        js_code = apis.get_js_code('ew_ttc')
        self.ew_ttc.page().runJavaScript(js_code)  
        time_id = apis.get_global_data('time_id')
        ttc_name = apis.get_global_data('ttc_name')
        self.update_ew_ttc_data(time_id, ttc_name)  
    
    def display_ew_frequency_initial_data(self):
        time_id = apis.get_global_data('time_id')
        self.update_ew_frequency_data(time_id)

    def display_ew_cf_data(self):
        time_id = apis.get_global_data('time_id')
        stage1_line = apis.get_ew_cf_stage1_line(time_id, 1)
        self.update_ew_cf_data(time_id, stage1_line)
  
    def update_ew_rank_data(self):
        level0_percent = apis.get_ew_rank_data('level0_percent')
        level1_percent = apis.get_ew_rank_data('level1_percent')
        level2_percent = apis.get_ew_rank_data('level2_percent')
        data = [level0_percent, level1_percent, level2_percent]
        self.ew_rank.page().runJavaScript('update_ew_rank_data({});'.format(data))

    def update_ew_ttc_data(self, time_id, ttc_name):
        apis.set_global_data('ttc_name', ttc_name)

        plan_power = apis.get_ew_ttc_data(time_id, ttc_name, 'plan_power')
        up_power = apis.get_ew_ttc_data(time_id, ttc_name, 'up_power')
        low_power = apis.get_ew_ttc_data(time_id, ttc_name, 'low_power')
        percent_1 = up_power / 20
        percent_2 = low_power / 20
        data = {'data': [{'name': '计划功率/GW', 'value': round(plan_power, 4)}], 
            'color': [[percent_1, 'green'], [percent_2, "rgb(247, 237, 32)"], [1, "rgb(214, 37, 39)"]],
            'subtext': ttc_name} 
        
        self.ew_ttc.page().runJavaScript('update_ew_ttc_data({});'.format(data))

    def update_ew_cf_data(self, time_id, stage1_line):
        data = apis.combine_cf_data(time_id, stage1_line)      
        self.ew_cf.page().runJavaScript('update_ew_cf_data({});'.format(data)) 
    
    def update_ew_frequency_data(self, time_id):
        level0_percent = apis.get_ew_frequency_data(time_id, 'level0_percent')
        level1_percent = apis.get_ew_frequency_data(time_id, 'level1_percent')
        level2_percent = apis.get_ew_frequency_data(time_id, 'level2_percent')
        data = [level0_percent, level1_percent, level2_percent]
        self.ew_frequency.page().runJavaScript('update_ew_frequency_data({});'.format(data))
    
    def display_grid_data(self):
        js_code = apis.get_js_code('ew_grid')
        self.ew_grid.page().runJavaScript(js_code)   
        self.update_grid_line_display()

    def update_grid_line_display(self):
        self.ew_grid.page().runJavaScript('clear_line();')
        self.ew_grid.page().runJavaScript('clear_node();')

        time_id = apis.get_global_data('time_id')
        cf_stage1_line_num = apis.get_global_data('cf_stage1_line_num')
        for i in range(cf_stage1_line_num):
            line = apis.get_ew_cf_stage1_line(time_id, i+1)
            location = apis.get_line_location(line)
            newLine = {"name": line, "coords": location}      
            self.ew_grid.page().runJavaScript('add_line({});'.format(newLine))
            
            bus_send, bus_receive = apis.get_line_bus(line)
            location1 = apis.get_bus_location(bus_send)
            location2 = apis.get_bus_location(bus_receive)
            node1 = {'name': bus_send, 'value': location1 + [0]}
            node2 = {'name': bus_receive, 'value': location2 + [0]}
            self.ew_grid.page().runJavaScript('add_node({});'.format(node1))
            self.ew_grid.page().runJavaScript('add_node({});'.format(node2))

    def analog_realtime_data(self):
        '''模拟实时数据 实际的计算程序可以分离'''
        algorithm.calculate_ew_rank_data()
        algorithm.calculate_ew_ttc_data()
        algorithm.calculate_ew_cf_data()
        algorithm.calculate_ew_frequency_data()

        self.update_ew_rank_data()
        time_id = apis.get_global_data('time_id')
        ttc_name = apis.get_global_data('ttc_name')
        self.update_ew_ttc_data(time_id, ttc_name)
        stage1_line = apis.get_ew_cf_stage1_line(time_id, 1)
        self.update_ew_cf_data(time_id, stage1_line)
        self.update_ew_frequency_data(time_id)
        self.update_grid_line_display()

    def update_display(self, strs):
        data = eval(strs)
        if data['seriesType'] == 'lines' and data['seriesName'] == '断面':
            time_id = apis.get_global_data('time_id')
            self.update_ew_ttc_data(time_id, data['name'])
        elif data['seriesType'] == 'lines' and data['seriesName'] == '线路': 
            time_id = apis.get_global_data('time_id')  
            self.update_ew_cf_data(time_id, data['name'])   
        else:
            pass      
    
    def update_homepage_display(self, strs):
        time_id = int(strs)
        apis.set_global_data('time_id', time_id)

        ttc_name = apis.get_global_data('ttc_name')
        self.update_ew_ttc_data(time_id, ttc_name)
        
        self.update_grid_line_display()

        stage1_line = apis.get_ew_cf_stage1_line(time_id, 1)
        self.update_ew_cf_data(time_id, stage1_line)
        
        self.update_ew_frequency_data(time_id)

    def closeEvent(self, event):
        basic.save_final_database()
            






        