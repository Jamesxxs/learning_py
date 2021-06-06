####################################################################################################
# 6.4 Boolean function
def is_between(x, y, z):
    return x <= y <= z


print(is_between(1, 5, 3))


# 6.8 Checking types
# isinstance(value,type)
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined to negetive integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


####################################################################################################
# Exercise
# Ex6,2
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


# print(ack(3,4))
# Ex6.3
from Char6.palindrome import first,middle,last
def is_palindrome(word):
    if len(word)<=1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))

#print(is_palindrome(''))
#print(is_palindrome('oto'))
#print(is_palindrome('otoo'))

#Ex6.4
def is_power(a,b):
    if a==b:
        return True
    elif a%b==0:
        return is_power(a/b,b)
    else:
        return False

#print(is_power(25,5))

#Ex6.5
#based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r).
#As a base case, we can use gcd(a, 0) = a.
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)


print(GCD(8,4))
