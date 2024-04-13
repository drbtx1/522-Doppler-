# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:07:48 2024

@author: dbtx
"""
from sympy import solve
from sympy import nsolve
from sympy import simplify
from sympy import symbols
from sympy import conjugate

d1, g, p11, p12, p13, p22, p23   = symbols('d1 g p11 p12 p13 p22 p23')
#L, G, g1,g2, d2 = symbols('L G g1 g2 d2')


L = 1.7
G = 14.3
g1 = 1 
g2 = 5.45
d2 = 25.1

'''e1 = -2*(g1 + L)*p11 + 2*g*p12_imag + 2*L*p22
e2 = -1j*g*p11 -(g1 +g2 +1j*d1 + 2*L)*(p12_real + 1j*p12_imag) -1j*G*p13 + 1j*g*p22
e3= -1j*G*(p12_real + 1j*p12_imag) -(g1 + 1j*(d1 + d2) + L)*p13 + 1j*g*(p23_real + 1j*p23_imag) 
e5 = 1j*g*p13 - 1j*G*p22 - (g1 + 1j*d2 + L)*(p23_real + 1j*p23_imag) + 1j*G*(1 - p11 - p22)
e6 = g2*p22 -G*p23_imag'''

#solutions = solve([e1,e2,e3,e5,e6], [p11,p12_real, p12_imag, p13, p22, p23_real, p23_imag ], dict=True)
#p12  = solutions[0][p]

e1 = -2*(g1 + L)*p11 + 1j*g*(conjugate(p12) - p12) + 2*L*p22
e2 = -1j*g*p11 -(g1 +g2 +1j*d1 + 2*L)*(p12) -1j*G*p13 + 1j*g*p22
e3= -1j*G*(p12) - (g1 + 1j*(d1 + d2) + L)*p13 + 1j*g*(p23) 
e5 = 1j*g*p13 - 1j*G*p22 - (g1 + 1j*d2 + L)*(p23) + 1j*G*(1 - p11 - p22)
e6 = g2*p22 + 1j*G*(p23 - conjugate(p23))

solutions = solve([e1,e2,e3,e5,e6], [p11,p12, p13, p22, p23 ],  dict=True)
print(solutions)
#p12  = solutions[0][p]


#print(simplify(solutions[0][p12_imag]))

#print(solutions[0][p23_real])
#print(solutions[0][p23_imag])
