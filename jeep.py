#spline hill climb algo

#import pymongo 
import numpy as np
import datetime
from scipy.interpolate import UnivariateSpline as US
from scipy.interpolate import splder
import matplotlib.pyplot as plt
import math as m
#database config settings 
#connection = pymongo.MongoClient('localhost:27017')
#db = connection.StockMarketDB
#col = db.hourlyStatistics #this is where you select the table (to be redone)
#
#prices = []
#time = []
prices = np.loadtxt('prices',delimiter = ',') 

#for doc in col.find().sort('date', pymongo.ASCENDING):
#    prices.append(doc['low'])
#    time.append(doc['date'])
#
#xaxis = np.linspace(0,len(time),len(time))
xaxis = np.linspace(0,70,70)

spl = US(xaxis, prices, k = 3, s = 5)
spl_der = spl.derivative()


av_der = np.sum(spl_der(xaxis))/len(spl_der(xaxis))
print(av_der)


plt.plot(xaxis,spl_der(xaxis)+92,'y',xaxis,spl(xaxis),'b',xaxis,prices,'ro')
#plt.plot(xaxis,spl_der(xaxis)+99)
plt.show()

#Useful loop for debugging
#for i in range(1,len(prices)):
#   print(prices[i])
#   print(timep[i])
