
                                                         #   This is maping or apply on all list or variable
# number=["5","67","34","9","34"]
# a=list(map(int,number))
# b=a[2]+6
# print(b)

# for i in range(len(number)):
#     a=int(i)
#     print(a)

# for i in range(len(number)):
#     number[i]=int(number[i])
#     print(number)

# for i in range(len(number)):
#     number[i]=int(number[i])
#     print(number)
# number[3]=number[3]+3
# print(number[3])

# def sqr(a):
#     return a*a
# num=[2,7,5,7,8]
# square=list(map(sqr,num))
# print(square)

# num=[6,3,24,6,8]
# sqr=list(map(lambda x:x*x,num))
# print(sqr)
"""
def square(a):
    return a*a
def cube(a):
    return a*a*a
store=[square,cube]
for i in range(1,5):
    s=list(map(lambda x:x(i),store))
    print(s)
"""

                                           #   This is filter function
"""                                           
num=[4,7,2,9,67,89,45,12,45,3,9,10]
def fil(num):
    return num>20
s=list(filter(fil,num))
print(s)
"""
#                                      # Reduce function
# from functools import reduce
# a=[5,6,9,2,4,6]
# # num=0
# # for i in a:
# #     num=num+i
# # print(num)
# k=reduce(lambda x,y:x+y, a)
# print(k)

# ____________________________________________Practice map,filter and reduce __________________________________________________________

                                         # map
# list=["enumerate","join","main","mamp","filter"]
# list1=["1","2","3","4","5"]
# map1=list(map(int,list1))
# print(map1)

# def sqr(a):
#     return a*a
# def cube(b):
#     return  b*b*b
# list2=[sqr,cube]
# for i in range(10):
#     s=list(map(lambda x:x(i),list2))
#     print(s)

                              # filter
#
# string1=["vikash","arun","vinaj","jay"]
# def  filt(map1):
#     return map1>2
# k=list(filter(filt,map1))
# print(k)
 #                        reduce ___________________________________________________

# from functools import reduce
# a=[5,6,9,2,4,6]
# j=reduce(lambda x,y:x+y,a)
# print(j)

# num=0
# for i in a:
#     num=num+i
# print(num)

# a=[5,6,9,2,4,6]
# num=0
# for i in a:
#     num=num+i
# print(num)


#--------------------------------------------   map ----------------------------------------

list1=["2","3","5","6","3","2","5","6"]
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(list1)
print(type(list1))

Map=list(map(int,list1))
print(Map)

# I want to square of iteself numbers
map1=list(map(lambda x : x*x,list1))
print(map1)


def square(a):
    return a*a
def cube(a):
    return a*a*a
container=[square,cube]
# for i in range(10):
#     map2=list(map(lambda x:x(i),container))
#     print(map2)

# I want to use the filter function
a=[3,3,2,4,2,4,5,34,3]
fil=list(filter(lambda x : x>=4,a))
print(fil)

#  I want to use reduce function
from functools import reduce
map4=reduce(lambda x,y:x+y,a)
print(map4)




