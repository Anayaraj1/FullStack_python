class Employee():
    company="T.C.S"
    employeeName="default name"
    salary="50000"

    def employeeDetails(self):
        print(f"\nEmployee is working at {self.company}\nEmployee name is {self.employeeName}\nEmployee salary is {self.salary}")


class Company:
    no_of_employee="2 lakh"

    def companyDetails(self):
        print("company is accenture it will fired 20,000 employee",self)

emp1=Employee()
emp1.employeeName="anaya"
emp1.company="Google"
emp1.salary=400000
emp1.employeeDetails()


emp2=Employee()
emp2.employeeDetails()


print("\n")
obj1=Company()
print(obj1.no_of_employee)
obj1.companyDetails()