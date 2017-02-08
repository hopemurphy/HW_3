# Hope Murphy Created 2/1/17


a_1= 15.67
a_2= 17.23
a_3= 0.75
a_4= 93.2

#a_5=12.0


A= int(input("Enter the desired value for A:"))	
Z= int(input("Enter the desired value for Z:"))


if A%2==0 and not Z%2==0:
	a_5= -12.0
elif A%2==0 and Z%2==0:
	a_5= 12.0
else: 
	a_5=0


B= (a_1 * A) - (a_2 * (A**(2/3))) - (a_3 * ((Z**2)/(A**(1/3)))) - (a_4 * (((A-2*Z)**2)/A)) - ((a_5)/(A**(1/2)))


print("For part a) The binding energy B is:", B)

print("For part b) The binding energy per nucleon is:", B/A)


#Output in the terminal
#HOPEs-MacBook-Air:desktop hopemurphy$ python Murphy_hw2_prob2.py
#Enter the desired value for A:58
#Enter the desired value for Z:28
#For part a) The binding energy B is: 490.78425241273493
#For part b) The binding energy per nucleon is: 8.46179745539198
#HOPEs-MacBook-Air:desktop hopemurphy$ python Murphy_hw2_prob2.py
#Enter the desired value for A:59
#Enter the desired value for Z:28
#For part a) The binding energy B is: 498.144677545714
#For part b) The binding energy per nucleon is: 8.443130127893458
#HOPEs-MacBook-Air:desktop hopemurphy$ python Murphy_hw2_prob2.py
#Enter the desired value for A:58
#Enter the desired value for Z:27
#For part a) The binding energy B is: 485.30934897614435
#For part b) The binding energy per nucleon is: 8.367402568554214