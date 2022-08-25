

from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid

import random 
import pandas as pd 

def generate_ew_frequency_data():
    time_id = []
    green_percent = []
    yellow_percent = []
    red_percent = []
    hvdc = []
    events = ['鲁固', '扎青', '银东', '陇东']
    for i in range(24):
        for event in events:
            a = random.uniform(0.7, 0.8)
            b = random.uniform(0.1, 0.15)
            d = 1 - a - b 
            green_percent.append(a)
            yellow_percent.append(b)
            red_percent.append(d)
            hvdc.append(event)
            time_id.append(i+1)

    data = pd.DataFrame({'time_id': time_id, 'event': hvdc, 'level0_percent': green_percent, 'level1_percent': yellow_percent, 'level2_percent': red_percent})
    data.to_csv('.\\data\\ew_frequency.csv', sep=',', index=None)        

def generate_ew_frequency_bar():
    generate_ew_frequency_data()
    
    events = ['鲁固', '扎青', '银东', '陇东']

    green_percent = []
    yellow_percent = []
    red_percent = []
    for i in range(len(events)):
        a = random.uniform(0.7, 0.8)
        b = random.uniform(0.1, 0.15)
        d = 1 - a - b 
        green_percent.append(a)
        yellow_percent.append(b)
        red_percent.append(d)

    bar = Bar(init_opts=opts.InitOpts(width="350px", height="300px", theme=ThemeType.INFOGRAPHIC, chart_id='ew_frequency'))
    
    bar.add_xaxis(['鲁固', '扎青', '银东', '陇东'])
    bar.add_yaxis('0', green_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='green'), bar_width="50%")
    bar.add_yaxis('I', yellow_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='rgb(247, 237, 32)'), bar_width="50%")
    bar.add_yaxis('II', red_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='rgb(214, 37, 39)'), bar_width="50%")
    bar.reversal_axis()

    bar.add_js_funcs('''
            function update_ew_frequency_data(data){ 
                var obj = eval(data);
                var level0_percent = obj[0];
                var level1_percent = obj[1];
                var level2_percent = obj[2];                
                let options = chart_ew_frequency.getOption();    
                let nodesOption = options.series[0]; 
                nodesOption.data = level0_percent;
                let nodesOption1 = options.series[1]; 
                nodesOption1.data = level1_percent;
                let nodesOption2 = options.series[2]; 
                nodesOption2.data = level2_percent;                                
                chart_ew_frequency.setOption(options); 
            }                              
        ''')

    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False), 
                    yaxis_opts = opts.AxisOpts(is_show=True),
                    legend_opts = opts.LegendOpts(is_show=False), 
                    title_opts = opts.TitleOpts(title='频率预警', pos_left=0, pos_top=0,
                    title_textstyle_opts=opts.TextStyleOpts(font_size=25, background_color='rgb(180, 157, 45)', color='rgb(230, 230, 230)', )), 
                    tooltip_opts=opts.TooltipOpts(is_show=False),)  
    return bar 