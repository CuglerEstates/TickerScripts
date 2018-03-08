# overarching function running script, this algo keeps the numbers, therefore
# it is the 'bookie'

#proper python modules used by other functions, one time load
import pymongo
import datetime
import numpy as np
import math as m
import matplotlib.pyplot as plt

#scripts we have written
import hill

#mode to run the script in (options are 'test' and 'running')
mode = 'test'

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

    for doc in col.find().sort('date', pymongo.ASCENDING):
        prices.append(doc['low'])
        time.append(doc['date'])
        xaxis = np.linspace(0,len(time),len(time))

#run functions
av_der= hill.hill(prices, xaxis) 

#display results
print(av_der)
