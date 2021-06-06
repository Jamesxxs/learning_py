####################################################################################################
#Floor division'//'
minutes = 105
hour = minutes//60
print('hour: ',hour)

reminder = minutes - hour*60
print('minutes: ',reminder)

#modulus operator '%'
reminder = minutes%60
print('reminder: ',reminder)

print(3.5//0.6)

#Relation operators '==,!=,>,<,>=,<='

#Logical operators 'and,or,not'
#In Python any nonzero number is interpreted as 'True'

####################################################################################################
#Conditional execution
x = 1

if x<0:
    pass    # TODO: need to handle negative values!

#Alternative execution
if x%2==0:
    print('x is even')
else:
    print('x is odd')

#Chained conditionals 'elif'

#Nested conditionals (It is a good idea to avoid them when you can.)

#Recursion
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

#countdown(5)

def print_a(capital):
    if capital:
        print('A')
    else:
        print('a')

def do_n(f,n,value):
    if n<=0:
        print('finishied!')
    else:
        f(value)
        do_n(f,n-1,value)

#do_n(print_a,5,True)

#Keyboard input
'''question1 = input('what do u like to eat?\n')
print(question1)

question2 = int(input('how old r u?'))
print(question2)
'''

####################################################################################################
#5.14 Exercises
#1
import time
print(time.time())


def convertedTime(time):
    day = 60*60*24
    hour = 60*60
    minute = 60
    d = int(time // day)
    h = int((time-d*day) // hour)
    m = int((time-d*day-h*hour) // minute)
    s = int(time-d*day-h*hour-m*minute)
    print('now is ',d,' days',h,':',m,':',s,'from 1st Jan 1970')

#convertedTime(time.time())

#2
def check_fermat():
    a = int(input('a:'))
    b = int(input('b:'))
    c = int(input('c:'))
    n = int(input('d:'))
    if n <= 2:
        print('n needs to be greater that 2!')
        return
    elif a <=0 or b<=0 or c <=0:
        print('a,b and c must be positive ')

    elif a**n + b**n == c**n:
        print("Fermat's theorem is WRONG!")
    else:
        print("No,that doesn't work")

#check_fermat()

#3
def is_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print('Yes')
    else:
        print('No')

#is_triangle(1,1,12)

#4
def recurse(n,s):
    """print the value of s when n is 0"""
    if n == 0:
        print(s)
    else:
        recurse(n-1,n+s)

#recurse(-1,0)

#5
#The following exercises use the turtle module, described in Chapter 4: