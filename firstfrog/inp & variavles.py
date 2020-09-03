#  we are easily understand variables , type casting , concatenate , types of variables

# var1=" Ajay "
# var2 = " programmer"
# print(" concatenate of two string characters",var1+var2)

# var3 = 45
# var4 = 48.3
# print("sum of two numbers", var3 + var4)

# print("sum of integer and a string", var1+ str(var3))
# print("sum of two numbers is", var3+var4)

# var5 = "4"
# var6 = "5"
# print(int(var5)+int(var6))

# print("type of var5", type(var5))
# print("type of var3", type(var3))
# print("type of var4", type(var4))

# print("Enter your first number: ")
# # input1 = input()
# input1 = float(input())
# print(" Enter your second number: ")
# # input2=input()
# input2=float(input())
# # print("Sum of two numbers", int(input1)+ int(input2))
# print("Sum of two numbers", input1+ input2)

print(" Find the percentage of  five given subjects of marks and 100 marks/per subjects")
subj1 = int(input(" enter your first subject of number \n"))
subj2 = int(input(" Enter your second subjecty of numbers \n"))
subj3 = int(input(" Enter your third subjecty of numbers \n"))
subj4 = int(input(" Enter your fourth subjecty of numbers \n"))
percentage = int((subj1+subj2+subj3+subj4)*100/400)
print("total number of all subjects of percentage",percentage ,"%")