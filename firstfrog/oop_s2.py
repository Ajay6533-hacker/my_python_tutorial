#                                     # self and _int_function
# class Employee:
#     number_of_leaves=4
#
#     def printdetils(self):
#         return f"this is {self.name} this is id {self.id} and rol {self.rol},and this{self.number_of_leaves} "
# ajay=Employee()
# vijay=Employee()
#
# ajay.name="ajay"
# ajay.rol="manager"
# ajay.id=1
#
# vijay.name="vijay"
# vijay.rol="manager"
# vijay.id=2
#
# print(ajay.printdetails())

                                           #  constructor
class Employee:
    def __init__(self,a,b,c):
        self.name=a
        self.rol=b
        self.id=c

# ajay=Employee()
# vijay=Employee()
#
# ajay.name="ajay"
# ajay.rol="manager"
# ajay.id=1
#
# vijay.name="vijay"
# vijay.rol="manager"
# vijay.id=2

sanjay=Employee("sanjay",1,"manager")
print(sanjay.id)
