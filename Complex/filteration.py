# a=[1,2,3,4,5,6,7,8,9]
# b=[1,2,34,5,6,7,8,9]
# res=list(filter(lambda x:x in a,b))
# print(res)
data=[1,2,3,4,5,6]
def filteration(n):
    if n==2 or n==3 or n==4:
        pass
    else:
        return n
    
res=list(filter(lambda x:filteration(x),data))
print(res)