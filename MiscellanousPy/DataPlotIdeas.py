#!/bin/bash/python3

from this import d
from matplotlib import pyplot as plt 
import pandas as pd 
import os 
import numpy as np 

filename = [1,2,3,4,5,6,7]

data = np.loadtxt(filename)

print(data)

# data points
x = [data]
y = [10,30,50,80,100,130,180,200,300,400,500,700,900]

plt.plot(x,y)

plt.title("Coin Stats")

plt.xlabel("Average from phone farms")

plt.ylabel("Account Growth")

plt.show()



# Coin data indicates how much the account at hinjews house has went up

# x should be the averages it pulls in daily from phone farm.

# y should be the growth of the account goal of 100k