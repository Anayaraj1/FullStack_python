# n = int(input("Enter the num"))
# print("*"*n)

# n = int(input("Enter the num"))
# for i in range(n):
#     for j in range(n*2):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# for i in range(n):
#     for j in range(i, n):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end="")
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print("\r")
#     for i in range(n):
#         for j in range(i, n):
#             print("*", end=" ")
#         print("\r")


# n = int(input("Enter a number: "))  # Assuming the user inputs 6

# # Upper half of the pattern
# for i in range(0, n - 2):
#     print(" " * (n - i), "@" * i)

# # Lower half of the pattern
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), "@" * i)

# # Additional pattern lines
# # print(" " * (n - 1), "*" * 12)
# # print(" " * (n - 1), "*" * 12)
# # print(" " * (n - 1), "*" * 12)
# # print(" " * (n - 1), " " * 3, "@")
# # print(" " * (n - 1), "@")

# # # Additional pattern lines (descending)
# # for i in range(1, n + 1):
# #     print(" " * (n - i), "@" * i)

# # Final line of the pattern
# print(" " * n, "@")


# most important

n = int(input("enter"))
# # print()
# for i in range(n):
#     for j in range(2*n-2):
#         print("", end=" ")
#     for j in range(2*n):
#         print("#", end="")
#     print("")

for i in range(n+1):
    print("=")
    # print(" "*(n-i), "@"*(n-(i+1)))
    # print(" " * (n - i), "@" * i)
