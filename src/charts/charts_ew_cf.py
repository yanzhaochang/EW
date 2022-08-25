
import random 
import pandas as pd 

from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts.globals import ThemeType



def generate_ew_cf_data():
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
                        cf_result.append('银东闭锁')
    data = pd.DataFrame({"time_id": time_id, 'stage1_index': stage1_index, 'stage1_line': stage1_line, 
        'stage2_index': stage2_index, 'stage2_line': stage2_line,
        'stage3_index': stage3_index, 'stage3_line': stage3_line, 
        'stage4_index': stage4_index, 'stage4_line': stage4_line, 'cf_result': cf_result})
    data.to_csv('.\\data\\ew_cf.csv', index=None)  


def generate_ew_cf_tree():
    #generate_ew_cf_data()

    tree = Tree(init_opts=opts.InitOpts(width="500px", height="600px", page_title="连锁故障",
                                theme=ThemeType.INFOGRAPHIC, chart_id='ew_cf'))
    data = [{
        "name": "德州-济南II线",
        "children": [
            {"name": "聊城-济南II线", 
            "children": [
                {"name": '淄博-东营I线'},
                {"name": '淄博-东营II线'},
                {"name": '淄博-东营III线'}]},
            {"name": "聊城-济南I线"},
            {"name": "聊城-济南III线"}
        ]
    }]

    data_1 = []
    data_2 = [{"name": "聊城-济南I线"}, {"name": "聊城-济南III线"}]
    

    for item in data:
        data_1.append(opts.TreeItem(name=item['name'], 
                              value=None,
                              children=item['children'],
                              label_opts=opts.LabelOpts(font_size=30, color='rgb(255, 255, 255)')),)
    tree.add_js_funcs('''
            function update_ew_cf_data(data){ 
                var obj = eval(data);          
                let options = chart_ew_cf.getOption();    
                let nodesOption = options.series[0]; 
                nodesOption.data = obj;                                   
                chart_ew_cf.setOption(options); 
            }                               
            ''') 

    tree.add("", data_1, symbol_size=14, pos_left='20%', pos_right='20%',
        initial_tree_depth=2, 
        label_opts=opts.LabelOpts(opts.TextStyleOpts(font_size=50, color='rgb(0, 0, 0)')), 
        leaves_label_opts=opts.LabelOpts(opts.TextStyleOpts(font_size=50, color='rgb(0, 0, 0)')),
        tooltip_opts=opts.TooltipOpts(is_show=True, textstyle_opts=opts.TextStyleOpts(font_size=25))
           )

    tree.set_series_opts(label_opts=opts.LabelOpts(opts.TextStyleOpts(font_size=30, color='rgb(255, 255, 255)')))
    tree.set_global_opts(title_opts=opts.TitleOpts(title="连锁故障搜索", title_textstyle_opts=opts.TextStyleOpts(font_size=25, background_color='rgb(180, 157, 45)', color='rgb(230, 230, 230)'))) 
    return tree 

                
