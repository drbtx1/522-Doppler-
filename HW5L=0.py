"""
Created on Tue Feb 27 10:59:17 2024

@author: dabuch
"""

import numpy as np
from matplotlib import pyplot as plt
g1 = 1
g2 = 5.45
#G1 = 1#10000000 #g on figure
G = 14.3
d2 = 25.1
L = 0
min = -100
max = 100
p11num = (G**2)*L*(d2 - L)
p11denom = (G**2)*(d2- L)*(3*L +2*g1) + (g1+L)*(g1**2 + (d2 + L)) + L*(g2 - L)*(L + g1)*(g1**2 + (d2 + L))
p11 = p11num/p11denom
p22 = G**2/(2*(G**2) + g2**2 +d2**2)
p23 = G*(1 - p11-2*p22)/(g2 + L + 1j*d2)

#Imp13 = []
#Rep13 = []
d1_array = []

im2 = []
re2 = []
for d1 in range(min,max):
    d1_array.append(d1)
    
    numerator = 1j*(p22 - p11)*(g1+ 1j*(d1 + d2) + L) +G*p23
    denominator = (g1 + g2 + 1j*d1 + 2*L)*(g1 + 1j*(d1 + d2) + L) + G**2
    expression = numerator/denominator
    re2.append(expression.real)
    im2.append(expression.imag)
plt.xlabel("delta1, MHz")    
plt.plot(d1_array,re2)
#plt.title("Real part of p13 vs delta_1")
#plt.show()    
title = "gamma1="+str(g1)+"MHz, gamma2="+str(g2)+"MHz, G="+str(G)+"MHz, delta2="+str(d2)+"MHz, " + "Lambda = " + str(L)

plt.plot(d1_array,im2)
plt.title(title)
plt.legend(["Real part of p12","Imaginary part of p12"])
#plt.savefig("d2/" +title + ".png")
plt.show() 
   