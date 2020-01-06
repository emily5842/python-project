from flask import Flask,render_template
import pandas as pd
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline
from pyecharts.faker import Faker
from pyecharts.charts import Line
app = Flask(__name__)

app.debug = True


def timeline_pie(df) -> Timeline:
   attr = Faker.choose()
   tl = Timeline()
   for i in range(2011, 2019):
      pie = (
         Pie()
            .add(
            "数值",
            list(zip(list(df.地区), list(df["{}年".format(i)]))),
            rosetype="radius",
            radius=["30%", "55%"],
         )
            .set_global_opts(title_opts=opts.TitleOpts("人均消费".format(i)),
                             legend_opts=opts.LegendOpts(pos_left='20%'))
      )
      tl.add(pie, "{}年".format(i))
   return tl

def line_base(df) -> Line:
   r = (
      Line()
         .add_xaxis(list(df.columns))
         .add_yaxis("广东", list(df.loc[18]))
         .add_yaxis("新疆", list(df.loc[30]))
         .add_yaxis("河南", list(df.loc[15]))
         .add_yaxis("山东", list(df.loc[14]))
         .add_yaxis("内蒙古自治区", list(df.loc[4]))
         .add_yaxis("甘肃", list(df.loc[27]))
         .add_yaxis("四川", list(df.loc[22]))

         .set_global_opts(title_opts=opts.TitleOpts(title="本科人数单位（万人）"))
   )
   return r


def timeline_map(df) -> Timeline:
   tl = Timeline()
   for i in range(2011, 2019):
      map0 = (
         Map()
            .add(
            "本科高素质人才（单位：万人）", list(zip(list(df.地区), list(df["{}年".format(i)]))), "china", is_map_symbol_show=False
         )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="{}race of increase".format(i), subtitle="",
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                 font_style="italic")),
            visualmap_opts=opts.VisualMapOpts(min_=-1, max_=50),

         )
      )
      tl.add(map0, "{}年".format(i))
   return tl


def line_base1(dff) -> Line:
   r = (
      Line()
         .add_xaxis(list(dff.columns))
         .add_yaxis("广东", list(dff.loc[18]))
         .add_yaxis("新疆", list(dff.loc[30]))
         .add_yaxis("河南", list(dff.loc[15]))
         .add_yaxis("山东", list(dff.loc[14]))
         .add_yaxis("内蒙古自治区", list(dff.loc[4]))
         .add_yaxis("甘肃", list(dff.loc[27]))
         .add_yaxis("四川", list(dff.loc[22]))

         .set_global_opts(title_opts=opts.TitleOpts(title="本科人数单位（万人）"))
   )
   return r


# def funnel_base(dff1) -> Funnel:
#    tl = Timeline()
#    for i in range(2011, 2019):
#       c = (
#          Funnel()
#             .add("人口自然增长率", list(zip(list(dff1.地区), list(dff1["{}年".format(i)]))))
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="{}第三产业产出（单位：亿元）".format(i), subtitle="",
#                                       subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
#                                                                                  font_style="italic")),
#             visualmap_opts=opts.VisualMapOpts(min_=1, max_=10000)
#
#          )
#       )
#       tl.add(c, "{}年".format(i))


def line_base2(dff1) -> Line:
   r = (
      Line()
         .add_xaxis(list(dff1.columns))
         .add_yaxis("广东", list(dff1.loc[18]))
         .add_yaxis("新疆", list(dff1.loc[30]))
         .add_yaxis("河南", list(dff1.loc[15]))
         .add_yaxis("山东", list(dff1.loc[14]))
         .add_yaxis("内蒙古自治区", list(dff1.loc[4]))
         .add_yaxis("甘肃", list(dff1.loc[27]))
         .add_yaxis("四川", list(dff1.loc[22]))

         .set_global_opts(title_opts=opts.TitleOpts(title="第三产业（单位：亿元）"))
   )
   return r


def timeline_map2(dff1) -> Timeline:
   tl = Timeline()
   for i in range(2011, 2019):
      map0 = (
         Map()
            .add(
            "人均消费水平", list(zip(list(dff1.地区), list(dff1["{}年".format(i)]))), "china", is_map_symbol_show=False
         )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="{}第三产业产值（单位：亿元）".format(i), subtitle="",
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                 font_style="italic")),
            visualmap_opts=opts.VisualMapOpts(min_=4500, max_=100000),

         )
      )
      tl.add(map0, "{}年".format(i))
   return tl

@app.route('/',methods=("POST", "GET"))
def peopleNum():
   df = pd.read_csv(open('./static/分省本科招生.csv', encoding='gbk'))
   dff = pd.read_csv(open('./static/财政.csv', encoding='gbk'))
   dff1 = pd.read_csv(open('./static/第三产业.csv', encoding='gbk'))
   # df.to_html(header="true", table_id="table")
   city = list(df.地区)
   city1 = list(dff1.地区)
   city_str = " ".join(city)
   city_str1 = " ".join(city1)
   variable = {"name": city_str}
   variable1 = {"name": city_str1}
   city_num = []
   for i in range(2011, 2019):
      city_num.append(list(zip(list(df.地区), list(df["{}年".format(i)]))))
   city_num1 = []
   for i in range(2011, 2019):
      city_num1.append(list(zip(list(dff1.地区), list(dff1["{}年".format(i)]))))
   city_va = {"num":city_num}
   city_va1 = {'num1':city_num1}
   return render_template('index.html',variable=variable,tables=[df.to_html(classes='data')], titles=df.columns.values,city_va=city_va,
                          bar_data=timeline_pie(df).dump_options(),bar_data2=line_base(df).dump_options(),bar_data3=timeline_map(df).dump_options(),
                          table1s=[dff.to_html(classes='data1')], title1s=dff.columns.values,bar_data4=line_base1(dff).dump_options(),
                          table2s=[dff1.to_html(classes='data2')],title2s=dff.columns.values,variable1=variable1,city_va1=city_va1,
                          bar_data6=line_base2(dff1).dump_options(),bar_data7=timeline_map(dff1).dump_options())


if __name__ == '__main__':
   app.run()