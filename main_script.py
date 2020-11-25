# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:24:40 2020

@author: itsjachowski
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import backtrader as bt  # Import the backtrader platform
from pandas_datareader import data, wb
import yfinance as yf

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()
    
    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    
    # Set our desired cash start
    cerebro.broker.setcash(100000.0)
    
    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final conditions
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    