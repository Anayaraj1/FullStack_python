# constructors - it is a init method inside a class which is going to call whenever the object is created and set the values for the varaibles for specific object


class Employee:
    company="Infosis"

    def __init__(self,name,role,age,salary):
        print("i am a constructor i am gonna set the values")
        self.name=name
        self.role=role
        self.age=age
        self.salary=salary
        print("i have set the values to specific object")

    def companyDetails(self):
        print(f'Employee name is {self.name}\nEmployee role is {self.role}\nEmployee age is {self.role}\nEmployee salary is {self.salary}')


class Student:
    institute="ria"


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def studentDetails(self):
        print(f'student name is {self.name}\nstudent age is {self.age}')


emp1=Employee("rohan","front-end",23,40000)
emp1.companyDetails()
emp2=Employee("Anaya","Data Science",23,60000)
emp2.companyDetails()

stud1=Student("Anaya",23)
stud1.studentDetails()