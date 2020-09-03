                            # Recursion
#
# j=0
# def rec():
#     global j
#     j=j+1
#     print("This is used for recursion",j)
#     # rec()
# rec()
# import sys
# print(sys.getrecursionlimit())


        # fibonacci numbers(4) = 4*3*2*1
#
# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# # number=int(input("enter your number"))
# # n=int(input("enter your number\n"))
# print(fibonacci(7))

          #Recursion

# def recursion1(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return recursion1(n)*recursion1(n-1)
# number=int(input("enter a number\n"))
# print(n)
# recursion1(number)

#--------------------------------------------------Recursion 2 -----------------------------------------------------------------------------------------

# def recur(k):
#     if k>0:
#         result=k+recur(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# recur(3)
#
# def recur1(recur2):
#     i=0
#     if i>0:
#         return 0
#     else:
#         i=i+1
#     return i+(i-1)
# @recur1
# def  recur2():
#     for i in range(2,10,2):
#         return i+(i-1)

# # _______________________________________Recursion ____________________________________________________________
# def factorial_iterative(n):
#     """
#     n*(n-1)
#     n! (5)=5*(5-1)*(4-1)*(3-1)*(2-1):-5*4*3*2*1
#     """
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# a=factorial_iterative(3)
# print(a)

# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# print(factorial_recursive(3))

# fibonachi series :-1,1,2,3,5,8,13, .......
# def fib(n):
#     if n== 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#  print(fib(4))

# def rec_iterative(n):
#     store = 1
#     for i in range(n):
#         store=store*(i+1)
#     return store
# print(rec_iterative(4))
#
# def recursive(n):
#     if n==0:
#         return  1
#     else:
#         return n * recursive(n-1)
# print(recursive(4))
#
# def fibo(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(5))

# Recursion - Iterative and recursive

# factorial(4) = 4*3*2*1
# Number= int(input("Enter your focrorial numbers \n"))
# def numrecur(n):
#     if n==1:
#         return 1
#     else:
#         return n * numrecur(n-1)     # this is recursive method
# # print(numrecur(Number))
#
# def numiter(n):
#     func = 1
#     for i in range(n):
#         func = func * (i + 1)     # this is iterative recursion
#     return func
# # print(numiter(Number))
#
# # find the N th of fibonacci series
# # fibonacci - 0,1,1,2,3,4,7,11,etc...
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fibo(n+1)+fibo(n-1)
# print(fibo(Number))