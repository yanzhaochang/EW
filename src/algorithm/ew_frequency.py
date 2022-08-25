import random 
import apis 

def calculate_ew_frequency_data():
    time_id = []
    level0_percent = []
    level1_percent = []
    level2_percent = []
    hvdc = []
    events = ['鲁固', '扎青', '银东', '陇东']
    for i in range(24):
        for event in events:
            a = random.uniform(0.7, 0.8)
            b = random.uniform(0.1, 0.15)
            d = 1 - a - b 
            level0_percent.append(a)
            level1_percent.append(b)
            level2_percent.append(d)
            hvdc.append(event)
            time_id.append(i+1)
    apis.add_ew_frequency_column('level0_percent', level0_percent)
    apis.add_ew_frequency_column('level1_percent', level1_percent)
    apis.add_ew_frequency_column('level2_percent', level2_percent)
