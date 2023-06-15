n = int(input("Enter num"))
for i in range(n+1):
    for j in range(n//2):
        print(end=" ")
    for j in range(n//2+1):
        if (j >= n//2-i and j >= i-n//2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n):
    for j in range(n):
        print(end=" ")
    for j in range(2*n):
        print("#", end="")
    print()
for i in range(n+1):
    for j in range(3*n):
        print(end=" ")
    for j in range(i):
        print(" ", end="")
    for j in range(n+1, 2*i, -1):
        print("@", end="")
    print()
