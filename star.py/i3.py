n = int(input("Enter The odd num only"))
# x = (n+n+n)-2
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    # for j in range(n-i-1):
    #     print(" ", end="")
    # for j in range(i+1):
    #     print("*", end="")
    for j in range(n):

        # for k in range(x):
        if (i == n):
            print("@", end=" ")
        else:
            print(" ", end=" ")
    print()

# for i in range(n):
#     for j in range(n):
#         print("@", end="")
#     print()
# for i in range(n//2+1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n, 2*i, -1):
#         print("*", end="")
#     print()
