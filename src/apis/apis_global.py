from database import GLOBALVARS, JSCODE

from database import LOCATION


def add_location_data(column, value):
    LOCATION[column] = value 

def get_line_bus(line):
    line_index = LOCATION['line'].index(line)
    bus_send = LOCATION['bus_send'][line_index]
    bus_receive = LOCATION['bus_receive'][line_index]    
    return bus_send, bus_receive

def get_bus_location(bus_name):
    index = LOCATION['bus_name'].index(bus_name)
    location = [LOCATION['longitude'][index], LOCATION['latitude'][index]]
    return location 

def get_line_location(line):
    bus_send, bus_receive = get_line_bus(line)  
    location_send = get_bus_location(bus_send) 
    location_receive = get_bus_location(bus_receive)
    return [location_send, location_receive]

def get_global_data(par_name):
    return GLOBALVARS[par_name]

def set_global_data(par_name, value):
    GLOBALVARS[par_name] = value 

def get_js_code(par_name):
    return JSCODE[par_name] 


