#spline derivative returns

import matplotlib.pyplot as py
import numpy as np
import pandas as pd
from scipy.interpolate import UnivariateSpline as US
from scipy.interpolate import splder
from collections import OrderedDict as OD
from itertools import islice


def hill (prices, xaxis):
    
    spl = US(xaxis, prices, k = 5, s = 5)
    spl_der = spl.derivative() 
    av_der = np.sum(spl_der(xaxis))/len(spl_der(xaxis))
    
    return av_der 

def jeep(file_list, ticker_array):
    #file_list is a string array
    #ticker_array is a list of pandas dataframes

    count = 0
    gather_results = {}
    results = []
    for i in ticker_array:
        if len(i) ==150:
            av_der = hill(i['3'],np.linspace(0,len(i)-1,len(i)))
            gather_results[file_list[count]] = av_der
        count += 1 
        continue  
    
    #massaging results into a portfolio format
    results = OD(sorted(gather_results.items(), key=lambda t: t[1], reverse = True)) #sorting dict
    result_top20  = list(islice(results.items(), 0, 20))# ripping the top 20 off
    result = pd.DataFrame.from_dict(result_top20) 
    x = 0
    divisor = result[1][0] 
    
    while x<=19:
       result[1][x] = result[1][x]/divisor
       x+=1 

    return result
    
