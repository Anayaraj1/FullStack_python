# 1)Take a inputs and Evaluate the expressions
# a)Take the Students name
# b)Take the student english marks
# maths,science,social,kannada,hindi
# c)add the total marks 
# d)print average
# e)add languages marks (english,kannada,hindi)and print average
# f)add the core subjects (maths,science and social)and print average

Name=input("Enter Student Name:")
print("Student Name :",Name)
English_Marks=int(input("Enter your English marks:"))
Maths_Marks=int(input("Enter your Maths marks:"))
Science_Marks=int(input("Enter your Science marks:"))
Social_Marks=int(input("Enter your Social marks:"))
Kannada_Marks=int(input("Enter your Kannada marks:"))
Hindi_Marks=int(input("Enter your Hindi marks:"))

Marks=English_Marks+Maths_Marks+Science_Marks+Science_Marks+Kannada_Marks+Hindi_Marks
print("Total Marks :",Marks)
print("Average Marks for each subject:",Marks/6)
core_subject=Maths_Marks+Social_Marks+Science_Marks
print("Addition of Core Subject:",core_subject)
print("Average of core subjects:",core_subject/3)

# 2)create a list mylist  ``  `
# add "apple","banana","orange","mosambi"
# a)append "pineapple"
# b)remove "orange" and find the length of list
# c)print "banana, mosambi, pineapple"
# d)add new list to the existing [1,2,3,4]
# e)print only [1,2,3,4] and reverse [4,3,2,1]----*--+

mylist=["apple","orange","banana","mosambi"]
mylist.append("pineapple")
print(mylist)
print("Length of mylist:",len(mylist))
print(mylist[2:])
mylist=mylist+[1,2,3,4]
print(mylist)
print(mylist[5:],"Reverse:",mylist[8:4:-1])
