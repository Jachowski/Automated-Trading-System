# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:02:32 2020

@author: itsjachowski
"""

# Download and save 
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)
df = data.get_data_yahoo('TGYM.MI', start, end)
df.to_csv('C:/Users/itsjachowski/Python/TGYM.csv')

# Datas are in a subfolder of the samples. Need to find where the script is
# because it could have been called from anywhere
modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, 'C:/Users/itsjachowski/Python/TGYM.csv')

# Create a Data Feed
data = bt.feeds.YahooFinanceData(
    dataname=datapath,
    # Do not pass values before this date
    fromdate=datetime.datetime(2010, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2019, 12, 31),
    reverse=False)
        