"""
Longest Collatz sequence

Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def p14():
    max = 0
    maxstart = 0
    for i in range(999999,1,-1):
        n = i
        counter = 0
        while n != 1:
            if n%2 == 0:
                n = int(n/2)
                counter +=1
            else:
                n = n*3 + 1
                counter +=1
        if counter > max:
            max = counter
            maxstart = i
        print(i, maxstart, max)
    return maxstart, max

"""
the above code is super slow ! 4min 20.5s to result

the project euler provided solution below took 33.7s

I see where I could have improved, mainly the recurisve function
"""


def countchain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + countchain(n/2)
    else: 
        return 1 + countchain(n*3 + 1)

def peulersol():
    longestchain = 0
    answer = -1

    for i in range(1,1000000):
        if countchain(i) > longestchain:
            longestchain = countchain(i)
            answer = i
    return answer, longestchain

print(peulersol())



