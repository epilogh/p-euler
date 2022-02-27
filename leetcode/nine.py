"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.

"""

def isPalindrome(x: int) -> bool:
    temp = str(x)[::-1]
    if str(x) == temp:
        return True
    else: 
        return False
    
x= 121
print(isPalindrome(x))
x = -121
print(isPalindrome(x))
x= 10
print(isPalindrome(x))