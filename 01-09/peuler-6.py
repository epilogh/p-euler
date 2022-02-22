"""
Sum square difference

Problem 6

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + .... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1+2+...+10)**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025-385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sumsquare():
    sum = 0
    x = [num**2 for num in range(1,101)]
    for item in x: 
        sum += item
    return sum

def squaresum():
    sum = 0 
    for x in range(1,101):
        sum += x
    sum = sum**2
    return sum

def p6():
    return squaresum() - sumsquare()

print(p6())