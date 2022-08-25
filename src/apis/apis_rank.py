'''
场景预警的数据操作
最外层存储历史数据，程序运行后初始化将数据读入内存
未来可以利用数据库存储技术进行升级
'''
from database import EWRANK

"""
def is_column_exist(column):
    keys = list(EWRANK.keys())
    if column not in keys:
        print('column 参数错误')
        return False
    else:
        return True
"""
def get_ew_rank_data(column):
    return EWRANK[column]

def set_ew_rank_data(column, data):
    EWRANK[column] = data    
    return  
