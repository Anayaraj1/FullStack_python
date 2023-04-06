# int a=12;
# if(a>20){
#     system.out.println("yes bro")
#     system.out.println("go ahead")
#     int x=20
#     sysytem.out.println(x)
# }

# system.out.println("go ahead now")

# x=25
# y=40
# if(x>y):
#     print("im a inside if block")
#     print("x is greater than y")
#     print("output of x and y ", x+y)


# print("i am outside of if block ")

# x=25
# y=40
# if(x>y):
#     print("i am inside the if block")
#     print("x is < than y ",x+y)
# else:
#     print("i am outside else block ")
#     print(" x is not > than y")
#     print("output of x and y ",x+y)

# print(" i am out side of if else block")

# x=25
# y=50
# if(x<y):
#     print("i am inside if block")
#     print("x is < then y")
#     print("outside of x and y",x+y)
#     if(12>5):
#         print("i am nested if")
#         if(10>20):
#             print("i am also nested if")
#         else:
#             print("  i am else nested esle of first")
#     else:
#         print("i am nested else of first")
# else:
#     print(" i am outside else block")
#     print(" x is not > than y")
#     print("output of x and y",x+y)

# print(" i am out side of nested if else block")

age=int(input("enter your age:\n"))
if(age<18):
    print("you cannot vote")
elif(age==18 or age==19):
    print("if you have voter id you can vote")

elif(age>18 and age<=85):
    print(" you can vote")

else:
    print("Enjoy your last days")