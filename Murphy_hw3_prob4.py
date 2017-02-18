from numpy import linspace
from pylab import plot, show, xlabel,ylabel
from math import e


# integrand from 0 to x
# Calculate for x=0-3 in steps of 0.1, therefore N=30
def f(t):
    return e**(t**2) 
    

y=[]
x=linspace(0,3,31,endpoint=True)

def frange(A,B,jump):
    while A<B:
        yield A
        A += jump
        
    
for t in frange(0,3.1,0.1):
    a=0
    b=t
    N=100
    h=(b-a)/N
    
    s=0.5*f(a) + 0.5*f(b)
    for j in range(1,N):
        s += f(a+j*h)
    E_x= s*h
    
    y.append(E_x)
    
    
print (y)
        
plot(x,y)
xlabel('x')
ylabel('E_x')
show()
