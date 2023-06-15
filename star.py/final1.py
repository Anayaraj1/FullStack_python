n = int(input("Enter num"))
# for i in range(n+1):
#     for j in range(4*n-1):
#         print(end=" ")
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("@", end="")
#     print()
# for i in range(n):
#     for j in range(n):
#         print("", end=" ")
#     for j in range(n):
#         print("#", end="")
#     for j in range(2*n):
#         print("#", end="")
#     print()
for i in range(n//2+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("@", end="")
    print()


# def numinput():
#     n = int(input("Number of lines 'only odd number' :: "))
#     if (n % 2 != 0 and n > 2):
#         diode(n)
#     else:
#         print(":: Only odd numbers and not 1 ::")
#         numinput()


# print()


# def diode(n):
#     print()
#     for i in range(1, n+3):
#         for j in range(1, 5*(n+2)//2):
#             if i <= n//2+2 and j <= i or i > 1 and i < n+2 and j >= 3*(n//2+2) or i > n//2+2 and j <= 2*(n//2+2)-i:
#                 print("@", end="")
#             elif i == n//2+2 and j > i and j < i*3:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print()
#     numinput()


# print()
# print("It's a symbol like a diode.")
# print()
# numinput()
