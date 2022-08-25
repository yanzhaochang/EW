
import pandas as pd 
import random 
import apis 

def calculate_ew_cf_data():
    lines = pd.read_csv('.\\conf\\lines.csv', header=0, encoding='GBK', engine='python')
    
    time_id = []
    stage1_line, stage1_index = [], []
    stage2_line, stage2_index = [], []
    stage3_line, stage3_index = [], []
    stage4_line, stage4_index = [], []
    cf_result = []
    for i in range(24):
        lines_name = lines['名称'].values.tolist()
        for j in range(5):
            lines_name_1 = lines_name.copy()
            line1 = random.choice(lines_name_1)
            lines_name_1.remove(line1)
            lines_2 = random.sample(lines_name_1, 4)
            for line_2 in lines_2:
                lines_name_1.remove(line_2)
            for k in range(len(lines_2)):    
                lines_name_2 = lines_name_1.copy()
                lines_3 = random.sample(lines_name_2, 3)
                for line_3 in lines_3:
                    lines_name_2.remove(line_3)
                for m in range(len(lines_3)):    
                    lines_name_3 = lines_name_2.copy()
                    lines_4 = random.sample(lines_name_3, 3)
                    for n in range(len(lines_4)):    
                        time_id.append(i+1)
                        stage1_line.append(line1)
                        stage1_index.append(j+1)
                        stage2_line.append(lines_2[k])
                        stage2_index.append(k+1)
                        stage3_line.append(lines_3[m])
                        stage3_index.append(m+1)
                        stage4_line.append(lines_4[n])
                        stage4_index.append(n+1)
    
    apis.add_ew_cf_column('time_id', time_id)                    
    apis.add_ew_cf_column('stage1_index', stage1_index)  
    apis.add_ew_cf_column('stage1_line', stage1_line)  
    apis.add_ew_cf_column('stage2_index', stage2_index)  
    apis.add_ew_cf_column('stage2_line', stage2_line)  
    apis.add_ew_cf_column('stage3_index', stage3_index)  
    apis.add_ew_cf_column('stage3_line', stage3_line)  
    apis.add_ew_cf_column('stage4_index', stage4_index)  
    apis.add_ew_cf_column('stage4_line', stage4_line)  