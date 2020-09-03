#
# class Employee:
#     leaves=7
#     def no_of_emp(self):
#         return print(f"this is name of employee{self.name} salary is {self.salary} and post is {self.post}")
#     def __init__(self,aname,bsalary,cpost):
#         self.name=aname
#         self.salary=bsalary
#         self.post=cpost
#     @classmethod
#     def change_leaves(cls,new_leaves):
#         cls.leaves=new_leaves
#     @classmethod
#     def alternative(cls,string):
#         # params=string.split("-")
#         # print(params)
#         # return cls(params[0],params[1],params[2])
#         return cls(*string.split("-"))
# rahul=Employee("rahul","35000","manager")  #  constructor
# print(rahul.name)
# ajay=Employee("ajay","40000","founder")
# print(ajay.post)
# deepak=Employee.alternative("deepak-30000-accountant")  #  constructor
# print(deepak.name)
# ajay.change_leaves(20)
# print(ajay.leaves)
# print(Employee.leaves)

# ______________________________________class method ____________________________________________________________________




# ajay=Employee()
# deepak=Employee()
#
# #
# # rahul.name="rahul"
# # rahul.salary=35000
# # rahul.post="manager"
#
# ajay.name="ajay"
# ajay.salary=30000
# ajay.post="manager"
#
# deepak.name="deepak"
# deepak.salary=25000
# deepak.post="accountant"
#
# ajay.leaves=7
# print(ajay.leaves)
# print(Employee.leaves)
# print(deepak.leaves)
#
# Employee.leaves=10
# print(Employee.leaves)
#
# print(ajay.no_of_emp())
#
# __________________________________________________part 2__________________________________________________________________________________

class Student:
    holiday=4
    leaves=7
    def info(self):
        print(f"this is name of student {self.name} roll no. is {self.roll} and subject is {self.subject}")
        return print("function are represent into the class")
    def __init__(self,aname,broll,csubject):
         self.name=aname
         self.roll=broll
         self.subject=csubject
                                                            # constructor
# ajay=Student("ajay",8,"arts")
# print(ajay.__dict__)
    @classmethod
    def stud(cls,holidays,leave):
        cls.holiday=holidays
        cls.leaves=leave
    @classmethod
    def alternatives(cls,str):
        param=str.split("-")
        print(param)
        return cls(param[0],param[1],param[2])
vijay=Student.alternatives("vijay-1-science")
amit=Student.alternatives("ajay-8-manager")
# print(vijay.roll)
# vijay.stud(5,2)
# print(vijay.holiday)
# print(amit.holiday)
# print(vijay.leaves)
vijay.holiday=19
print(Student.holidays)

# print(vijay.name)
# vijay.stud(20)
# print(vijay.holiday)
# amit.name="amit"
# amit.roll=10
# amit.subject="science"
# print(amit.leaves)
# print(amit.info())
