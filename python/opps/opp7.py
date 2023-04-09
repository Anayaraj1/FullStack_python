
# single level inheritance

class Company:
    company_Name="Accenture"

    def __init__(self,location,branch,no_of_block):
        self.location=location
        self.branch=branch
        self.no_of_block=no_of_block

    def companyDetails(self):
        print(f'Company is{self.company_Name}\nLocation is {self.location}\nBranch is {self.branch}\n No of Building is {self.no_of_block}')


    @staticmethod
    def companySalary():
        print(" Base salary is 4LPA")

class Employee(Company):

    def __init__(self, EmployeeName,EmployeeRole,EmployeeSalary):
        self.EmployeeName=EmployeeName
        self.EmployeeRole=EmployeeRole
        self.EmployeeSalary=EmployeeRole

    def EmployeeDetails(self):
        print(f'EmployeeName is {self.EmployeeName}\nEmployeeRole is {self.EmployeeRole}\nEmployeeSalary is {self.EmployeeSalary}')

    def EmployeeInsurance(self):
        print(f'{self.company_Name} has HIP policy')


emp1=Employee("harshit","dev",23000)
print(emp1.company_Name)
emp1.companySalary()
emp1.EmployeeDetails()