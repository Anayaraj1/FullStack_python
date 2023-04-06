
# for i in range(100):
#         print(i)

# for i in range(10,101):
#         print(i)

# for i in range(1,1001,2):
#         print(i)

# for i in range(0,101,2):
#         print(i)

# for i in range(100,0,-2):
#         print(i)


# mylist =["grapes ","mango","orange","pineapple","grapes",1,2,3,4,5,True]

# for i in mylist[::2]:
#     print(i)

# for i in mylist[::1]:
#     print(i)

# print("\n")
# for i in mylist[1:7:3]:
#     print(i)

# for i in mylist:
#     pass
#     if i==2:
#         break
#     print(i)


# for i in mylist:
#     pass
#     if i==4 or i=="grapes":
#         continue
#     print(i)

userItem=input("Enter what ypu want :\n")
fruitMenu=["apples","mango","orange","pineapple","grapes"]

item=""
for i in fruitMenu:
    if i==userItem:
        item=i
        
