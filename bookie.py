# overarching function running script, this algo keeps the numbers, therefore
# it is the 'bookie'

#proper python modules used by other functions, one time load
import os
import pandas
#import pymongo
import datetime
#import tailer
import numpy as np
import math as m
import matplotlib.pyplot as plt

#algos we have written
from jeep import jeep

#mode to run the script in (options are 'test' and 'running')
mode = 'set'



if mode == 'set':
    
    #PURPOSE: this provides 150 test points of data. 
    #VAR: file_list is the list of files stored as string names, so it can be reused
    #           as a list of ticker names in the same order as ticker_array
    #VAR: ticker_array holds the CSV data of a ticker

    os.chdir('/home/stefan/Stocks/TickerScripts/refinedstock/')
    file_list = os.listdir()
    ticker_array = []  

    for i in file_list: 
        holder = pandas.read_csv(i).tail(150)
        ticker_array.append(holder) 
        


if mode == 'test':
    prices = np.loadtxt('prices',delimiter = ',')
    time = np.linspace(0,70,70)
    xaxis = np.linspace(0,70,70)

if mode == 'running':
    #database config settings 
    connection = pymongo.MongoClient('localhost:27017')
    db = connection.StockMarketDB
    col = db.hourlyStatistics #this is where you select the table (to be redone)
    
    prices = []
    time = []
    #the block below is shit. 
    for doc in col.find().sort('date', pymongo.ASCENDING):
        prices.append(doc['low'])
        time.append(doc['date'])
        xaxis = np.linspace(0,len(time),len(time))


#run library of functions
jeepp = jeep(file_list,ticker_array)

print(jeepp)
