import pandas as pd
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline

df = pd.read_csv(open('./static/分省本科招生.csv', encoding='gbk'))
city = list(df.地区)
city_str = " ".join(city)
variable = {"name": city_str}
city_num = []
for i in range(2011, 2019):
  city_num.append(list(zip(list(df.地区), list(df["{}年".format(i)]))))
city_va = {"num":city_num}
A=list(df.地区)
B=list(df.columns)
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline




