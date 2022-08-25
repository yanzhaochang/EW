from database import EWTTC


def add_ttc_column(column, value):
    EWTTC[column] = value 

def get_ttc_column(column):
    return EWTTC[column]

def set_ew_ttc_data(time_id, ttc_name, par_name, par_value):
    ttc_time_id = EWTTC['time_id']
    ttc_ttc_name = EWTTC['ttc_name'] 
    for i in range(len(ttc_time_id)):
        if ttc_time_id[i] == time_id and ttc_ttc_name[i] == ttc_name:
            break 
    EWTTC[par_name][i] = par_value

def get_ew_ttc_data(time_id, ttc_name, par_name):
    ttc_time_id = EWTTC['time_id']
    ttc_ttc_name = EWTTC['ttc_name'] 
    for i in range(len(ttc_time_id)):
        if ttc_time_id[i] == time_id and ttc_ttc_name[i] == ttc_name:
            break 
    return EWTTC[par_name][i] 