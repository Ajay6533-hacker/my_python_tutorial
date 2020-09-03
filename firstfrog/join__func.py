# list1=["ajay","vijay","vijay","aman","nitish","rohan"]
# for item in list1:
#     print(item,"kumar",end=" ")
# a=" kumar  ".join(list1)
# print(a)

# ---------------------------------------------Join function 2 ---------------------------------------------------------
# list2=["vijay","ajay","deepak","rahul"]
# b=" malhotra ".join(list2)
# print(b)
# list3=["vijay","ajay","deepak","rahul"]
# list3[1]="ajay malhotra"
# print(list3)
def list1():
    a={"fruits":"mango","vegitables":"potato","transport":"bus","city":"delhi"}
    for index,(item,value) in enumerate(a.items()):
        if index %2!=0:
            print(item,value)

def use_func(normal,*args,**kwargs):
    print(args)
    for index,(item,value) in enumerate(kwargs.items()):
        if index%2==0:
            print(f"{item} is {value}")
    print(normal)
list2=["ajay","vijay","deepak","saurabh","rahul"]
simple="this is usd for specially for normal arguement"
list3={"me":"ajay","brother":"vijay","friend":"deepak"}

container=[list1(),use_func(simple,*list2,**list3)]
i=1
for item in container:
    if i%2==0:
        print(item)
        i=i+1
# use_func(simple,*list1,**list2)

# a=["this","me"]
# b="this is used second join function"
# c="my name is ajay".join(a)
# print(c)


