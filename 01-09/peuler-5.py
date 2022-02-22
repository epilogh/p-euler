"""
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

"""
https://en.wikipedia.org/wiki/Least_common_multiple#Using_a_simple_algorithm
using this method

An array of the multiplicands
Original array
Multiplied array that has values

so long as the multiplied array has a set value of > 1 
we choose the smallest value in multiplied array and change that value for original og array value * multiplicands 
(+1 to multiplicands)

"""
def p5(array):
    multiplicands = [1 for x in range(len(array))]
    algoarray = array.copy() 
    # made a mistake here, doing "=" rather than copy for lists
    while len(set(algoarray)) != 1:
    # while list doesn't have identical values 
        current_min = min(algoarray) 
        #current minimum value in algorithm array
        indexcurmin = min([i for i in range(len(algoarray)) if algoarray[i]==min(algoarray)], key=lambda j: multiplicands[j])
        # this code ^ was created by DORON#8434 on the python discord after working through the problem with me
        # [i for i in range(len(algoarray)) if algoarray[i]==min(algoarray)] gives us list of algoarray indices with same min values
        # then the key=lambda j: multiplicands[j] gives us the multiplicand array values for those indices
        # then take min() of that 
        algoarray[indexcurmin] = arr[indexcurmin] * multiplicands[indexcurmin]
        #update current minium
        multiplicands[indexcurmin] += 1
        #update +1 to multiplicand     
        #using sleep cause I don't know how to debug
        # print("algoarray="+str(algoarray))
    return algoarray[0]

def brutep5():
    num = 20    
    while (num %  2 != 0 or  num %  3 != 0 or  num %  4 != 0 or  num %  5 != 0 or 
            num %  6 != 0 or  num %  7 != 0 or  num %  8 != 0 or  num %  9 != 0 or 
            num % 10 != 0 or  num % 11 != 0 or  num % 12 != 0 or  num % 13 != 0 or 
            num % 14 != 0 or  num % 15 != 0 or  num % 16 != 0 or  num % 17 != 0 or 
            num % 18 != 0 or  num % 19 != 0 or  num % 20 != 0):
        num += 20
        
    return num


arr = [i for i in range(1,21,1)]

"""
p5() takes a LONG TIME FYI

"""
p5()

"""
brutep5() takes like two seconds
"""

brutep5()
