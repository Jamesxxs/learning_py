#Char3

import math
print(type(__name__))
print(__name__)
if __name__ == '__main__':
    print('done!')


# Ex3.2/p49
def do_twice(func,value):
    func(value)
    func(value)

def print_spam():
    print('spam')

def print_twice(text):
    print(text)
    print(text)

#do_twice(print_twice,'spam')

def do_four(func,value):
    do_twice(func,value)
    do_twice(func,value)

#do_four(print,'spamm')


#Ex3.3

def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)


def print_hor():
    print('+', '-', '-','-','-' ,'+' ,'-','-','-','-' ,'+')

def print_ver():
    print('|','       ','|','       ','|')

def print_grid():
    print_hor()
    do_four(print_ver)
    print_hor()
    do_four(print_ver)
    print_hor()

print_grid()


#######################################################################################################################
#Char4
import turtle


bob = turtle.Turtle()

#4.3 Exercises (p53)
#1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def run(t):
    square(t)
    turtle.mainloop()

#run(bob)

#2
def square2(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def run2(t,length):
    square2(t,length)
    turtle.mainloop()

#run2(bob,200)

#3
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def run3(t,length,n):
    polygon(t,length,n)
    turtle.mainloop()

#run3(bob,100,3)

#4
import math

# circumference = 2*pi*r = legnth*n
# n = (2*pi*r)/length
# let length be 1
def circle(t,r):
    length = 1
    n = (2*math.pi*r)/length
    polygon(t, length, int(n))

def run4(t,r):
    circle(t,r)
    turtle.mainloop()

#run4(bob,100)

#5
def arc(t,r,angle):
   arc_length = (angle/360) * 2*math.pi*r
   step_length = 1
   n = int(arc_length/step_length)
   step_angele = angle/n
   for i in range(n):
       t.fd(step_length)
       t.lt(step_angele)

def run5(t,r,angle):
    arc(t,r,angle)
    turtle.mainloop()

#run5(t=bob,r=50,angle=60)

# and then we can rewrite 'circle' use 'arc'
def circle1(t,r):
    arc(t,r,360)




def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


# draw a sequence of three flowers, as shown in the book.
def runFlowers():
    move(bob, -100)
    flower(bob, 7, 60.0, 60.0)
    move(bob, 100)
    flower(bob, 10, 40.0, 80.0)
    move(bob, 100)
    flower(bob, 20, 140.0, 20.0)
    bob.hideturtle()
    turtle.mainloop()

#runFlowers()

def pie(t,n,length):
    for i in range(n):
        t.fd(length)
        t.lt(90+(360/(2*n)))
        t.fd((math.sin(math.pi/(n))*length*2))
        t.lt(90+(360/(2*n)))
        t.fd(length)
        t.lt(180)

def runPie(t,n,length):
    pie(t,n.length)
    turtle.mainloop()

#runPie(bob,7,50)


def spiral(t,r,n):
    for i in range(n):
        arc(t,r+10*i,180)

#spiral(bob,10,20)









def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)
koch(bob,100)
turtle.mainloop()