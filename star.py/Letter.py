# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

# for row in range(7):
#     for col in range(5):
#         if (col==0 ) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# ****
# *   *
# *   *
# ****
# *   *
# *   *
# ****

n = int(input("Enter"))
k = 2
for i in range(1, n+1):
    print("*")
    for j in range(0, n-3):
        # if ((j >= 0 and j <= 6) or (j >= 1 and j <= 5) or (j >= 2 and j <= 4) or (j >= 3)):
        print("*", end="")
print()


#     for j in range(n+1):
#         if ((j >= 0 and j <= 6) or (j >= 1 and j <= 5) or (j >= 2 and j <= 4) or (j >= 3)):
#             print("*", end="")
#         else:
#             print(" ")
