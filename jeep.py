#spline derivative returns

import numpy as np
from scipy.interpolate import UnivariateSpline as US
from scipy.interpolate import splder

def hill (prices, xaxis):
    
    spl = US(xaxis, prices, k = 3, s = 5)
    spl_der = spl.derivative() 
    av_der = np.sum(spl_der(xaxis))/len(spl_der(xaxis))
    return av_der

def jeep(file_list, ticker_array):
    #file_list is a string array
    #ticker_array is a list of pandas dataframes

    count = 0
    gather_results = {}

    for i in ticker_array:
        print(np.linspace(0,len(i)-1,len(i)))
        if len(i) ==150:
            av_der = hill(i['3'],np.linspace(0,len(i)-1,len(i)))
            gather_results[file_list[count]] = av_der
        count += 1
        continue  
    results = [(k, d[k]) for k in sorted(gather_results, key = gather_results \
        , reverse = 1)]
    
