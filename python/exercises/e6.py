# 1)write a 4 functions
# a)to find the area of circle
# b) to find the area of rectangle
# c)to find the area of square
# d)find the area of triangle
# use return statements and print it 
# for taking the inputs use input()

import math
def area_of_circle(Radius):
    area= Radius**math.pi
    return area

Radius=float(input("Enter  your radius :"))
print("The area of circle:",area_of_circle(Radius))

def area_of_rectangle(w,h):
    area1 = w*h
    return area1

w =float(input("Enter w:"))
h = float(input("Enter h:"))
print("Area of Reactangle:",area_of_rectangle(w,h))

def area_of_square(r):
    area = r*r
    return area

r =float(input("Enter your radius:"))
print("Area of square :" ,area_of_square(r))

def area_of_triangle(b,h):
    area = float((b*h)/2)
    return area

b=float(input("Enter your b:"))
h=float(input("Enter your h:"))
print("Area of Triangle",area_of_triangle(b,h))