"""
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

"""
gonna do the sieve thing, I have to remember...

sieve of erathones or something. 


"""

def p7(n=1):
    # default value
    arr = sieveofe(n)
    # call sieve for default value at first
    if len(arr) > 10000:
        #if len(sieve result) does contain the 10001st prime
        return arr[10000]
        # return the 10001 prime
    else:
        return p7(n+1000)
        # recursively call p7 which calls sieve to (n+1000) 
        # chose 1000 cause why not, it's a big enough number to limit iterations
        # but not overshoot the value of 10001

            
def sieveofe(n):
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

print(p7())