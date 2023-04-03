# def greeting():
#     print("Good Morning Ria")

# greeting()

# def greeting(name):
#     print("Gud Mrng Ria",name)

# greeting("Annes")
# greeting("Anaya")

# def greeting(name="annes"):
#     print("good mrng",name)

# greeting()
# greeting("anaya")


# def greeting(name="gobin",salary=15000):
#     print("good mrng",name,"\n salary credited",salary)

# greeting()
# greeting("anaya",50000)

# def greeting(name,salary):
#     print("good mrng",name,"\n your salary is credited",salary)

# greeting()
# greeting("anaya",9092347)


# a=20  #global variable
# b=60
# def sum(a,b):
#     a=40 #local variable
#     b=60
#     print(a+b)


# sum(a,b)


# mylistsal=[]

# def employee(name,salary):
#     print(f"\nEmployee {name}\n salary credited\n{salary}")
#     bonus=10000
#     mylistsal.append(salary+bonus)
#     return salary+10000
# # employee("anaya",56789)

# Annessal=employee("annes",400000)
# gobinsal=employee("Gobin",857558)
# anayasal=employee("anaya",50000)
# print("\n")
# print(Annessal,gobinsal,anayasal)
# print((Annessal+gobinsal+anayasal)/3)
# print(mylistsal)

 # 1)write a 4 functions
# a)to find the area of circle
# b) to find the area of rectangle
# c)to find the area of square
# d)find the area of triangle
# use return statements and print it 
# for taking the inputs use input()

# area of circle

import math
def area_of_circle(Radius):
    area=Radius**math.pi
    return area

Radius = float(input("Please enter your radius: "))
print("The area of circle is:",area_of_circle(Radius))

def area_of_rectangle(w,h):
    area=w*h
    return area
w=float(input("Enter w :"))
h=float(input("Enter h :"))
print("The area of Rectangle is :",area_of_rectangle(w,h))


def area_of_sqare(r):
    area=r*r
    return area

r=float(input("Enter the value of r: "))
print("Area of square is :",area_of_sqare(r))
