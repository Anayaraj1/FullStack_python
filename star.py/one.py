# for i in range(6):
#     for j in range(6):
#         print("#",end=" ")
#     print("")

# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 

# num=int(input("Enter the num of rows"))

# for i in range(num):
#     for j in range(i+1):
#         print("^", end=" ")

#     print()
# ^ 
# ^ ^ 
# ^ ^ ^ 
# ^ ^ ^ ^ 
# ^ ^ ^ ^ ^ 
# ^ ^ ^ ^ ^ ^ 

# num=int(input("Enter the no of rows "))
# for i in range(num):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# for i in range(8):
#     for j in range(8-i):
#         print("A",end=" ")
#     print()

    
# A A A A A A A A 
# A A A A A A A 
# A A A A A A 
# A A A A A 
# A A A A 
# A A A 
# A A 
# A 


num=int(input("Enter The num of rows "))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("A",end=" ")
    k=k+2
    print()


