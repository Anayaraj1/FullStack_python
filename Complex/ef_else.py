mylist=["a","b","c","d","e","f"]
for i in mylist:
    print(i)
else:
    print("i am a else block of for loop")


items=["pizza","burger","frice"]

for j in items:
    if j=="chicken":
        print(j,"is tasty")
        break
    else:
        print("items not found")


items=["pizza","burger","idli","frice","dosa","sambhar"]

for j in items:
    if j=="idli":
        print(j,"is tasty")
        break

else:
    print("items not found")