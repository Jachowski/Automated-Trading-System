# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:37:29 2020

@author: padel
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)
import pandas as pd
import os
import backtrader as bt
import backtrader.indicators as btind
import backtrader.analyzers as btanalyzers
import datetime
import os.path 
import sys  
import yfinance as yf
import matplotlib.pyplot as plt

def Trading_simulator(strategy, title_name, start_date, end_date, start_cash=float,
                      commission=0, stake_val=int, curr_dir=str, plott=False):
    #Download title_dataframe
    data = yf.download(title_name, start=start_date, end=end_date)
    
    #Print df name
    print('The title we are simulating is {}'.format(title_name))
    
    data.to_csv(curr_dir+'/{}.csv'.format(title_name))
    
    # Inizializziamo istanza Cerebro
    cerebro = bt.Cerebro()
        
    # Aggiungiamo la strategia programmata nella classe
    cerebro.addstrategy(strategy)
        
    # Inseriamo i dati
    modpath = os.path.basename(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath,curr_dir+'/{}.csv'.format(title_name))
    
    # Salviamo i dati nella variabile data
    data = bt.feeds.YahooFinanceCSVData(
           dataname=datapath,
           fromdate=start_date,
           todate=end_date,
           reverse=False)
    
    # Aggiungiamo i dati a Cerebro
    cerebro.adddata(data)
    
    # Impostiamo il valore iniziale del portafoglio
    cerebro.broker.setcash(start_cash)
    
    # Impostiamo il numero di azione che traderemo
    cerebro.addsizer(bt.sizers.FixedSize, stake=stake_val)
    
    # Impostiamo il valore delle commissioni
    cerebro.broker.setcommission(commission)
    
    # Stampiamo le condizioni iniziali
    print('Valore iniziale Portafoglio: %.2f' % cerebro.broker.getvalue())
    
    # Lanciamo la nostra strategia
    cerebro.run()
    
    # Stampiamo le condizioni finali
    print('Valore Finale Portafoglio: %.2f' % cerebro.broker.getvalue())
    
    #Cancelliamo il dataframe scaricato, sempre per fare economia di spazio
    os.remove(curr_dir+'/{}.csv'.format(title_name))

    if plott==True:
        cerebro.plot(iplot=False)
    
    
    
    
    
    
    
    
