import pandas as pd
from pyecharts.globals import ThemeType, CurrentConfig, GeoType
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode
import random 


icon_substation = "image://D:/code/ew/img/变电站.svg"
icon_plant = "image://D:/code/map/ew/发电站.svg"
icon_convert = "image://D:/code/ew/img/换流站.svg"




def generate_ew_grid():
    geo = Geo(init_opts=opts.InitOpts(width="1000px", height="700px", page_title="山东电网",
                                theme=ThemeType.INFOGRAPHIC, chart_id='ew_grid')) 

    geo = generate_basic_map(geo)
    geo = init_plant_substation(geo)
    #init_lines_flow(geo)
    geo.set_global_opts(tooltip_opts=opts.TooltipOpts(trigger=None, is_show=False,), legend_opts=opts.LegendOpts(is_show=False))
    return geo 

def generate_basic_map(geo):
    geo.add_schema(maptype='山东', zoom=1.2,
        #itemstyle_opts=opts.ItemStyleOpts(color='rgb(66, 63, 80)', border_color="rgb(127, 135, 179)", border_width=1), 
              
        #    emphasis_itemstyle_opts=opts.ItemStyleOpts(color='rgb(66, 63, 80)')
        )     
    
    geo.add_js_funcs('''
        chart_ew_grid.on('click', function(params){
            if (params.seriesName){
                var sv = {"seriesName": params.seriesName, "seriesType": params.seriesType, "name": params.name} 
                var json_data = JSON.stringify(sv);
                window.connection.value = json_data;
            }
            });
        chart_ew_grid.on('dblclick', function(params){
            });  
        chart_ew_grid.on('contextmenu', function(params){
            window.mouse_location = chart_grid.convertFromPixel('geo', [params.event.offsetX, params.event.offsetY]);  // 鼠标的经纬度坐标设为了全局变量
            }); 
        function clear_node(){
            let options = chart_ew_grid.getOption();
            var index = options.series.findIndex(element => element.name == "节点");
            let nodesOption = options.series[index].data;        
            while(nodesOption.length > 0) {
                nodesOption.pop();
            }
            chart_ew_grid.setOption(options);
        }    
        function clear_line(){
            let options = chart_ew_grid.getOption();
            var index = options.series.findIndex(element => element.name == "线路");
            let linesOption = options.series[index].data;        
            while(linesOption.length > 0) {
                linesOption.pop();
            }            
            chart_ew_grid.setOption(options);
        }
        function add_node(Node){
            var newNode = eval(Node);
            let options = chart_ew_grid.getOption();
            var index = options.series.findIndex(element => element.name == "节点");
            let nodesOption = options.series[index].data; 
            nodesOption.push(newNode);
            chart_ew_grid.setOption(options);                         
        }   
        function add_line(line){
            var newLine = eval(line);
            let options = chart_ew_grid.getOption(); 
            var index = options.series.findIndex(element => element.name == "线路");   
            let linesOption = options.series[index].data;        
            linesOption.push(newLine);
            chart_ew_grid.setOption(options);
        }   
        document.addEventListener("DOMContentLoaded", function () {
                new QWebChannel( qt.webChannelTransport, function(channel) {
                    window.connection = channel.objects.connection;
                });
            });           
            ''')        
    return geo         

def init_plant_substation(geo):

    geo.add_coordinate(name="鲁邹县G", longitude=116.952279, latitude=35.330448)
    geo.add_coordinate(name="鲁淄川", longitude=117.982036, latitude=36.644972)

    geo.add_coordinate(name="河北山东断面1", longitude=117.286494, latitude=38.086073)
    geo.add_coordinate(name="河北山东断面2", longitude=115.620379, latitude=36.971876)
    
    geo.add_coordinate(name="山东半岛断面1", longitude=119.437524, latitude=37.071148)
    geo.add_coordinate(name="山东半岛断面2", longitude=119.785668, latitude=35.709988)
    
    geo.add(series_name='节点', data_pair=[('鲁邹县G', 2), ('鲁淄川', 35)], symbol_size=20, color="black", 
            label_opts=opts.LabelOpts(position="top", is_show=True, formatter=JsCode(                    
                """function(params) {
                    if ('value' in params.data) {
                        return params.data.name;
                    }
                }"""),), 
                itemstyle_opts=opts.ItemStyleOpts(color='rgb(50, 84, 111)'), is_selected=True)    

    geo.add("断面", [('河北山东断面1', '河北山东断面2'), ('山东半岛断面1', '山东半岛断面2')], type_=ChartType.LINES, is_polyline=True,
        effect_opts=opts.EffectOpts(is_show=False, symbol=SymbolType.ARROW, symbol_size=6, color ='yellow'), 
        linestyle_opts=opts.LineStyleOpts(is_show=True, color='rgb(244, 138, 10)', width=10, curve=0.2),
        label_opts=opts.LabelOpts(position="top", is_show=True))     
    
    geo.add("线路", [('鲁邹县G', '鲁淄川'),], type_=ChartType.LINES, is_polyline=True,
        effect_opts=opts.EffectOpts(is_show=True, symbol=SymbolType.ARROW, symbol_size=6, color ='yellow'), 
        linestyle_opts=opts.LineStyleOpts(is_show=True, color='rgb(130, 138, 110)', width=3, curve=0.2),
        label_opts=opts.LabelOpts(position="top", is_show=True))      

    return geo 


     