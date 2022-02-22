"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

"""
https://stackoverflow.com/a/11620399
Kudos to  user448810  for sharing this solution to find primes until n 
Super intuitive solution after I understood it all

Had I not found it I would have still been trying to brute force my way up to 600851475143
"""

import math
def p3():
    num = 600851475143
    sqrt = math.floor(math.sqrt(num))
    # Simple, we want to take find the square root of the number in order to know what the largest factor could be
    arr = primes(sqrt)
    # Array of primes from our "Prime function"
    final = []
    #Initialize empty array
    [final.append(j) for j in arr if num % j == 0]
    #Add our prime factors to new array
    return str(final[-1]) + " is the largest prime factor of 600851475143"
    # Return the largest prime factor, I initially had (max(final)) but I think final[-1] is faster ? idk 
    
def primes(n):
    arr = [] # My addition
    sieve = [True] * (n+1)
    # Create a list of True values
    for p in range(2, n+1):
    # Loop through range from 2 to n+1 
        if (sieve[p]):
        # If that value in list "sieve" is True (You'll see where we're going with this)
        # Then it's prime
            arr.append(p) # My addition
            for i in range(p, n+1, p):
            # Loop through range from P (Number in initial for loop) in increments of P (multiples)
                sieve[i] = False
                # Make all multiples of P -- False that way when we go back to the If statement, it won't recognize those values as True/Prime
    return arr

p3()