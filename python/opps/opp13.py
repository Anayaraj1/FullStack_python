class Company:
    company_name="Accenture"

    def __init__(self,EmployeeName,EmployeeRole,EmployeeSalary):
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeSalary
        print("\n\ni am consructor of company")

    def CompanyEmployeeDetails(self):
        print(f"\nCompany name is {self.company_name}\nEmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}")


class Employee(Company):
    def __init__(self, EmployeeName, EmployeeRole, EmployeeSalary,EmployeeManager,EmployeeTl):
        super().__init__(EmployeeName, EmployeeRole, EmployeeSalary)
        self.EmployeeManager=EmployeeManager
        self.EmployeeTl=EmployeeTl
        print("\n\n i am constructor of Employee")

    def EmployeeDetails(self):
        print(f"\nEmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}\nEmployeeManager is {self.EmployeeManager}\nEmployeeTL is {self.EmployeeTl}")



obj1=Employee("Anaya","Data Analyst",50000,"annes","Chaitu")
obj1.CompanyEmployeeDetails()
obj1.EmployeeDetails()
print(obj1.EmployeeName)

cp1=Company("TCs","Back end dev",90000)
print(cp1.company_name)
cp1.CompanyEmployeeDetails()