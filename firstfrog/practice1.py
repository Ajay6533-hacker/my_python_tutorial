
list1=[["ajay",56],["vijay",7],["sanajay",7],["deepak",9]]
dict1=dict(list1)
#print(dict1)


# for item,flower in list1:
#     print(item ,flower)


"""
for ajay,flowers in dict1.items():
    print(ajay,flowers)
"""
# print(item,"have number of flowers","flowers",flowers)

# item=[int,float,"ajay",78,36,58,30,56,23,21,3,]
# for items in item:
#     if str(items).isnumeric() and items>30:
#         print(items)

               #  while loop

# i=0
# while(i<60):
#     i=i+1
#     if i==65:
#         print(i+1,end=" ")
#         continue
#         print(i,end=" ")
#     if 60>1:
#         print('ajay')
#         break
# print("deepak")


                               # break statement
"""
i=0
while(True):
    if i<7:
        i=i+1
        print(i,end=" ")
        break
print("deepak")

     #if i>6:
        # print("no")"""

                   # continue statement

# i=9
# while(True):
#     if i<=10:
#         i=i+1
#         print("It is a continue statement")
#         continue
#     print("yes")
#     break


while(True):
    inp=int(input("enter a number"))
    if inp>100:
        print("your input are greaterr than 100")
        break
    else:
        print('try again')
        continue
        




