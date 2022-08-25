import apis 
import random


def calculate_ew_ttc_data():
    for i in range(24):
        plan_power = random.uniform(12, 16)
        up_power = random.uniform(18.5, 19.8)
        low_power = random.uniform(17, 18)
        apis.set_ew_ttc_data(i+1, '河北山东断面', 'plan_power', plan_power) 
        apis.set_ew_ttc_data(i+1, '河北山东断面', 'up_power', up_power) 
        apis.set_ew_ttc_data(i+1, '河北山东断面', 'low_power', low_power) 

    for i in range(24):
        plan_power = random.uniform(12, 16)
        up_power = random.uniform(18.5, 19.8)
        low_power = random.uniform(17, 18)
        apis.set_ew_ttc_data(i+1, '山东半岛断面', 'plan_power', plan_power) 
        apis.set_ew_ttc_data(i+1, '山东半岛断面', 'up_power', up_power) 
        apis.set_ew_ttc_data(i+1, '山东半岛断面', 'low_power', low_power) 