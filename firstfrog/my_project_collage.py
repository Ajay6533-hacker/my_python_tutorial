# from tkinter import *
# root=Tk()
# root.geometry("800x500")
# list1=["This is Blank ","1. who is Goood Actor in world "]
# def number(n):
#     for i in range(1,n):
#         yield i
# num=number(100)
# def Question():
#     a=num.__next__()
#     # lbox.insert(ACTIVE,num.__next__())
#     if a==1:
#         lbox.insert(ACTIVE,f"{list1[1]}")
#     if a==2:
#         lbox.insert(ACTIVE,f"{list1[2]}")
#     elif a==3:
#         lbox.insert(ACTIVE,f"{list1[3]}")
#     elif a==4:
#         lbox.insert(ACTIVE,f"{list1[4]}")
#     elif a==5:
#         lbox.insert(ACTIVE,f"{list1[5]}")
#     elif a==6:
#         lbox.insert(ACTIVE,f"{list1[6]}")
#     elif a==7:
#         lbox.insert(ACTIVE,f"{list1[7]}")
#     elif a==8:
#         lbox.insert(ACTIVE,f"{list1[8]}")
#     elif a==9:
#         lbox.insert(ACTIVE,f"{list1[9]}")
#     elif a==10:
#         lbox.insert(ACTIVE,f"{list1[10]}")
#     elif a==11:
#         lbox.insert(ACTIVE,f"{list1[11]}")
#
# Label(root,text="This is list of questions",bg="red",font="cascade 19 bold").pack(padx=10)
# lbox=Listbox(root)
# lbox.pack(anchor="nw",fill="x",padx=10,pady=10)
# lbox.insert(END,"nothig")
# Button(root,text="Add",bg="blue",fg="white",command=Question).pack(padx=10)
# # e.event()
# root.mainloop()

# def inp(n):
#     for i in range(n):
#         yield i
# prof=inp(10)
# print(prof.__next__())
# print(prof.__next__())
# print(prof.__next__())

# def number(n):
#     for i in range(n):
#         yield i
# num=number(10)
# a = num.__next__()
# b = num.__next__()
#     # i = i + 1
# if a == 0:
#     print(a)
# if b == 1:
#     print(b)

# from tkinter import *
# root=Tk()
# root.geometry("800x500")
# i=0
# # def num():
# #     global i
# #     a.insert(ACTIVE,f"{i}")
# #     i=i+1
#
# def number(n):
#     for i in range(1,n):
#         yield i
# num=number(100)
# def Question():
#     b=num.__next__()
#     a.insert(ACTIVE,f"{b}")
# # number=num()
# f=Frame(root,bg="grey",borderwidth=7,relief=SUNKEN)
# f.pack(side=TOP,fill="x")
# a=Listbox(f)
# a.pack(fill="x")
# a.insert(END,"This is used for ending and its compalsary put in the our listbox")
# Button(root,text="Next",borderwidth=3,command=Question).pack()
# root.mainloop()

# class Project:
#     pass
#
# class Pro(Project):
#     # def Ques(n):
#     #     for list1 in range(n):
#     #         yield list1
#     def __init__(self,exp,q,w,e):
#         self.Zero=exp
#         self.first=q
#         self.second=w
#         self.third=e
#     @classmethod
#     def detail(cls,Questions):
#         paras=Questions.split(",")
#         # print(paras[1])
#         return cls(paras[0],paras[1],paras[2],[paras[3]])
#         # return cls(*Questions.split(","))
#     @staticmethod
#     def num(n):
#         for Question in range(n):
#             yield Question
#     # number=num(10)
#     # print(number.__next__())
#     # print(number.__next__())
#     # number = num(10)
# Questions = "this is my firsts 0 , this is my second 1 ,  This is my third 2  , this is my fourth 3 "
# # numlis = Ques(Questions)
# Question=Pro.detail(Questions)
# # print(Question.Questions[1])
# print(Question.__dict__)

from tkinter import *
class Question:
    def __init__(self,a,b,c,d):
        self.Zero=a
        self.first=b
        self.second=c
        self.third=d
    @classmethod
    def detail(cls,Questions):
        return cls(*Questions.split(","))


class KBC(Tk,Question):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
    def frames(self):
        self.f=Frame(padx=5,pady=5,borderwidth=10,relief=SUNKEN)
        self.f.pack(side=TOP,fill="x")

if __name__ == '__main__':
    root=KBC()
    root.frames()
    root.mainloop()
    Questions = "this is my firsts 0 , this is my second 1 ,  This is my third 2  , this is my fourth 3 "
    Que=Question.detail(Questions)
    s= Que
    for i in s:
        print(i)

