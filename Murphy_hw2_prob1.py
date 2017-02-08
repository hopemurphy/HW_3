# Hope Murphy Created 2/6/17

from math import sqrt

x= int(input("Enter the desired x in lightyears (distance between spaceship and planet):"))	#x light years away 

v= float(input("Enter the desired value for v as a fraction of the speed of light (in m/s):"))	


# x needs to be in meters 
x_0 = 9.461E15 * x


# Ex. V=.9 needs to become V=.9c
# c=2.998E8
v_0 = v * 2.998E8


gamma = 1/(sqrt(1-(v**2)))


# This is the time percieved by a person on Earth
t_0 = x_0 / (v_0*3.154E7)


print ("Time percieved by the observer in the rest frame:",t_0, "years")

# This is the time percieved by a person in the spaceship
t=t_0 / gamma

print ("Time percieved by the person in the spaceship",t, "years")


#Output in the terminal
#hopes-air:desktop hopemurphy$ python Murphy_hw2_prob1.py
#Enter the desired x in lightyears (distance between spaceship and planet):10
#Enter the desired value for v as a fraction of the speed of light (in m/s):.9
#Time percieved by the observer in the rest frame: 11.117348388909265 years
#Time percieved by the person in the spaceship 4.84593981473902 years
#hopes-air:desktop hopemurphy$ python Murphy_hw2_prob1.py
#Enter the desired x in lightyears (distance between spaceship and planet):10
#Enter the desired value for v as a fraction of the speed of light (in m/s):.98
#Time percieved by the observer in the rest frame: 10.209809744916672 years
#Time percieved by the person in the spaceship 2.0317264862881688 years
#hopes-air:desktop hopemurphy$ python Murphy_hw2_prob1.py
#Enter the desired x in lightyears (distance between spaceship and planet):10
#Enter the desired value for v as a fraction of the speed of light (in m/s):.999
#Time percieved by the observer in the rest frame: 10.015629179197536 years
#Time percieved by the person in the spaceship 0.44780056150314096 years

