import numpy as py 
import seaborn as sns 
import pandas as pd 
import hurst as h 
from hurst import random_walk, compute_Hc 
import matplotlib as plt 
import yfinance as yf 
import pprint as pp 

#Inputs below for inital python implimentation. These will be moved to forms on our website 

company = 'tsla'

time_span = '2019-05-01','2022-05-01'

start_date, end_date = time_span
#https://stackoverflow.com/questions/18372952/split-tuple-items-to-separate-variables 


yf.Ticker(company) 

pp.pprint(company.info)


df = yf.download(company, 
start = start_date, 
end = end_date, 
progress = False)


plot = df["Adj Close"].plot(title = company)

plot.show









