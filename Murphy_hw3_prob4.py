# Created by Hope Murphy

from math import e


# integrand from 0 to x
# Calculate for x=0-3 in steps of 0.1, therefore N=30
def f(t):
	return e**(t**2) 

# x =['0', '1', '2', '3']

a= 0
b= 1
N= 10
h= (b-a)/N

E1= 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
	E1 += f(a+k*h)

print(h*E1)


a2= 0
b2= 2
N= 20
h= (b2-a2)/N

E2= 0.5*f(a2) + 0.5*f(b2)
for k in range(1,N):
	E2 += f(a2+k*h)

print(h*E2)


a3= 0
b3= 3
N= 30
h3= (b3-a3)/N

E3= 0.5*f(a3) + 0.5*f(b3)
for k in range(1,N):
	E3 += f(a3+k*h)

print(h*E3)


