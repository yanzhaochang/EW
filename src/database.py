import pandas as pd 

GLOBALVARS = {'time_id': 1, 'time': '15:00', 'ttc_name': '河北山东断面', 'cf_stage1_line_num': 5}

LOCATION = {'bus_name': [], 'longitude': [], 'latitude': [], 'bus_send': [], 'bus_receive': [], 'line': []}

EWRANK = {'time_id': [], 'level0_percent': [], 'level1_percent': [], 'level2_percent': []}

EWTTC = {'time_id': [], 'ttc_name': [], 'plan_power': [], 'up_power': [], 'low_power': []}

EWFREQ = {'time_id': [], 'event': [], 'level0_percent': [], 'level1_percent': [], 'level2_percent': []}

EWCF = {'time_id': [], 'stage1_line': [], 'stage2_line': [], 'stage3_line': [],
    'stage4_line': [], 'cf_result': []}

JSCODE = {'ew_rank':  '''
            function myFunction(){   
                let options = chart_ew_rank.getOption();
                var dic = {x:40, y:70, x2:40, y2:20}; 
                options.grid = dic; 
                chart_ew_rank.setOption(options);    
            }
            myFunction();   
        ''',
        'ew_grid': '''
            function myFunction(){   
                let options = chart_ew_grid.getOption();
                var index = options.series.findIndex(element => element.name == "线路");   
                let linesOption = options.series[index].data;  
                var item = linesOption.pop();
                
                var index = options.series.findIndex(element => element.name == "断面");
                let ttcOption = options.series[index].data;
                ttcOption[0].name = "河北山东断面";
                ttcOption[1].name = "山东半岛断面";
                chart_ew_grid.setOption(options);    
            }
            myFunction();   
        ''',
        'ew_ttc': '''
            function myFunction(){   
                let options = chart_ew_ttc.getOption();
                var dic = {x:0, y:0, x2:0, y2:0}; 
                options.grid = dic; 
                chart_ew_ttc.setOption(options);    
            }
            myFunction();   
        '''
        }







CurrentSystem = {'plant_power': 20000, 'hvdc_power': 10000, 'new_energy_power': 5000, 'load_power': 50000}


BusConf = {'buses':[], 'names': [], 'longitude':[], 'latitude': []}

grid_model = {'raw_file': '', 'dyr_file': ''}


plants = []
plants_index = []

substations = []
substations_index = []

convert_stations = []
convert_stations_index = []

class PLANT(): # 火电厂
    # 火电厂应为一个多个发电机和一台双绕组或三绕组变压器组成
    def __init__(self):
        self.bus = 0  # 发电机所连的母线号
        self.name = ''  # 火电厂名称，用低压侧母线名代称
        self.bus_names = []  # 包含的母线名
        self.loads = []
        self.generators = []  # 厂内的发电机
        self.transformers = []  # 厂内的变压器，两种类型，一台或者连续两台升压
        self.buses = []  # 包含的母线号 


class SUBSTATION():  # 变电站
    def __init__(self):
        self.name = ''
        self.bus = 0
        self.bus_names = []  # 包含的母线名

        self.loads = []  # 厂内的发电机
        self.transformers = []  # 厂内的变压器，两种类型，一台或者连续两台升压
        self.buses = []  # 包含的母线号 
    
class CONVERTER_STATION():
    def __init__(self):
        self.bus = 0
        self.name = ''
        self.shunts = []
        pass 