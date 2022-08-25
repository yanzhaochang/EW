'''
数据初始化
'''

import apis 
import pandas as pd


def init_database():
    init_location_data()

    init_ew_rank_data()
    init_ew_ttc_data()
    init_ew_cf_data()
    init_ew_frequency_data()
    
def init_ew_rank_data():
    rank_data = pd.read_csv('.\\data\\ew_rank.csv', header=0, encoding='GBK')
    
    apis.set_ew_rank_data('time_id', rank_data['time_id'].values)
    apis.set_ew_rank_data('level0_percent', rank_data['level0_percent'].values.tolist())
    apis.set_ew_rank_data('level1_percent', rank_data['level1_percent'].values.tolist())
    apis.set_ew_rank_data('level2_percent', rank_data['level2_percent'].values.tolist())

def init_ew_ttc_data():
    ttc_data = pd.read_csv('.\\data\\ew_ttc.csv', header=0, encoding='utf-8')
    
    apis.add_ttc_column('time_id', ttc_data['time_id'].values.tolist())
    apis.add_ttc_column('ttc_name', ttc_data['ttc_name'].values.tolist())
    apis.add_ttc_column('plan_power', ttc_data['plan_power'].values.tolist())
    apis.add_ttc_column('up_power', ttc_data['up_power'].values.tolist())
    apis.add_ttc_column('low_power', ttc_data['low_power'].values.tolist())

def init_ew_frequency_data():
    ew_freq_data = pd.read_csv('.\\data\\ew_frequency.csv', header=0, encoding='utf-8') 
    
    apis.add_ew_frequency_column('time_id', ew_freq_data['time_id'].values.tolist())
    apis.add_ew_frequency_column('event', ew_freq_data['event'].values.tolist())
    apis.add_ew_frequency_column('level0_percent', ew_freq_data['level0_percent'].values.tolist())
    apis.add_ew_frequency_column('level1_percent', ew_freq_data['level1_percent'].values.tolist())
    apis.add_ew_frequency_column('level2_percent', ew_freq_data['level2_percent'].values.tolist())

def init_ew_cf_data():
    cf_data = pd.read_csv('.\\data\\ew_cf.csv', header=0, encoding='utf-8')
    
    apis.add_ew_cf_column('time_id', cf_data['time_id'].values.tolist())
    apis.add_ew_cf_column('stage1_index', cf_data['stage1_index'].values.tolist())
    apis.add_ew_cf_column('stage1_line', cf_data['stage1_line'].values.tolist())
    apis.add_ew_cf_column('stage2_index', cf_data['stage2_index'].values.tolist())
    apis.add_ew_cf_column('stage2_line', cf_data['stage2_line'].values.tolist())
    apis.add_ew_cf_column('stage3_index', cf_data['stage3_index'].values.tolist())
    apis.add_ew_cf_column('stage3_line', cf_data['stage3_line'].values.tolist())
    apis.add_ew_cf_column('stage4_index', cf_data['stage4_index'].values.tolist())
    apis.add_ew_cf_column('stage4_line', cf_data['stage4_line'].values.tolist())

def init_location_data():
    location_data = pd.read_csv('.\\conf\\location.csv', header=0, encoding='GBK', engine='python')
    
    apis.add_location_data('bus_name', location_data['母线名'].values.tolist())
    apis.add_location_data('longitude', location_data['经度'].values.tolist())
    apis.add_location_data('latitude', location_data['纬度'].values.tolist())

    lines_data = pd.read_csv('.\\conf\\lines.csv', header=0, encoding='GBK', engine='python')
    apis.add_location_data('bus_send', lines_data['起始'].values.tolist())
    apis.add_location_data('bus_receive', lines_data['终止'].values.tolist())
    apis.add_location_data('line', lines_data['名称'].values.tolist())

     