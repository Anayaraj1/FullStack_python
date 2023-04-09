class Employee:
    company="Infosis"

    def __init__(self,name,role,age,salary):
        print("i am constructor i am goona set the values")
        self.name=name
        self.role=role
        self.age=age
        self.salary=salary
        print("i have set the values to specific object")

    def employeeDetails(self):
        print(f"\nEmployee name is {self.name} \nAge is {self.age} \nRole is {self.role}\nSalary is {self.salary}")

    def getEmployeeSalary(self):
        print(f'\nsalary is {self.salary}')

    
    @staticmethod
    def employeeBank():
        print(f'cpmany uses default ICICI bank for all the employees')

    @staticmethod
    def employee(name,salary):
        mylisal=[]
        print(f'company {name}\nsalary {salary}')
        bonus=30000
        salary=salary+bonus
        mylisal.append(salary)
        if salary<50000:
            print("Total salary is ",salary)
            return salary,bonus
        else:
            print("Total salary is greater than 50000",salary)
            return salary,bonus
        
    @classmethod
    def changeDetails(self,name,role):
        self.name=name
        self.role=role
        print(f'i have changed this role {self.role} for {self.name} it will work only in this method call and it wont change in the constructor init method ')


emp1=Employee("Rohan","front-end dev",20,50000)
emp1.employeeDetails()
emp2=Employee("mohan","back-end dev",24,60000)
emp2.employeeDetails()
emp1.employeeBank()
emp1.getemployeeSalary()
emp1.employeeBank()
emp1.employee("anees",40000)
emp1.changeDetails("ark","Full stack dev")
emp1.employeeDetails()

emp2=Employee("Shreya","database engineer",21,50000)
emp2.employeeDetails()
emp2.changeDetails("Shreya","backend dev")