 # pip uninstall pandas_datareader
 # pip install pandas_datareader
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 
from pandas_datareader import data as wb 
import datetime              #不要忘记

start = datetime.datetime(2020,1,1)    #起始时间,注意是date不是data
end = datetime.date.today()        #结束时间,注意是date不是data

# 读取公司数据
aapl_stock = wb.DataReader("AAPL","yahoo",start,end)  
aapl_stock

aapl_stock.to_csv("AAPL_stock.csv")  # 保存数据

aapl_stock = pd.read_csv("AAPL_stock.csv")  # 读取本地
aapl_stock.head(10)                         # 默认5条，可改

aapl_stock.info()                           # 查看文件数据概要

aapl_stock.describe() # 统计量分析 数据量、标准差、最小值、下4分位数，中位数，上4分位数、最大值
aapl_stock.aggregate([min,max,np.mean,np.median])  # 选择统计量查看

# 绘图展示
# aapl_stock.plot()                           # 绘制在一张图上，无法清晰体现
aapl_stock.plot(subplots=True)                # columns分别绘制
aapl_stock.plot(figsize=(10,20),subplots=True)# figsize调整图像到合适大小
plt.show()                                    









