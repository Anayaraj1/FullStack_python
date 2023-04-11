#method overriding
class Employee:
    def printDetails(self):
        print("i am a class Details")
    
class Student(Employee):
    def printDetails(self):
        print("i am a class student")

class Child(Student):
    def printDetails(self):
        print("i am a class of child")


obj1=Student()
obj1.printDetails()
obj2=Student()
obj2.printDetails()
obj3=Child()
obj3.printDetails()