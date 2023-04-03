class Employee:
    company="T.C.S"
    employeename="default name"
    salary=" default salary"

    def employeeDetails(self):
        print(f"\nEmployee is working at {self.company}\nEmployee name is{self.employeename}\nEmployee salary is{self.salary}")


emp1=Employee()
emp1.employeename="anaya"
emp1.salary=50000
emp1.company="Infosis"
emp1.employeeDetails()


emp2=Employee()
emp2.employeename="Puja"
emp2.salary="200000"
emp2.company="Google"
emp2.employeeDetails()