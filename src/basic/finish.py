'''
窗口关闭后保存文件
'''
import apis 
import pandas as pd 

def save_final_database():
    save_ew_rank_data() 
    save_ew_ttc_data()
    save_ew_cf_data()
    save_ew_frequency_data()
    
def save_ew_rank_data():
    time_id = apis.get_ew_rank_data('time_id')
    level0_percent = apis.get_ew_rank_data('level0_percent')
    level1_percent = apis.get_ew_rank_data('level1_percent')
    level2_percent = apis.get_ew_rank_data('level2_percent')
    data = pd.DataFrame({'time_id': time_id, 'level0_percent': level0_percent, 'level1_percent': level1_percent, 'level2_percent': level2_percent})
    data.to_csv('.\\data\\ew_rank.csv', sep=',', index=None)    

def save_ew_ttc_data():
    time_id = apis.get_ttc_column('time_id')
    ttc_name = apis.get_ttc_column('ttc_name')
    plan_power = apis.get_ttc_column('plan_power')
    up_power = apis.get_ttc_column('up_power')
    low_power = apis.get_ttc_column('low_power')

    data = pd.DataFrame({'time_id': time_id, 'ttc_name': ttc_name, 
        'plan_power': plan_power, 'up_power': up_power, 'low_power': low_power})
    data.to_csv('.\\data\\ew_ttc.csv', sep=',', index=None)

def save_ew_frequency_data():
    time_id = apis.get_ew_frequency_column('time_id')
    event = apis.get_ew_frequency_column('event')
    level0_percent = apis.get_ew_frequency_column('level0_percent')
    level1_percent = apis.get_ew_frequency_column('level1_percent')
    level2_percent = apis.get_ew_frequency_column('level2_percent')
    data = pd.DataFrame({'time_id': time_id, 'event': event, 'level0_percent': level0_percent, 'level1_percent': level1_percent, 'level2_percent': level2_percent})
    data.to_csv('.\\data\\ew_frequency.csv', sep=',', index=None)        


def save_ew_cf_data():
    time_id = apis.get_ew_cf_column('time_id')
    stage1_index = apis.get_ew_cf_column('stage1_index')
    stage1_line = apis.get_ew_cf_column('stage1_line')
    stage2_index = apis.get_ew_cf_column('stage2_index')
    stage2_line = apis.get_ew_cf_column('stage2_line')
    stage3_index = apis.get_ew_cf_column('stage3_index')
    stage3_line = apis.get_ew_cf_column('stage3_line')
    stage4_index = apis.get_ew_cf_column('stage4_index')
    stage4_line = apis.get_ew_cf_column('stage4_line')

    data = pd.DataFrame({"time_id": time_id, 'stage1_index': stage1_index, 'stage1_line': stage1_line, 
        'stage2_index': stage2_index, 'stage2_line': stage2_line,
        'stage3_index': stage3_index, 'stage3_line': stage3_line, 
        'stage4_index': stage4_index, 'stage4_line': stage4_line})
    data.to_csv('.\\data\\ew_cf.csv', index=None)    