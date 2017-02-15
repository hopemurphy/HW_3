# Created by Hope Murphy
# Using trapizodal rule

from numpy import exp
import numpy as np
import math
from pylab import plot,show, imshow
# Using N=1000
# Hint: integrand at x=0 is zero


#T= float(input("Enter the desired value for T (in K):"))
V= 0.001 # in cubic meters of solid aluminum
p= 6.022E28 # in 1/m^3
theta= 428 # in K
k= 1.38E-23 # in J/K


def f(x):
	return ((x**4)*(math.e**x))/(((math.e**x) - 1)**2)


temp=[]
Temp=np.linspace(5,500,495,endpoint=True)
for T in range(5,500):
	N=1000
	# integrand from 0 to theta/T
	a= 0
	b= theta/T
	h=(b-a)/N

	const = (9*V*p*k*((T/theta)**3)) 

	C_V = 0.5*f(b)
	for j in range (1,N):
		C_V += f(a+j*h)

	t= const*C_V*h
	temp.append(t)
	# print(const*C_V*h)
	# python Murphy_hw3_prob3.py
	# Enter the desired value for T (in K):100
	# 1152.7215828175533


# make graph of function
plot(Temp,temp)
show()

