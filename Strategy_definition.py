# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:38:06 2020

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
import matplotlib
from pandas_datareader import data, wb
import yfinance as yf

# Create a Strategy Test
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        if self.dataclose[0] < self.dataclose[-1]:
            # current close less than previous close

            if self.dataclose[-1] < self.dataclose[-2]:
                # previous close less than the previous close

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.buy()
    


# Create a Double Crossover Strategy
class Cross_Medie(bt.Strategy):
    #definiamo la media veloce e la media lenta
    params = (('Med_vel', 50), ('Med_len', 100))

    #inizializziamo le due medie
    def __init__(self):
        self.sma_vel = btind.SMA(period=self.p.Med_vel)
        self.sma_len = btind.SMA(period=self.p.Med_len)

    #definiamo il segnale di acquisto/vendita
        self.buysig = btind.CrossOver(self.sma_vel, self.sma_len)
        
        # salviamo di dati di closing
        self.dataclose = self.datas[0].close
        
    #Il metodo next racchiude la strategia; 
    #se siamo in posizione ci fa chiudere e ribaltare altrimenti 
    #se non siamo in posizione ci fa entrare a mercato    
             
    def next(self):
        if self.position.size:
            if self.buysig < 0:
                self.close()
                self.sell()
            elif self.buysig > 0:
                self.close()
                self.buy()
                    
        else:
            if self.buysig > 0:
                self.buy()
            elif self.buysig < 0:
                self.sell()
                
    def stampa(self, txt, dt=None):
        
        #Funzione di stampe per capire cosa sta accadendo
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # ordine acquisto/vendita accettato
            return

        # Verifica se ordine completato
        if order.status in [order.Completed]:
            if order.isbuy():
          #Stampiamo dettaglio di quantità, prezzo e commissioni
                self.stampa(
                    'ACQ ESEGUITO, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM %.2f' %
                    (order.executed.size,
                     order.executed.price,
                     order.executed.value,
                     order.executed.comm        
                     ))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Vendita
                self.stampa('VEND ESEGUITA, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM %.2f' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.value,
                          order.executed.comm
                          ))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.stampa('Ordine Cancellato')

        self.order = None
        
    # Questa funzione ci restituisce il P&L dell'operazione chiusa
    
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.stampa('PROFITTO OPERAZIONE, LORDO %.2f, NETTO %.2f' %
                 (trade.pnl, trade.pnlcomm))