"""Special Pythagorean triplet

Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Found out about Euclid's formula 
https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
a = m**2 - n**2 
b = 2mn
c = m**2 + n**2 

also fibonacci's method

and tried doing some complicated stuff
like getting triplets where x was a prime number
but couldn't get the rest of them
stuck for the entire day
then 
I realized it's actually much easier to find if you just force it
but not good time wise, especially if it's not a+b+c=1000 but instead somethgin much larger

"""


def p9():
    for x in range (1, 1000):
        for y in range (x+1, 1000):
            for z in range(y+1, 1000):
                if x*x + y*y == z*z and x+y+z == 1000:
                    print(x*y*z)
                    return None
    return None

         
p9()