"""
Lattice paths

Problem 15

https://projecteuler.net/project/images/p015.png

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

"""
thinking of something like all array zero
default is right, if you go switch from right to down or down to right you flip that element to one?
thoughts? 

gonna finish my workout
"""
import numpy as np

two = np.zeros(4).reshape(2,2)
twenty = np.zeros(400).reshape(20,20)
print(two)
print(twenty)



def p15():

    return True

