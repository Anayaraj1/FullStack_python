n=int(input("Enter the num"))
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(n):
    for j in range(2*n):
        print("",end=" ")
    # for j in range(n):
    #     print("#",end="")
    for j in range(2*n):
        print("#",end="")
    print("")

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("@",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    print()

