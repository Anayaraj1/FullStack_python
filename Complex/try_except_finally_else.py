# try:
#     pass #run the code whem there is no error
# except:
#     pass #execute when try block fails
# else:
#     pass #executes when try block has no error and except block is not used
# finally:
#     pass # i dont care about try except and else i am going to execute complusory

def Divide(a,b):

    try:
        # print("i am try if no error i will execute")
        print("divide res",a/b)

    except Exception as e:
        print("exception was ",e)

    else:
        print("i am else block")
    finally:
        print(" i am finally block ", num1+num2)


num1=int(input("Enter the numerstor value\n"))
num2=int(input('Enter your denomenator value\n'))

Divide(num1,num2)