n = int(input("Enter the num"))
# for i in range(n//2+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()

# first print
# for i in range(1, n):
#     for j in range(0, 3*n):
#         print("", end=" ")
#     for j in range(1, i+1):
#         print("@", end="")
#     print()
# for i in range(n, 0, -1):
#     for j in range(0, 3*n):
#         print("", end=" ")
#     for j in range(1, i+1):
#         print("@", end='')
#     print()
# for i in range(n):
#     for j in range(0, n):
#         print("", end=" ")
#     for j in range(2*n):
#         print("*", end="")
#     print()
# for i in range(n//2+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# first print

# for i in range(n):
#     for j in range(2*n):
#         print("", end=" ")
#     # for j in range(n):
#     #     print("#",end="")
#     for j in range(2*n):
#         print("#", end="")
#     print("")

'''for i in range(n):
    for j in range(i, n):
        print("\b", end=" ")
    for j in range(i):
        print("\b @", end=" ")
    for j in range(i+1):
        print("\b @", end=" ")
    print()'''
'''n = int(input("Enter num"))
for i in range(1, n+2, 2):
    print(" "*(n-i), "@"*i)'''

# for i in range(n):
#     for j in range(i, n):
#         print("", end=" ")
#     for j in range(i):
#         print("@", end="")
#     for j in range(i+1):
#         print("@", end="")
#     print()

# for i in range(n):
#     for j in range(2*n):
#         print("*", end="")
#     print()

# for i in range(n//2+1):
#     for j in range(n-i):
#         print(" ")
#     for j in range(n, 2+i, 2):
#         print("@")
# print()

# mystr = "Hello World"
# mystr[8]
# print(mystr[8])

# for i in range(n//2+1):
#     for j in range(n,n-i)


# for i in range(n+1):
#     for j in range(0, 3*n):
#         print("", end=" ")
#     if (n-i < 0):
#         print(" ", end="")
#     # for j in range(n-i):
#     #     print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# for i in range(n+1):
#     for j in range(n-i):
#         print(" "*i)
#     print()

# for i in range(n//2+1):
#     for j in range(n//2-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# most important
# for i in range(n//2+1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n+2, 2*i+1, -1):
#         print("@", end="")
#     print()

# second
# for i in range(n//2+1):
#     for j in range(0, n+1):
#         print(" ", end=" ")
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n+2, 2*i+1, -1):
#         print("@", end="")
#     print()
# for i in range(n):
#     for j in range(0, n):
#         print("", end=" ")
#     for j in range(2*n):
#         print("#", end="")
#     print()
# for i in range(n//2+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i+1, -1):
#         print("@", end="")
#     print()

# for i in range(n+1):
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
for i in range(n+1):
    for j in range(n//2+1):
        if (j >= n//2-i and j >= i-n//2):
            print("*", end="")
    print()
