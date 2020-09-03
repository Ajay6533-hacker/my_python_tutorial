class Employee:
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname
        #self.email=f"{self.name}.{self.lname}@gmail.com"
    def explain(self):
        return f"this is first name {self.name} and last name is {self.lname}"

    @property
    def email(self):
        return f"{self.name}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("setting now")
        vname=string.split("@")[0]
        name=vname.split(".")[0]
        lname=vname.split(".")[1]
        print(" setting end")
rahul=Employee("rahul","kumar")
roshan=Employee("roshan","kumar")
print(rahul.email)
rahul.name="ajay"
print(rahul.email)
roshan.email="rohan.kumar@email.com"
print(roshan.email)