
# class Student:
#     holiday=4
#     leaves=7
#     def info(self):
#         print(f"this is name of student {self.name} roll no. is {self.roll} and subject is {self.subject}")
#         return print("function are represent into the class")
#     def __init__(self,aname,broll,csubject):
#          self.name=aname
#          self.roll=broll
#          self.subject=csubject
#                                                             # constructor
# # ajay=Student("ajay",8,"arts")
# # print(ajay.__dict__)
#     @classmethod
#     def stud(cls,holidays,leave):
#         cls.holiday=holidays
#         cls.leaves=leave
#     @staticmethod
#     def simple(string):
#         print("this is me" + string)
#     @classmethod
#     # def alternatives(cls,str):
#     #     param=str.split("-")
#     #     print(param)
#     #     return cls(param[0],param[1],param[2])
#     def alternatives(cls, str):        #   class method alternative constructor
#      return cls(*str.split("-"))
#
# vijay=Student.alternatives("vijay-1-science")
# amit=Student.alternatives("ajay-8-manager")
# print(vijay.roll)
# vijay.stud(5,2)
# print(vijay.holiday)
# print(amit.holiday)
# print(vijay.leaves)
# amit.simple( " ajay")
# vijay.simple( " ajay")
# print(vijay.__dict__)
# print(vijay.name)
# vijay.stud(20)
# print(vijay.

# _________________________________________Single Inheritance _______________________________________________________________
#
# class Employee:
#     no_of_leaves=3
#     holiday=4
#     def printdetails(self):
#         print(f"this is name of employee {self.name} id is {self.id} and role is {self.role}")
#     def __init__(self,a,b,c):
#         self.name=a
#         self.id=b
#         self.role=c
# ajay=Employee("ajay",101,"owner")
# vijay=Employee("vijay",102,"manager")
# print(vijay.printdetails())
#
# class Programmer(Employee):
#     def printdetail(self):
#         print(f"this is name of programmer {self.name} work is {self.work} and iterest in{self.interest} and live in {self.live}")
#     def __init__(self, a, b, c, d):
#         self.name = a
#         self.work=b
#         self.interest=c
#         self.live=d
#     @classmethod
#     def alternatives(cls,slash):
#         params=slash.split("-")
#         print(params)
#         return cls(params[0],params[1],params[2],params[3])
# deepak=Programmer.alternatives("deepak-business-movies-delhi")
# # ajay=Employee.alternatives("ajay-programer-movies")
# print(deepak.printdetail())
# print(ajay.printdetails())
# _________________________________________________multiple inheritance _____________________________________________________________________

# class Employee:
#     no_of_leaves=3
#     holiday=4
#     def printdetails(self):
#         print(f"this is name of employee {self.name} id is {self.id} and role is {self.role}")
#     def __init__(self,a,b,c):
#         self.name=a
#         self.id=b
#         self.role=c
# ajay=Employee("ajay",101,"owner")
# vijay=Employee("vijay",102,"manager")
# #print(vijay.printdetails())
#
# class Player:
#     time_use=2
#     def __init__(self,name,games):
#         self.name=name
#         self.games=games
#     def detailprint(self):
#         return print(f"name of player {self.name} and game is{self.games}")
# class Expert(Employee,Player):
#     pass
    # def __init__(self,a,b,c,d):
    #     self.name=a
    #     self.salary=b
    #     self.time=c
    #     self.work=d
    # def __init__(self,name,time,salary):
    #     self.name="name"
    #     self.time="time"
    #     self.salary="salary"

#________________________________________________multilevel inheritance __________________________________________________________________________________
#
# class Father:
#     cricket=4
#     def __init__(self,a):
#         self.name=a
#     def printdetails(self,a):
#         return f"{self.a} is Father of all child"
#
# class Son(Father):
#     badminton=3
# class Grandson(Son):
#     pass
# ajay=Father("ajay")
# deepak=Son()
# rahul=Grandson()
# # print(ajay.name)

#___________________________________Public ,Protected and Private ____________________________________________________________________
# class Father:
#     carrom=3
#     _clas=5
#     __outdoor_game=1.5
#     def __init__(self,work,time):
#         self.work=work
#         self.time=time
# ajay=Father("programming",8)
# print(ajay._Father__outdoor_game)
# class Son(Father):
#     play=4
#     # def __init__(self,job,part_time):
#     #     self.job=job
#     #     self.part=part_time
#     def printdetails(self):
#         return f"this is work{self.work} and time is{self.time}"
# vijay=Son("govt",10)
# print(vijay.printdetails())

# __________________________________________________Super function ________________________________________________________________

# class A:
#     var1="I am inside the class variable A"
#     def __init__(self):
#         self.var1="This is method in inside of the class A"
#         self.variable2="this is me inside the class A"
#         self.important="i want to print this line"
# class B(A):
#     var1="I am inside the class variable B"
#     def __init__(self):
#         # super().__init__()                                    #solve the overriding in constructor
#         self.var1="This is method in inside of the class B"
#         self.variable2="this is me inside the class B"
#         super().__init__()
# a=A()
# b=B()
# print(b.important ,b.var1 ,b.variable2)

# #________________________________________________Diamond shape problem ______________________________________________________________
#
# class A:
#     var1=" This class from A"
# class B(A):
#     var1 = " This class from B"
# class C(A):                                           # This problems are create by using multiple inheritance
#     var1 = " This class from C"
# class D(C,B):
#     pass
# a=A()
# b=B()
# c=C()
# d=D()
# print(d.var1)
# ______________________________________Operator overloading and Dunder methods _______________________________________________________________-

class Employee:
        def __init__(self,name,work,time):
            self.name=name
            self.work=work
            self.time=time
        def printdetails(self):
            return f"this is employee name {self.name} work is {self.work} and {self.time}"
        def __add__(self, other):
            return self.time + other.time                      # Dunder method are starting with double underscore(__) and ending with double double underscore(__)
        def __sub__(self, other):
            return 89
        def __truediv__(self, other):
            return self.time / other.time
        def __repr__(self):
            return  f"'{self.name}','{self.work}','{self.time}'"
        def __str__(self):
            return f"this is employee name {self.name} work is {self.work} and {self.time}"
ajay=Employee("Ajay","programmer",8)
deepak=Employee("Deepak","programmer 2",10)
print(ajay+deepak)
print(ajay - deepak)
print(ajay / deepak)
print(repr(ajay))
print(ajay)


