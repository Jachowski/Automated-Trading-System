# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:41:19 2020

@author: padel
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)
import pandas as pd
import numpy as np
import os
import backtrader as bt
import backtrader.indicators as btind
import backtrader.analyzers as btanalyzers
import datetime
import sys 
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas_datareader as wb #import data, wb
plt.style.use('fivethirtyeight')

curr_dir='C:/Users/itsjachowski/Python/Trading Project/Pad'
os.chdir(curr_dir)

#Import the strategy you need
from Strategy_definition import Cross_Medie, TestStrategy

#Import the trader
from Trading_backtrader import Trading_simulator

#Set your parameters 
strategy=Cross_Medie
title_name='AMZN'
start_date=datetime.datetime(2017, 1, 1)
end_date=datetime.datetime(2019, 12, 31)
start_cash=100000.0
commission=0.0002 #If you want no commission set 0
stake_val=1000

#Insert the tickers where you want to perform the simulation on
#titles=['AMZN','GOOGL','MSFT','IBM','FCA','LDO','TSLA','NFLX','G']

Trading_simulator(strategy=strategy, title_name=title_name, start_date=start_date,
                      end_date=end_date, start_cash=start_cash,
                      commission=commission, stake_val=stake_val,
                      curr_dir=curr_dir, plott=True)

#Perform your simulation
#for title_name in titles:
#    Trading_simulator(strategy=strategy, title_name=title_name, start_date=start_date,
#                      end_date=end_date, start_cash=start_cash,
#                      commission=commission, stake_val=stake_val,
#                      curr_dir=curr_dir)
#    cerebro.plot()




