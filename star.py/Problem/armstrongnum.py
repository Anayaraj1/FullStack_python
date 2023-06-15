# arm = int(input("enter"))
# for i in range(arm):
#     num = i
#     result = 0
#     n = len(str(i))
#     while (i != 0):
#         digit = i % 10
#         result = result+digit**n
#         i = i//10
#     if num == result:
#         print(num, "is a armstrong num")
#     else:
#         print(num, "It is not a armstrong num")


# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0
# length = len(str(num))
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** length
#     temp //= 10

# # display the result
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


# num = int(input("Enter your num"))
# sum = 0
# Value = num
# length_of_num = len(str(num))
# while (Value > 0):
#     digit = num % 10
#     sum = sum+digit**length_of_num
#     Value = Value//10
# if num == sum:
#     print(num, "It is armstrong num")
# else:
#     print(num, "It is not armstrong num")

n = int(input("Enter the num"))

# for i in range(n//2+1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n+1, 2*i, -1):
#         print("*", end="")
#     print()
