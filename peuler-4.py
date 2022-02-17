"""
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def p4():
    max = 0
    for i in range (999, 99, -1):
        for j in range(999, 99, -1):
            mult = j*i
            if isPal(mult) and mult > max:
                max = mult
    return max

"""
I was being stupid at first and starting at 100, 1000, and doing the same operation as above
then I stored the multiples in an array, then checked if they were palindromes ...  so bad
then I stored if palindrome, then start from 999"""

def isPal(arg):
    num = str(arg)
    rev = num[::-1]
    return num == rev
    # chararr = []
    # revchararr = []
    # for k in str(arg):
    #     chararr.append(int(k))
    # print(chararr)
    # for l in range(len(chararr)-1, -1, -1) :
    #     revchararr.append(chararr[l])
    # print(revchararr)
    # return chararr == revchararr   
    
"""
for isPal() I was initially making a char array, then reversing it, then comparing it
later found that ::-1 exists, it starts at the end of the strings and creates a slice with each string character
I'm sure it's faster 
"""
        
print(p4())