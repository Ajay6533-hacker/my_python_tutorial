def add():                              # Input_Output file
    pass
    """
    "r" -open file for reading      #default mode
    "w" -open file for writing
    "x" - creates file in not exists                                 exclusive creation
    "a" - Add more content to a file
    "t" - text mode            #default mode
    "b" -binary mode
    "+" - read and write
    """
# print(add.__doc__)
'''
f=open("practice1.py" ,"r")         #   open(file name , mode)
content=f.read()
print(content)
f.close()
'''
"""
#f=open("ajay.txt")
# content=f.write()
# print(content)
# f.close()
# for line in f:
#     print(line,end=" ")
#print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
                                   #  File write
# f=open("ajay2.txt","w")
# s=f.write("ajay is a good boy")
# print(s)
# f.close()

# f=open("ajay2.txt","a")
# f.write("ajay is a good boy")
# f.close()
                                        # Read and write
'''
f=open("ajay2.txt","r+")
print(f.read())
f.write("read and write mode\n")
f.write("read and write mode\n")  '''

                            #  Tell("this function tell where the file pointer on the line") and seek("this is used to reset file pointer") function
# f=open("ajay.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.seek(10))
# print(f.readline())
# print(f.tell())

                                             #  Block to open python files
def a():
    "this is a write choice baby"
    with open("ajay.txt") as f:
        a=f.read()
        print(a)
        print(a.__doc__)
a()
"""

# f=open("ajay.txt")
# store=f.read()
# print(store)
# f.close()
#
# f=open("ajay3.txt","w")
# content=f.write("this is my practice\n")
# print(content)
#
# f=open("ajay3.txt","a")
# content=f.write("this is my practice\n tis is me")
# print(content)

#
# f=open("ajay3.txt","r+")
# print(f.read())
# content=f.write("this is my practice\n ")
# content2=f.write("yes this is me")
# print(content2)
# print(content)
#
# f=open("ajay3.txt","r+")
# print(f.tell())
# # print(f.readline())
# # print(f.tell())
# # print(f.read())
# # print(f.seek(10))
# # print(f.tell())
# print(f.readline())
# print(f.seek(10))
# print(f.tell())
# content=f.write("this is my practice\n ")
# content2=f.write("yes this is me")
# print(content2)
# print(content)

#---------------------------------------------------------------------------------------------------------------------------------
# f=open("ajay4.txt","r") #by default this is read mode
# print(f.read())
# print(f.tell())
# print("1",f.readline(9))
# print(f.seek(15))
# print("2",f.readline())
# print(f.tell())
# f.readline()
# print(a)
# print(f.readline())
# print(f.readlines())
# f.write("this is used for if file are exist in file \nthan ignore it else create a new file")
# f.write("this is me\n")
# f.close()

# print()
#
# f=open("ajay2.txt","a")
# f.write("ajay is a good boy \n")
# f.close()


# f = open("ajdon.txt" , "r")
# with open("ajdon.txt", "r") as f:
#     # content=f.write("This is my new file before these not creation")
#     # content=f.readline()
#     content=f.readlines()
#     print(content)
    # f.close()

# f = open("ajdon.txt" , "a")
# # content=f.readable()
# content=f.write("This is my fourth line \n")

f = open("ajay2.txt", "r")
# content=f.readlines()
# print(content)
# add = f.write("this is my last number of my read and write file \n ")
content=f.readline()
print(f.tell())
print(f.readline())
print(f.tell())
# print(f.seek(20))
# print(f.readline())
# print(f.readline())
print(f.newlines)
print(f.tell())
# print(f.readlines())
# print(f.seek())
# print(content)




























from tkinter import *
# def name():
#     global  name_input
#     name_root = Tk()
#     name_root.minsize(700,400)
#     name_label =  Label(name_root,text = "N A M E ",font =  "cascade 30 bold")
#     name_label.grid(row = 0, column = 0)
#     name_var =  StringVar()
#     name_entry =  Entry(name_root,textvariable = name_var,width=40)
#     name_entry.grid(row = 0 , column = 1)
#     def get1():
#         global name_input
#         name_root.destroy()
#         name_input=name_var.get()
#         # print(" this is input",name_input)
#     sub_button = Button(name_root,text = " O K ", font = "cascade 30 bold",command=get1)
#     sub_button.grid(row=0,column=2)
#     def main():
#         global  name_input
#         name_label.destroy()
#         name_entry.destroy()
#         sub_button.destroy()
#         f = open("ajay.txt")
#         label=Label(name_root,text=f.readline(),font="cascade 20 bold")
#         label.grid(row=0,column =0)
#     main()
#     name_root.mainloop()
#
# name()



#
# # print(f.tell())
# print(f.readline())
# # print(f.seek(10))
# print(f.readline())
# # print(f.tell())
