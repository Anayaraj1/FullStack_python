# 1)
# 1. Write a program to print the odd numbers from 1 to 100
# 2. Write a program to print the even numbers from 1 to 100
# 3. Write a program to print {20,40,60,80,100} using for loop

print("Even number between 1 to 100")
for i in range(0,101,2):
    print(i)

print("odd number between 1 to 100")
for i in range(1,100,2):
    print(i)

for i in range(20,120,20):
    print(i)

# 2. Using while loop 
# a)print the number 1 to 10
# b)print the numbers 1 to 100  and it should print only even numbers
# c)print the numbers 1 to 100 and should print only odd numbers
#  and it should break the loop when value becomes 51
# d)print the numbers 1 to 100 and should print 100 and skip 55 using continue

#a
# print("print between 1 to 10 using while loop")
# i=1
# while(i<=10):
#     print(i)
#     i=i+1

# # #b
# print("Even number between 1 to 100 in while loop")
# i=0
# while(i<100):
#     i=i+2
#     print(i)

# #c
# print("odd number between 1 to 100 in while loop")
# i=1
# while(i<99):
#     i=i+2
#     print(i)
#     if(i==51):
#         break
# # d 
# print("print the numbers 1 to 100 and should print 100 and skip 55 using continue")
# i=0
# while(i<100):
#     i=i+1
#     if(i==55):
#         continue
#     print(i)

#  2)
#  Write a program to print the tables from 1 to 10
# take a input from user.

# 2 x 1= 2
# ..
# ..
# 2 x 10 =20

# num =2

# print(int(input("Multiple of :")))

# for i in range(1,11):
#     print(num , "x" ,i,"=",num*i)

# question no 3)
# write square root of 1 to

# for i in range(1,11):
#     print(i*1)



# 4. Write a program to validate a person can vote or not
# *take the age as input from the user
# if age is less than 18 print he cannot vote
# if age is greater than 18 print he can vote
# if age is greater than 90 print please stay at home
# if age is 18 than  print please make the voter id

# age=int(input("Enter your Age :"))

# if(age<18):
#     print("You cannot vote after 18 you can vote understand")

# elif(age==18 or age==19):
#     print("if you have voter id you can vote")

# elif(age>18 and age<=85):
#     print("you can vote")

# else:
#     print("Enjoy your last day")