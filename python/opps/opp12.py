#multilevel inheritence

class India:
    states=["Karnataka","Ap","up","bihar","kashmir","goa","TN"]
    
    def indiaDetails(self):
        print(f"India Details are {self.states}")
    
class Karnataka(India):
    def __init__(self,name):
        self.name=name
        print("Constructor of Karnataka")


    district=["Chikabalapur","mangalore","Tumkur","Bangalore Urban"]
    def karnatakaDetails(self):
        print(f"karnataka district are {self.district} {self.name}")
    
class Bangluru(Karnataka):
    def __init__(self, name):
        super().__init__(self)
        self.name=name
        print("constructor of bangluru")

    wards=["chamrajpet","hebbal","marathalli","devenhalli"]
    def BangluruDetails(self):
        print(f"Bangluru wards are {self.wards}")


class Marathalli(Bangluru):
    def __init__(self, name):
        self.name=name

    instituteName=["Ria","governmentInstitue"]
    def instituteNameDetails(self):
        print(f"Marathalli institute are {self.instituteName}")


obj=Bangluru("anaya")
print(obj.BangluruDetails())
print(obj.wards)
print(obj.district)
print(obj.karnatakaDetails())
print(obj.states)
print(obj.indiaDetails())