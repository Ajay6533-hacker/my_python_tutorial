                     # Metlhod (function)
# def function1():      # function with without arguement
#     a=78
#     b=89
#     c=a+b
#     print("additon of two numbers ",c)
# function1()

                                                 # function with arguement

# def function2(a,b):
#     """this is used for function and doc string"""    # this is doc string intionalize after function creation
#     print("addition of two numbers",a+b)
#
# print(function2.__doc__)
# function2(89,36)

                                    # function give return value
def function3(a,b):
    average=(a+b)/2
    print(average)
    return a
v=function3(3,5)
print(v)

def function4():
    a=89
    b=78
    print(a+b)
    return a+b
s=function4()
print(s)

                                   # Try and except
#
# print("enter your first number")
# a=input()
# b=input("enter your second number \n")
# try:
#     print("sum of two numbers",int(a)+b)
# except Exception as e:
#     print(e)
# print(int(a)+int(b))

                            #  Input output File
'''
"r"-open file for reading    #read mode(default)
"w"-open a file for write
"a"- add more content in file
"x"-creat  file if not exists
"t"- text mode           # read mode(default)
"b"- binary mode
"+"- for read and write
'''
# f=open("ajay.txt","w")        # f is a file pointer , open return the value by f pointer
# content=f.write("yes this is changed ok")
# print(content)
#
# f=open("ajay.txt","rb") #("self,mode")
# content=f.read()
# print("1"content)
# print("2",content)
# content=f.read(4)
# print("2",content)

# f=open("ajay.txt","r")
# content=f.read(5)
# #content=f.read(5)
# for line in content:
# print(line,end="")
# f=open("ajay.text","rb")
# content=f.read()
# print(content)
# f.close()





