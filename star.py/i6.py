n = int(input("Enter Number"))
for i in range(n//2+1):
    for j in range(n//2):
        print(end=" ")
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(n):
        print(" ", end="")
    for j in range(n):
        if (j == 0 or j == n-1):
            print("@", end="")
        else:
            print(" ", end="")
    print()
# for i in range(n//2+1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n, 2*i, -1):
#         print("*", end="")
#     print()
