# def sub(k,l):
#     return print(k-l)


# a=5 # global variable
# def var():
#     # a=3 # local variable
#     b=4 # local variable
#     global a  # global keyword
#     a=a+5+5+5      # most importent :- store first three number after first execution
#     global sub
#     def sub(k,l):
#         return print(k+l)
#     sub(100,2)
#     c=a
#     print(c)
#     return 0
# var()
# print(s)
# sub(28,2)
# var()
# var()
# var1=6
# def add(a,b):
#     average=(a+b)/2
#     out+inner=average+var1

# var1=42 # Global variables
# def add():
#     # var1=56   #Locale variables
#     var2=4
#     global var1
#     var1=42+6
#     print("Addition of two numbers",var1+var2)
# add()
# print(var1)

def add():
    var1=2
    def sub():
        global var1  # global keyword
        var1 = 20
        var4=15
        var2 = 10
        print("Subtraction of numbers",var4-var2)
        print("this is var1",var1)
    sub()
    print("Addition", var1 + 5)
add()
print("this is var1", var1)