
                                              #  Creating class
# class Student:
#     pass
# ajay=Student()
# vijay=Student()
# print(ajay,vijay)          # ajay and vijay both are store in different memory address
#
# ajay.name="ajay"
# ajay.branch="C.E"
# ajay.roll=1
# vijay.name="ajay"
# vijay.branch="C.E"
# vijay.roll=1
# vijay.subject=["hindi","english"]
# print(ajay.roll)
# print(vijay.subject)
                                                    # Instance and class variable

# class Employee:
#     sellary=1500                        # this variable are change only by Employee
#     pass
# ajay=Employee()
# aman=Employee()
# ajay.name="Ajay"
# ajay.id="1"
# ajay.rol="manager"
# print(ajay.sellary)
# ajay.sellary=1000
# print(ajay.sellary)
# print(ajay.__dict__)
# aman.name="Ama"
# aman.id="1"
# aman.rol="accountant"
# print(aman.rol,aman.sellary)

""" ---------------------------------------OOPs2--------------------------------------------------------------"""
#
# class Student:
#     Subject = ["jave","c","c++","python"]
#     Excur =  "crecket"
#     pass
# Ajay = Student()
# Deepak=Student()
# Rahul=Student()
#
# Ajay.Roll =  "01"
# Ajay.name = "ajay"
# Ajay.Branch = "C.E"
#
# Deepak.Roll =  "02"
# Deepak.name = "Deepak"
# Deepak.Branch = "C.E"
#
# print(Deepak.__dict__)
# print(Ajay.Subject)
# print(Deepak.Subject)
# # Deepak.Excur = "football"
# print(Deepak.Excur)
# print(Ajay.Excur)
# Student.Excur =  "badminton"
# print(Deepak.Excur)

class Employee:
    def aj(self):
        return f"this is name of the employee {self.name} salary is {self.salary} and post {self.post}"
    def __init__(self,name,salary,post):
        self.name = name
        self.salary =salary
        self.post = post

Ajay = Employee("ajay","30000","Manager")
print(Ajay.__dict__)     # Constructor
#Deepak = Employee("Deepa")

#Ajay.name =  "Ajay"
#Ajay.salary = "30000"
#Ajay.post = "Manager"

#Deepak.name =  "Deepak"
#Deepak.salary = "15000"
#Deepak.post = "P.O"
#print(Ajay.aj())
