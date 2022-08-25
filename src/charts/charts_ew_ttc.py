from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Gauge

import random 
import pandas as pd 

def generate_ew_ttc_data():
    time_id = []
    ttc_name = []
    plan_power = []
    up_power = []
    low_power = []
    name = ['河北山东断面', '山东半岛断面']
    for i in range(24):
        for j in name:
            time_id.append(i + 1)
            ttc_name.append(j)
            plan_power.append(random.uniform(12, 16))
            up_power.append(random.uniform(18.5, 19.8))
            low_power.append(random.uniform(17, 18))
    data = pd.DataFrame({'time_id': time_id, 'ttc_name': ttc_name, 
        'plan_power': plan_power, 'up_power': up_power, 'low_power': low_power})
    data.to_csv('.\\data\\ew_ttc.csv', sep=',', index=None)

def generate_ew_ttc_gauge():
    generate_ew_ttc_data()
    
    gauge = Gauge(init_opts=opts.InitOpts(width="350px", height="300px",
                                theme=ThemeType.INFOGRAPHIC, chart_id='ew_ttc'))
    
    gauge.add("", [("计划功率/GW", 14.12)], radius="85%", min_=12, max_=20, start_angle=210, end_angle=-30,
        split_number=4,
        title_label_opts=opts.GaugeTitleOpts(font_size=20, color="rgb(230, 230, 230)", offset_center=[-90, 140]),
        detail_label_opts=opts.GaugeDetailOpts(is_show=True, offset_center=[50, 140], font_size=20),
        axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(
                color=[(0.9425, "green"), (0.9515, "rgb(247, 237, 32)"), (1, "rgb(214, 37, 39)")], width=15)),
        )
    gauge.add_js_funcs('''
            function update_ew_ttc_data(data){   
                var obj = eval(data);
                let options = chart_ew_ttc.getOption();    
                let nodesOption = options.series[0];
                var newData = obj.data;
                var new_color = obj.color;
                nodesOption.data = newData;
                nodesOption.axisLine.color = new_color;

                let titleOption = options.title[0];
                titleOption.subtext = obj.subtext;
                chart_ew_ttc.setOption(options); 
            }     
            ''')          

    gauge.set_global_opts(title_opts=opts.TitleOpts(title="TTC预警", subtitle="河北山东断面",
        title_textstyle_opts=opts.TextStyleOpts(font_size=25, background_color='rgb(180, 157, 45)', color='rgb(230, 230, 230)', )),
        legend_opts=opts.LegendOpts(is_show=False),)
    return gauge 