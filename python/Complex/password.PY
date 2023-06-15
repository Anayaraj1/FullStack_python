import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "0123456789"
symbols = "@#$%^&*?/"

user_for = lower_case+upper_case+number+symbols
length_for_pass = 8

password = "".join(random.sample(user_for, length_for_pass))
print("your generated password is", password)
