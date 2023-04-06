# Firstname=input("Enter Firstname")
# Lastname=input("Enter lastname")
# fullname=Firstname+Lastname
# print(fullname)
# sperator="@"
# Emailid=sperator.join(fullname)
# print(Emailid)

a=input("Enter your first name:")
b=input("Enter your last name:")
c="@gmail.com"
mylist=[a,b,c]
Emailid=c.join(mylist,c)
print(Emailid)

