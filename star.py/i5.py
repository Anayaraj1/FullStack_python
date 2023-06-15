n = int(input("Enter num"))

# for i in range(n//2+2):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i+1):
#         print("@", end="")
#     print()
# for i in range(n):
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     for j in range(n):
#         if (i == n//2):
#             print("@", end="")
#         else:
#             print(" ", end="")
#     for j in range(n//2+1):
#         if (j >= n//2-i and j >= i-n//2):
#             print("*", end="")
#     print()
#    @
#   @@@
#  @@@@@
#  *   *
# **@@@**
#  *   *

# *       *
# **     **
# ***@@@***
#    @@@
#    @@@
#    ***
#     *

# n = int(input())
# x = (n + n + n) - 2
# for i in range(1, n + 1):
#     for j in range(i):
#         print('*', end='')
#     if (i == n):
#         for _ in range(x):
#             print('@', end='')
#         x -= 2
#     else:
#         for _ in range(x):
#             print(end=' ')
#         x -= 2
#     for _ in range(i):
#         print('*', end='')
#     print()
# for _ in range(1, n):
#     for _ in range(n):
#         print(end=' ')
#     for _ in range(n):
#         print('@', end='')
#     print()
# x = n
# k = n
# for l in range(x, 0, -1):
#     for _ in range(k):
#         print(end=' ')
#     k += 1
#     x1 = x
#     for _ in range(x1):
#         print('*', end='')
#     x1 -= 2
#     x -= 2
#     print()
# *       *
# **     **
# ***@@@***
#    @@@
#    @@@
#    ***
#     *

# x = (n+n+n)-2
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for j in range(n):
        if (i == n):
            print("@", end="")
    print()

for i in range(1, n):
    for j in range(n):
        print(" ", end="")
    for j in range(1, n+1):
        print("@", end="")
    print()
for i in range(n//2+2):
    for j in range(n):
        print(" ", end="")
    for j in range(i):
        print(" ", end="")
    for j in range(n, 2*i, -1):
        print("*", end="")
    print()
