#spline derivative returns

import numpy as np
from scipy.interpolate import UnivariateSpline as US
from scipy.interpolate import splder

def hill (prices, xaxis):
    
    spl = US(xaxis, prices, k = 3, s = 1)
    spl_der = spl.derivative() 
    av_der = np.sum(spl_der(xaxis))/len(spl_der(xaxis))
    return av_der
