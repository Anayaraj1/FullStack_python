n = int(input("Enter the num"))
# for i in range(n//n+3):
#     for j in range(i):
#         print("@", end="")
#     print()
for i in range(n+1):
    for j in range(0, 3*n):
        print("", end=" ")
    # for j in range(n-i):
    #     print(" ", end="")
    for j in range(2*i+1):
        print("@", end="")
    print()
for i in range(n):
    for j in range(0, n):
        print("", end=" ")
    for j in range(2*n):
        print("*", end="")
    print()
for i in range(n//2+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("@", end="")
    print()


# second important

for i in range(n//2+1):
    for j in range(i):
        print(" ", end="")
    for j in range(n+2, 2*i+1, -1):
        print("@", end="")
    print()
