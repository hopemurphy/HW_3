# Created by Hope Murphy 

from math import sqrt


a=float(input("Enter the desired value for a:"))	
b=float(input("Enter the desired value for b:"))	
c=float(input("Enter the desired value for c:"))	

#part a
x_a1= (-b + sqrt(b**2 - 4*a*c))/(2*a)
x_a2= (-b - sqrt(b**2 - 4*a*c))/(2*a)


#part b
x_b1= (2*c)/(-b - sqrt(b**2 - 4*a*c))
x_b2= (2*c)/(-b + sqrt(b**2 - 4*a*c))


print("x for part a is:", x_a1 , 'and', x_a2)
print("x for part b is:", x_b1 , 'and', x_b2)



# Enter the desired value for a:.001
# Enter the desired value for b:1000
# Enter the desired value for c:.001
# x for part a is: -9.999894245993346e-07 and -999999.999999
# x for part b is: -1.000000000001e-06 and -1000010.5755125057

# The answers are similar but not identical.
# There is some differnece in the precision of the numbers.
# These differneces are most likely due to python's problem with subbtraction and division. 
