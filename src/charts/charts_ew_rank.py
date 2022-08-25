'''
rank图
'''
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid

import random 


def generate_ew_rank_data():
    time_id = [i for i in range(1, 25)]
    green_percent = []
    yellow_percent = []
    red_percent = []
    for i in range(24):
        a = random.uniform(0.7, 0.8)
        b = random.uniform(0.1, 0.15)
        d = 1 - a - b 
        green_percent.append(a)
        yellow_percent.append(b)
        red_percent.append(d)
    
    #data = pd.DataFrame({'time_id': time_id, 'level0_percent': green_percent, 'level1_percent': yellow_percent, 'level2_percent': red_percent})
    #data.to_csv('ew_rank.csv', sep=',', index=None)
    return time_id, green_percent, yellow_percent, red_percent

def generate_ew_rank_bar():
    time_id, green_percent, yellow_percent, red_percent = generate_ew_rank_data()

    bar = Bar(init_opts=opts.InitOpts(width="1850px", height="200px", theme=ThemeType.INFOGRAPHIC, chart_id='ew_rank'))
    
    bar.add_xaxis(time_id)
    bar.add_yaxis('0', green_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='green'), bar_width="50%")
    bar.add_yaxis('I', yellow_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='rgb(247, 237, 32)'), bar_width="50%")
    bar.add_yaxis('II', red_percent, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='rgb(214, 37, 39)'), bar_width="50%")
    
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(name=''), 
                    yaxis_opts = opts.AxisOpts(is_show=False),
                    legend_opts = opts.LegendOpts(is_show=False), 
                    title_opts = opts.TitleOpts(title=None, pos_left=0, pos_top=0), 
                    tooltip_opts=opts.TooltipOpts(is_show=False),
                    )  
    
    bar.add_js_funcs('''
        chart_ew_rank.on('click', function(params){
            window.connection.value = params.name;
            }); 
        document.addEventListener("DOMContentLoaded", function () {
                new QWebChannel( qt.webChannelTransport, function(channel) {
                    window.connection = channel.objects.connection;
                });
            });              
        ''')
    
    
    bar.add_js_funcs('''
            function update_ew_rank_data(data){ 
                var obj = eval(data);
                var level0_percent = obj[0];
                var level1_percent = obj[1];
                var level2_percent = obj[2];                
                let options = chart_ew_rank.getOption();    
                let nodesOption = options.series[0]; 
                nodesOption.data = level0_percent;
                let nodesOption1 = options.series[1]; 
                nodesOption1.data = level1_percent;
                let nodesOption2 = options.series[2]; 
                nodesOption2.data = level2_percent;                                
                chart_ew_rank.setOption(options); 
            }                               
            ''') 
           
    return bar 
# 立体圆柱用象形图加柱图实现，但需要修改JS程序，立体圆柱也不适合显示堆积图