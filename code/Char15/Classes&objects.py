from math import sqrt


class Point:
    """Represents a point in 2-D space.
        attributes: x, y"""

def print_point(p):
    print('(%g,%g)' % (p.x,p.y))


def distance_between_points(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    distance = sqrt(dx**2 + dy**2)
    print(distance)
    return distance

def point_solution():
    point1 = Point()
    point1.x = 3.0
    point1.y = 4.0

    point2 = Point()
    point2.x = 6.0
    point2.y = 7.0

    print('point1 is: ')
    print_point(point1)
    print('point1 is: ')
    print_point(point2)

    print('distance between p1 and p2 is: ')
    distance_between_points(point1, point2)

point_solution()



class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

box1 = Rectangle()
box1.width = 100.0
box1.height = 200.0
box1.corner = Point()
box1.corner.x = 0.0
box1.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box1)
print('center of box1 is: ')
print_point(center)

def grow_rectangular(rect,dw,dh):
    rect.width += dw
    rect.height += dh

box2 = Rectangle()
box2.width = 150.0
box2.height = 300.0
box2.corner = Point()
box2.corner.x = 0.0
box2.corner.y = 0.0

grow_rectangular(box2,50,100)
print('growed box2 is:\n',box2.width,box2.height)


def move_rectangular(ract,dx,dy):
    ract.corner.x += dx
    ract.corner.y += dy

move_rectangular(box2,10,20)
print('moved box2 is: ')
print_point(box2.corner)

import copy

def move_rectangular_deepcopy(ract,dx,dy):
    new_ract = copy.deepcopy(ract)
    new_ract.corner.x += dx
    new_ract.corner.y += dy
    return new_ract.corner.x,new_ract.corner.y


print('the original box2 is at: (%g,%g)' % (box2.corner.x,box2.corner.y))
print('the new box is at: ',move_rectangular_deepcopy(box2,100,100))


#Exercises
print('[Exercise]','-'*70)
print('[Ex15.1]','-'*70)
class Circle:
    """Represents a Circle.

        attributes: center, radius.
        """

c1 = Circle()
c1.radius = 75
c1.center = Point()
c1.center.x = 150
c1.center.y = 100

def point_in_circle(cir,point):
    d = distance_between_points(cir.center,point)
    return d <= cir.radius

def rect_in_circle(cir,rect):
    p = copy.copy(rect.corner)
    if not point_in_circle(cir,p):
        return False

    p.x += rect.width
    if not point_in_circle(cir, p):
        return False

    p.x -= rect.width
    if not point_in_circle(cir, p):
        return False

    p.y -= rect.height
    if not point_in_circle(cir, p):
        return False

    p.y -= rect.height
    if not point_in_circle(cir, p):
        return False

    return True

def rect_circle_overlap(cir,rect):
    p = copy.copy(rect.corner)
    if point_in_circle(cir, p):
        return True

    p.x += rect.width
    if point_in_circle(cir, p):
        return True

    p.x -= rect.width
    if point_in_circle(cir, p):
        return True

    p.y -= rect.height
    if point_in_circle(cir, p):
        return True

    p.y -= rect.height
    if point_in_circle(cir, p):
        return True

    return False

import turtle
from Char4 import polygon

def draw_rect(t,rect):
    t.pu()
    t.goto(rect.corner.x,rect.corner.y)
    t.pd()
    t.lt(90)
    for length in rect.width,rect.height,rect.width,rect.height:
        t.fd(length)
        t.lt(90)


def draw_circle(t,cir):
    t.pu()
    t.goto(cir.center.x,cir.center.y)
    t.fd(cir.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t,cir.radius)

if __name__ == '__main__':
    bob = turtle.Turtle()

    face = Circle()
    face.center = Point()
    face.center.x = 0
    face.center.y = 0
    face.radius = 100
    draw_circle(bob,face)

    eye1 = Circle()
    eye1.center = Point()
    eye1.center.x = -25
    eye1.center.y = 25
    eye1.radius = 25
    draw_circle(bob, eye1)

    eye2 = Circle()
    eye2.center = Point()
    eye2.center.x = 25
    eye2.center.y = 25
    eye2.radius = 25
    draw_circle(bob, eye2)

    mouth = Rectangle()
    mouth.width = 80
    mouth.height = 40
    mouth.corner = Point()
    mouth.corner.x = -40
    mouth.corner.y = -60
    draw_rect(bob,mouth)

    # wait for the user to close the window
    turtle.mainloop()

