                                 #  *args and **kwargs
# def fun(*args):
#     print(args[0])                 # this is a tuple
#     print(type(args))
# aj=["onion","potato","tomato","brinjal"]
# fun(*aj)
# print(aj)


# def fun(*args):
#     print(args[0])                # this is a tuple
#     for item in args:
#         print(item)
#     print(type(args))
# aj=["onion","potato","tomato","brinjal","chilli"]
# fun(*aj)
# print(aj)

#
# def fun(normal,*args):
#     print(normal)
#     print(args[0])                # this is a tuple
#     for item in args:
#         print(item)
#     print(type(args))
# normal="This is normal ,write in first into the function"
# aj=["onion","potato","tomato","brinjal","chilli"]
# fun(normal,*aj)
# print(aj)
"""
def fun(normal,*args,**kwargs):
    print(args[2])
    for item in args:
        print(item,end=" ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
normal="This is normal ,write in first into the function"
aj=["onion","potato","tomato","brinjal","chilli"]
aj2={"ajay":"principle","vijay":"teacher"}
#dict1=["teacher":"vijay","principle":"afh"]
fun(normal,*aj,**aj2)
"""
# def funct(a,*args,**kwargs):
#     print(type(args))
#     print(args)
#     print(a)
#     print(kwargs)
# b="this is used for normmal in function"
# c=["onion","potato","brinjal"]
# d=["kl","k2","k3"]
# print(type(c))
# funct(b,*c,**d)

# ----------------------------------Args and kwargs and normal function ---------------------------------------
#
#
# def fibo(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# # print(fibo(5))
#
# def func2(a,b,c):
#     """this is a doc string"""
#     average=(a+b)/c
#     #print(average)
#     return average
# print(func2.__doc__)
# s=func2(9,11,2)
#     # func2(9,5,2)
# print(s)

# def use_func(normal,*args,**kwargs):
#     print(args)
#     for index,(item,value) in enumerate(kwargs.items()):
#         if index%2==0:
#             print(f"{item} is {value}")
#     print(normal)
# list1=["ajay","vijay","deepak","saurabh","rahul"]
# simple="this is usd for specially for normal arguement"
# list2={"me":"ajay","brother":"vijay","friend":"deepak"}
# use_func(simple,*list1,**list2)

#--------------------------------------------Normal , Args and Kwargs--------------------------------------------------------------------------

# Inside the function take first-arguement is normal and second is args(*) and thid is  kwargs(**)
def func(n ,*args ,**kwargs):
    # print("thiss is",args)
    print(n)
    print(type(args))
    # print(args)
    print(kwargs)
    print(dsad)

# arg_func = "This is a args variable"  # All character take a sting
arg_func = ["Ajay","Rohan","vikash","rahul","Roshan","deepak"]
normal="This is a normal varaible"
# kwarg = [["This is a kwargs function" ,"this is two",]]
kwarg = [["ajay","Student"],["lakhan","Ram"]]
kwargs_func = dict(kwarg)
dsad  = "djolkg"
func(normal, *arg_func, **kwargs_func , dsad)