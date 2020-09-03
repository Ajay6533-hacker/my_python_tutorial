# book = ["python ","machine learning","data structure","computer networking"]
# print(book)
# print(type(book))
# print(book[0])
# print(len(book))
# print(type(book))
# a=book[0]
# b=book[1]
# print(a + b)
# book.sort()
# print(book)
# book.append("data science")
# print(book)

numbers = [3,4,6,8,36,5]
print(len(numbers))
print(max(numbers))
print(min(numbers))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers[1])
# # nulls = numbers.clear()   #not store in any variables
# print(numbers)
#
# numbers.append(89)

numbers.insert(2,5)
print(numbers)
numbers.pop()
print(numbers)
numbers[1]=10
print(numbers)

# mutable and unmutable
# mutable =  can change
# unmutable = can not change

# tup1=( 4,56,23)
tup1=(4,)
print(type(tup1))
print(tup1)

# swap two numbers
a=4
b=5
a,b=b,a
print(b)