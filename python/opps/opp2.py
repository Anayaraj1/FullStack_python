class Student():
    schoolName="Ria School"
    location="Marathgalli"
    nam="student Name"

stud1=Student()
print(stud1.location)
print(stud1.schoolName)
stud1.nam="rohan"
print(stud1.nam)
print(stud1)


std2=Student()
print(std2.location)
print(std2.schoolName)
print(std2.nam)
std2.hobbies=["Eating","Sleeping"]
std2.isMale=True
std2.marks={
    "English":68,
    "Maths":78
}

std2.subject={"Engligh","Maths"}
std2.attendance=(1,2,3,4)

print(Student.location)
print(std2.__dict__)
print(stud1.__dict__)
print(Student.__dict__)

std3=Student()
print(std3.__dict__)