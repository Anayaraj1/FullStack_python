mydict={
    "name":"rohan",
    "age":20,
    "phone":78654324,
    "salary":679.87
}

mylist=[1,2,3,4,5,6,7,8,9,10]

def KeywordArgsFunction(greet,*args,**kwargs):
    print(kwargs)
    for i in args:
        print(i)

    for k,v in kwargs.items():
        print("key is ",k,"value is", v)

    print(greet,"good morning")

KeywordArgsFunction("ark",mylist,mydict)