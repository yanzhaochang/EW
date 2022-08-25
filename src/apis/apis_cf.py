from database import EWCF 

def add_ew_cf_column(column, value):
    EWCF[column] = value

def get_ew_cf_column(column):
    return EWCF[column] 

def get_ew_cf_stage1_line(time_id, stage1_index): 
    lines = set(EWCF['stage1_line'][i] for i in range(len(EWCF['time_id'])) if (EWCF['time_id'][i] == time_id and EWCF['stage1_index'][i] == stage1_index)) 
    return list(lines)[0] 

def get_ew_cf_stage2_line(time_id, stage1_index, stage2_index):
    lines = set(EWCF['stage1_line'][i] for i in range(len(EWCF['time_id'])) if (EWCF['time_id'][i] == time_id and EWCF['stage1_index'][i] == stage1_index and EWCF['stage2_index'][i] == stage2_index)) 
    return list(lines)[0]

def combine_cf_data(time_id, stage1_line):
    label = {"show": 'true', "position": "top",
                        "color": "rgb(255, 255, 255)",
                        "margin": 8, "fontSize": 15}
    data = {}
    data['name'] = stage1_line 
    data['label'] = label 
    data['children'] = []
    # 先筛选time_id
    a = [i for i in range(len(EWCF['time_id'])) if EWCF['time_id'][i] == time_id]
    # 筛选stage1_line
    b = [i for i in a if EWCF['stage1_line'][i] == stage1_line]
     
    stage2_line = list(set(EWCF['stage2_line'][i] for i in b if EWCF['stage1_line'][i] == stage1_line)) 
    for k in range(len(stage2_line)):
        data['children'].append({'name': stage2_line[k], 'children': [], 'label': label})
        
        c = [i for i in b if EWCF['stage2_line'][i] == stage2_line[k]]
        stage3_line = list(set(EWCF['stage3_line'][i] for i in c if EWCF['stage2_line'][i] == stage2_line[k])) 
        for m in range(len(stage3_line)):
            data['children'][k]['children'].append({'name': stage3_line[m], 'children': [], 'label': label})        
            d = [i for i in c if EWCF['stage3_line'][i] == stage3_line[m]]
            
            stage4_line = list(set(EWCF['stage4_line'][i] for i in d if EWCF['stage3_line'][i] == stage3_line[m]))

            for n in range(len(stage4_line)):
                data['children'][k]['children'][m]['children'].append({'name': stage4_line[n], 'label': label}) 
                          
    return [data] 