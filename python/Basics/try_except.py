num1=int(input("Enter the number1\n"))
num2=int(input("Enter the number2\n"))
try:
    # print("i am a try if no error i will execute")
    print("divide res",num1/num2)

except Exception as e:
    pass
    print("Exception was ",e)    
    # print("i will execute only if there is a exception")