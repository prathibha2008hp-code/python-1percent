x=10
print(type(x)) #o/p <class 'int'>
x= "hello"
print(type(x)) #o/p <class 'str'>
x=3.14
print(type(x)) #o/p <class 'float'>
x=True
print(type(x)) #o/p <class 'bool'>

a=12
b=12
print(id(a)) #o/p 140712345678912
print(id(b)) #o/p 140712345678912

a=12
b=int(input("Enter a number: "))
print(id(a)) #o/p 140712345678912
print(id(b)) #o/p 140712345678912