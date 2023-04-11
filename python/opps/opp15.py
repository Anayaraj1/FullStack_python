# operator overloading and dunder methods in python

class Employee:
    no_of_leaves=14

    def __init__(self,name,salary,age,role,phone):
        self.name=name
        self.salary=salary
        self.age=age
        self.role=role
        self.phone=phone

    def printDetails(self):
        print(f"Employee name is {self.name}\nEmployee salary is {self.salary}\nEmployee age is {self.age}\nEmployee phone is {self.phone}")

    @classmethod
    def change_of_leaves(cls,n):
        cls.no_of_leaves=n

    def __add__(emp1,emp2):
        return emp1.salary+emp2.salary
    
    def __sub__(emp1,emp2):
        return emp1.salary-emp2.salary

    def __mul__(emp1,emp2):
        return emp1.salary*emp2
    
    
    def __truediv__(self,other):
        return self.phone/other.phone

    def __floordiv__(self,other):
        return self.phone//other.phone
    
    # def __str__(self):
        # return f"STR: Employee Name is {self.name}\nSalary {self.salary}\nRole {self.role}\nPhone Number is {self.phone}\n No of Leave {self.no_of_leaves} "

    def __repr__(self):
        return f"Repr: Employee Name is {self.name}\nSalary {self.salary}\nRole {self.role}\nPhone Number is {self.phone} No of Leave {self.no_of_leaves}"

    @staticmethod
    def Company():
        print("i am accenture")

emp1=Employee("Anaya",80000,21,"data analyst",8665)
emp2=Employee("farhan",7544444,21,"Businnes",896346)
print(emp1+emp2)
print(emp1/emp2)
print(emp1//emp2)
print(emp1)
print(emp2)

print(emp2.no_of_leaves)
print(emp2.printDetails())
emp1.Company()

emp2.change_of_leaves(80)
print(emp2)