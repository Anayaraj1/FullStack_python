# fruits=["apple","orange","banana","grapes"]
# seprator="@"
# res=seprator.join(fruits)
# print(res)
# print(type(res))

# fruits=["apple","orange","banana","grapes"]
# sperator="#"
# res=sperator.join(fruits)
# print(res)
# print(type(res))

# fruits=["apple","orange","banana","grapes"]
# sperator="/"
# res=sperator.join(fruits)
# print(res)
# print(type(res))


mydict={"employeeName":"Anaya","employeeSalary":2000,"isActice":True}
sperator="ria"
newmyDict=sperator.join(mydict.keys())
print(newmyDict)

print("********")
mylist=[]
fName=input("Enter your FirstName \n")
lName=input("Enter Your lastName \n")
mylist.append(fName)
mylist.append(lName)
name="".join(mylist)
mylist.clear()
mylist.append(name)
mylist.append("")
sep="@gmail.com"
print(mylist)
print(sep.join(mylist))