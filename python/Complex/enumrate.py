mylist=["manohar","bhanu","anaya","raj","abhishek"]

for i in mylist:
    print(i)

newList=enumerate(mylist,1)
print(type(newList))

# for i,j in mylist:
#     print(i,j)

# newList=list(newList)
# print(newList)
# print(type(newList))
# print(type(newList[0]))
# print(newList[4])

for i,j in enumerate(mylist,100):
    print(i,j)

mydict={
    "name":"ria institute",
    "established":2034,
    "course":["python","java"],
    "isActive":True
}

for i,j in enumerate(mydict.items(),100):
    print(i,j)