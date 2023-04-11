# for row in range(6):
#     for col in range(7):
#         if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("^",end="")
#         else:
#             print(end=" ")
#     print()

#  ^^ ^^ 
# ^  ^  ^
# ^     ^
#  ^   ^ 
#   ^ ^  
#    ^  

# num=int(input("Enter the num of rows"))
# k=1
# for i in range(1,num+1):
#     for j in range(1,k+1):
#         print("1",end=" ")
#     k=k+2
#     print()

# 1 
# 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 1 1 1 


num=int(input("Enter the num of rows:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("^",end=" ")
    print()