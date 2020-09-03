                   #  Function with doc_string,return statement  # Two types of function= built in function and user define function

# a=67
# b=67                                  # This is a built in function
# print(sum([a,b])) #sum(iterable)
# def func1():
#     print("This is a function without arguement")
# func1()
#                    # This is a function with arguement
# def func2(a,b,c):
#     """this is a doc string"""
#     average=(a+b)/c
#     #print(average)
#     return average
# print(func2.__doc__)
# s=func2(9,11,2)
#     # func2(9,5,2)
# print(s)


                     #  Lambda function or anonymous function  =  this is a one liner function
# function1=lambda x,y:x+y
# print(function1(2,5))

# def a_first(a):
#     """this is doc string"""
#     return a[1]
# a=[[6,8],[2,5],[4,9]]
# a.sort(key=a_first)
# print(a)
# print(a_first.__doc__)

# func2=lambda a
# print(3)
# a=[[6,8],[2,5],[4,9]]
# a.sort(key=lambda x:x[1])
# print(a)


# simple functioin
def display():       # function without arguement
    print("this is inside the function")
display()


def add(a,b):  # Fuciton with arguement
    """this is a doc string"""
    c=a+b
    print("sum of these two numbers",a+b)
    return c
s=add(10,20)
print(s)
print(add.__doc__)

