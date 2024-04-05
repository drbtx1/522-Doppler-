# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:46:32 2024

@author: dabuch
"""

import numpy as np
from matplotlib import pyplot as plt




g1 = 1
g2 = 5.45
G = 14.3
#2 = 10000000
d2 = 25.1
min = -60
max = 60000000
D1 = 1
D2 = 10000000
D3 =1000000000
#max_d1 = d2*2

upper_bound = max*2
lower_bound = -upper_bound
d1_array = []
D1_array = []
D2_array = []
D3_array = []

def integral(d1, upper, lower, spacing, D):
    sum = 0
    for delta1 in range(lower, upper, spacing):
        
        delta2 = d2 - (d1 - delta1)
        expression = (delta1-delta2)/(G2**2 - 1j*(g1 + g2 - 1j*delta1)*(delta1-delta2))
        
        probability = np.exp((-1*(delta1 - d1)**2)/(2*D*D))/((2*np.pi*D*D)**(1/2))
        sum = sum + (expression.imag)*probability*spacing
        #print(sum)
        
    return sum 

#im2 = []
#re2 = []


for d1 in range(min,max,100000):
    d1_array.append(d1)
    print(d1)
    
    D1_array.append(integral(d1, upper_bound, lower_bound, 100000, D1 ))
    D2_array.append(integral(d1, upper_bound, lower_bound, 100000, D2 ))
    D3_array.append(integral(d1, upper_bound, lower_bound, 100000, D3 ))
    
    
    
    #re2.append(expression.real)
    #im2.append(expression.imag)


title = "Imaginary part of p13 vs delta_1 with Doppler effects (d2 = 0), D = " + str(D1) 
plt.plot(d1_array,D1_array)
plt.title(title)
#plt.legend(["D =" + str(D1)])
plt.savefig(title + ".png")
plt.show()

title = "Imaginary part of p13 vs delta_1 with Doppler effects (d2 =0), D = " + str(D2) 
plt.plot(d1_array,D2_array)
plt.title(title)
#plt.legend(["D =" + str(D2)])
plt.savefig(title + ".png")
plt.show()

title = "Imaginary part of p13 vs delta_1 with Doppler effects (d2 = 0), D = " + str(D3) 
plt.plot(d1_array,D3_array)
plt.title(title)
#plt.legend(["D =" + str(D1)])
plt.savefig(title + ".png")
plt.show()
