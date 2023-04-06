# 1) write a program to take a input from the user and print the details
#    *Employee Name
#    *Employee Age
#    *Employee Phone Number\
#    *EMployee Address
# along with this print the type of all the variables

x=input("Enter Employee Name:")
x1=int(input("Enter Employee Age:"))
x2=int(input("Enter Phone Number:"))
x3=input("Enter EMployee Adress:")

print(type(x),x)
print(type(x1),x1)
print(type(x2),x2)
print(type(x3),x3)


# 2)write a program to take a input from the user and print the details
#   *Student Name 
#   *Student maths marks
#   *Student science marks

# ->print student name in Upper case
# ->add students marks (math+science) then print the total marks
# ->then find the average of two subjects

x=input("Enter yor Name:")
x1=int(input("Enter Maths Marks"))
x2=int(input("Enter Science Marks"))
x3=x1+x2

print("Student Name:",x.upper())
print("Maths Marks:",x1)
print("Science Marks:",x2)
print("Total Marks:",x3)
print("Average of Two Subject:",x3/2)