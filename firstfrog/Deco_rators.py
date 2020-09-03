# def function1():
#     print("this is decorators")
# v=function1
# del function1
# v()
#
# def funcret(num):
#     if num==0:
#         return int
#     elif num==1:
#         return sum
#     elif num==2:
#         return print
# a=funcret(2)
# print(a)
#
#
# def executor(arg):
#     arg("This")
# executor(print)

                                                     #  decorators
#
# def dec1(func1):
#     def nowexec():
#         print("executing now")
#         func1()
#         print("Executed")
#     return nowexec
# @dec1
# def who_is_ajay():
#     print("ajay is a good boy")
# who_is_ajay=dec1(who_is_ajay)
# who_is_ajay()
#
#
# def ajay():
#     print("This is me")
# vijay=ajay
# del ajay
# ajay()

#
# def aj(a):
#     if a>=5:
#         return int
#     else:
#         return sum
# aj(2)

# def a(fun1):
#     def b(c,d):
#         print(c+d)
#         fun1()
#         print("this print after the executor")
#     return b(6,7)
# def fun1():
#     print("this is first print")
# fun1=a(fun1)
# h=fun1
#
# def dec1(any):
#     def add(a,b):
#         c=a+b
#         print(c)
#         any()
#         print("this print after the second function")
#     return add(4,3)
#
# #@dec1
# def dec2():
#     def sub(g,h):
#         print("subtraction of g and h",g-h)
#     return sub(70,50)
# dec2=dec1(dec2)
# # h=dec2
# dec2()

#   _________________________practice of decorator ________________________________________________________________________________

# def multiply(other):
#     def mult(a,b):
#         c=a*b
#         print(c)
#         print("this function are before execution")
#         other()
#         print("other function execution")
#     return mult(9,2)
# #@multiply
# def dec2():
#     def add(d, e):
#         f=d+e
#         print(f)
#     return add(90, 10)
# dec2 = multiply(dec2)
#

#-----------------------------------Decorator ----------------------------------------------------------------------------
#
def calculator(sub):
    def add():
        print("this is before the execution")
        a=int(input("enter your first for add number\n"))
        b=int(input("enter your second for add number\n"))
        c=a+b
        print("this is after the addion function",c)
        sub(k,l)
    return add
k=int(input("enter your first number for subtract\n"))
l=int(input("enter your second number for subtract\n"))
@calculator
def sub(k,l):
    c=k-l
    print("subtraction of two number",c)
sub()