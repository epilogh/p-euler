"""
Summation of primes

Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def p10():
    primes = sieveofe(2000000)
    sum = 0
    for item in primes:
        sum+=item
    return sum

def sieveofe(n):
    arr = []
    sieve = [True] * (n+1)
    for i in range(2,n+1):
        if sieve[i]:
            arr.append(i)
            for g in  range(i, n+1, i):
                sieve[g] = False
    return arr
    
print(p10())

"""
this one was easy 
what's up with all these prime number questions tho

"""