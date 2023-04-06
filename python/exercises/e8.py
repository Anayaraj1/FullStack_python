# 1. Calculate the multiplication and sum of two 
# numbers 
# Given two integer numbers return their product only if the product is equal to 
# or lower than 1000, else return their sum.

def multi_sum(num1,num2):
    product= num1 * num2
    if product <=1000:
        return product
    else:
         return num1 + num2
    
result= multi_sum(20,30)
print("The result is " ,result)

result= multi_sum(40,30)
print("The result is ", result)



# Exercise 2: Print the sum of the current number and 
# the previous number 
# Write a program to iterate the first 10 numbers and in each iteration, print the 
# sum of the current and previous number. 


print("Print the sum of the current number and the previous number :")

previous_num= 0

for i in range(1,11):
    sum=previous_num + i
    print("Current number ", i, "previous num" , previous_num,"=", "sum :", sum)

    previous_num = i


# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.