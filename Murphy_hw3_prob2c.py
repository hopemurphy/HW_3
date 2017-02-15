# Created by Hope Murphy


# x for part a is: -9.999894245993346e-07 and -999999.999999
# x for part b is: -1.000000000001e-06 and -1000010.5755125057
# The correct answers are -1e-6 and -1,000,000, a2 and b1 are correct answers. 
# This is because there is minimal error in these two answers.
# a2 is off by 0.000001 and b1 is off by 0.000000000001 while the other numbers are significantly off from the right answer.

from math import sqrt


a=float(input("Enter the desired value for a:"))	
b=float(input("Enter the desired value for b:"))	
c=float(input("Enter the desired value for c:"))	


x_a2= (-b - sqrt(b**2 - 4*a*c))/(2*a)

x_b1= (2*c)/(-b - sqrt(b**2 - 4*a*c))


print("x for part c is:", x_b1 , 'and', x_a2)



# Enter the desired value for a:.001
# Enter the desired value for b:1000
# Enter the desired value for c:.001
# x for part b is: -1.000000000001e-06 and -999999.999999