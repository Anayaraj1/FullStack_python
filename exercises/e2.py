#  using positive slicing
'''
# Syntax mystr[start:end-1:step-size-1]
1)List Slicing mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
10is 11
write a python program to slice the mylist
a)print elements [1,2,3] using slicing concept
b)print elements [9,0,122,10,2,3] 
c)print elements [8,1,2,3,9,0,122,10,2,3,4,3,3,2] 
d)print elements [10,2,3,4,3,3,2]
e)print elements [10,3,3,2]
f)print elements [6,8,2,9]
g)print elements [1,0,3,2]
'''
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
print(mylist[6:9])
print(mylist[9:15])
print(mylist[5:])
print(mylist[12:])
print(mylist[12::4])
print(mylist[3:10:2])
print(mylist[6::4])

# using Negative slicing
# e)print elements [10,3,3,2]
# f)print elements [6,8,2,9]
# g)print elements [1,0,3,2]
# h)print elements [1,2,3,9,0,122]
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
print(mylist[-7::4])
print(mylist[-13::4])
print(mylist[-13:-7])