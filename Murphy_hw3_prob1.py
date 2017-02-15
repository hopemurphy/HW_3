# Created by Hope Murphy

from pylab import imshow,spectral,show
from numpy import loadtxt


data = loadtxt("stm.txt",float)
imshow(data,origin="lower")
spectral()
show()