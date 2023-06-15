# rows = 2
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         if (i == 0 or i == 1 or i == 2 or i == 3 or i == 4) or (j == 4 or i == 2):
#             print("*", end=' ')
#         else:
#             print(" ", end=" ")
#     print("\r")
#     for i in range(rows, 0, -1):
#         for j in range(0, i - 1):
#             print("*", end=' ')
#     print("")
# for i in range(4):
#     for j in range(4):
#         print("#", end=" ")
#     print("")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(3):
#     for j in range(3):
#         print("#", end=" ")
#     print("")
#  @
# @@@

for i in range(2):
    for j in range(2):
        if (i == 0 or j == 1) and (j != 0 or j != 1):
            print("@", end="")
    print()
for i in range(0, 2):
    for j in range(2):
        if (i == 0 or i == 1 or j == 0 or j == 1 or j == 2):
            print("@", end="")
    print()
