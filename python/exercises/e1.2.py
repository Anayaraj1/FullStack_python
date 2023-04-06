# 3)mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# mystr= "Ria Institue of Technology"
# 1)write a python program to evaluate below list
# a)Add the items in list 
# b)Find the length of the list
# c)sort the elements from the list
# d)reverse the list
# e)Count the duplicates elements from the list 3,2
# g)print "Institue" using slicing
# h)print "Institue" using negative index
# i)print "Ria Institue of"
# # j)print "Rs"

# # list part
# mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# mylist.sort()
# print(mylist)
# mylist.append(12)
# mylist.append(14)
# print(mylist)
# mylist.sort()
# print(mylist)
# print(len(mylist))  
# mylist.reverse()
# print(mylist)
# mylist=mylist.count(3)
# print(mylist)

# # string part
# mystr= "Ria Institue of Technology"
# print(mystr[4:12])
# print(mystr[-22:-14])
# print(mystr[0:15])
# print(mystr[1::2])
# print(mystr[-30:-19])

# 3)List Slicing 
# write a python program to slice the mylist
# a)print elements [1,2,3] using slicing concept
# b)print elements [9,0,122,10,2,3] 
# c)print elements [8,1,2,3,9,0,122,10,2,3,4,3,3,2] 
# d)print elements [10,2,3,4,3,3,2]
# e)print elements [10,3,3,2]
# f)print elements [6,8,2,9]
# g)print elements [1,0,3,2]

# using negative slice 
# e)print elements [10,3,3,2]
# f)print elements [6,8,2,9]
# g)print elements [1,0,3,2]
# h)print elements [1,2,3,9,0,122]

# 1)mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# mystr= "Ria Institue of Technology"
# 1)write a python program to evaluate below list
# a)Add the items in list 
# b)Find the length of the list
# c)sort the elements from the list
# d)reverse the list
# e)Count the duplicates elements from the list (3,2)
# g)print "Institue" using slicing
# h)print "Institue" using negative index
# i)print "Ria Institue of"
# j)print "Rs"

mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mylist.append(20)
print(mylist)
print(len(mylist))
mylist.sort()
print(mylist)
# mylist.reverse()
# print(mylist)
print(mylist[::-1])
print(mylist.count(3))
print(mylist.count(2))

mystr= "Ria Institue of Technology"
print(mystr[4:12])
print(mystr[-22:-14])
print(mystr[0:15])
print(mystr[0:7:6])


# 2)write a python program to evaluate below String
 # a)Add the string " Marathhalli "  and print the new string
 # b)Find the length of the string and reverse it
mystr=mystr+"marathalli"
print(mystr)
print(len(mystr))  
print(mystr[::-1])  


# 3)List Slicing 
# write a python program to slice the mylist
# a)print elements [1,2,3] using slicing concept
# b)print elements [9,0,122,10,2,3] 
# c)print elements [8,1,2,3,9,0,122,10,2,3,4,3,3,2] 
# d)print elements [10,2,3,4,3,3,2]
# e)print elements [10,3,3,2]
# f)print elements [6,8,2,9]
# g)print elements [1,0,3,2]

# using negative slice 
# e)print elements [10,3,3,2]
# f)print elements [6,8,2,9]
# g)print elements [1,0,3,2]
# h)print elements [1,2,3,9,0,122]
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]

print(mylist[6:9])
print(mylist[9:15])
print(mylist[5:])
print(mylist[12:])
print(mylist[12::2])
print(mylist[3:10:2])
print(mylist[6::4])

print(mylist[-7::2])
print(mylist[-16:-9:2])
print(mylist[-13::4])
print(mylist[-13:-7])
