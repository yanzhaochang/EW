'''
场景预警
算法与前端页面应该是同步进行的
如果把data文件夹视为数据库的话，那算法运行结束应将结果写入csv文件中
前端应每隔一个定时器时间去获取csv文件的数据
即database.py这个文件是不应存在的，为了方便我们设置了一个中间数据存储程序
'''

import apis 
import random 

def calculate_ew_rank_data():
    level0_percent = []
    level1_percent = []
    level2_percent = []
    for i in range(24):
        a = random.uniform(0.7, 0.8)
        b = random.uniform(0.1, 0.15)
        d = 1 - a - b 
        level0_percent.append(a)
        level1_percent.append(b)
        level2_percent.append(d)       
    apis.set_ew_rank_data('level0_percent', level0_percent)
    apis.set_ew_rank_data('level1_percent', level1_percent)
    apis.set_ew_rank_data('level2_percent', level2_percent)        

