#7.1 Reassignment

#7.2 Updating variable

#7.3 the 'While' statement
def print_n(s,n):
    while n>0:
        print(s)
        n = n-1

#print_n('hh',8)

#7.4 Break
def use_break():
    while True:
        line = input('>')
        if line=='done':
            break
        print(line)
    print('Finished!')

#use_break()

#7.5 Square roots

#Exercise 7.9
#Ex7.1
import math
from prettytable import PrettyTable

def mysqrt(a,x):
    while True:
        print(x)
        y = (x+a/x)/2
        if y == x:
            return y
        x = y

def test_square_root():
    field_names = ("a", 'mysqrt(a)', 'math.sqrt(a)', 'diff')
    table = PrettyTable(field_names=field_names)
    for a in range(1,10):
        myfuc = mysqrt(a,5) #5 is a random chosen number
        mathfuc= math.sqrt(a)
        diff = abs(myfuc-mathfuc)
        table.add_row([a,myfuc,mathfuc,diff])
    print(table)

#test_square_root()

#Ex7.2
def eval_loop():
    while True:
        string = input('>>')
        if string=='done':
            print('done!')
            break
        print(eval(string))

#eval_loop()


#Ex7.3
def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
    return result

def estimate_pi():
    e = 1e-15
    c = (2*math.sqrt(2))/9801
    k = 0
    total = 0
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = c * num / den
        total += term
        mpi = 1/total
        if abs(mpi - math.pi) < e:
            break

        k += 1
    return mpi

print(estimate_pi())