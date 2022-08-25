
from database import EWFREQ 

def add_ew_frequency_column(column, value):
    EWFREQ[column] = value 

def get_ew_frequency_column(column):
    return EWFREQ[column]

def get_ew_frequency_data(time_id, par_name):
    index = [i for i in range(len(EWFREQ['time_id'])) if EWFREQ['time_id'][i] == time_id]
    value = [EWFREQ[par_name][i] for i in index]
    return value 