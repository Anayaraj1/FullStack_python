def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

returnval=factorial(5)
print(returnval)


# def factorial(5):
#     if 5==1 or 5==0: #false
#         return 1
#     return 5*factorial(5-1)
#     return 5*factorial(4)
# returnval = factorial(5)

# def factorial(4):
#     if 4==1 or 4==0:
#         return 1
#     return 4*factorial(4-1)
#     return 4*factorial(3)
# returnval = factorial(4)

# def factorial(3):
#     if 3==1 or 3==0:
#         return 1
#     return 3*factorial(3-1)
#     return 3*factorial(2)
# returnval=factorial(3)

# def factorial(2):
#     if 2==1 or 1==0:
#         return 1
#     return 2*factorial(2-1)
#     return 2*factorial(1)
# returnval=factorial(2)

# def factorial(1):
#     if 1==1 or 1==0:
#         return 1
#     return 1*factorial(1-1)
#     return 1*factorial(0)
# returnval=factorial(1)

# print(120)