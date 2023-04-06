from functools import reduce
mydata=[10,20,30,40,50]
res=reduce(lambda x,y:x*y,mydata)
# res=reduce(lambda 10,20:10*20,mydata)
# res=reduce(lambda 200,3:200*3,mydata)
print(res)