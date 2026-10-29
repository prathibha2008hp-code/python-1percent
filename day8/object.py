x=10;
print(type(x)) #o/p <class 'int'>
print(x) #o/p 10
print(id(x)) #o/p 140712345678912
""" object:
type
 value
   idendentity 
    these are the three properties of an object in python"""
a=12
b=12
print(id(a)) #o/p 140712345678912
print(id(b)) #o/p 140712345678912
print(a is b) #o/p True

a=12
b=int(input("Enter a number: "))
print(id(a)) #o/p 140712345678912
print(id(b)) #o/p 140712345678912
print(a is b) #o/p False

""" one important concept  when a=12 and b=12 have the same memory address 
but when we take input from user and assign it to b then a and b have different
 memory address because python caches small integers for performance reasons.
 if will happens wiht immuable objects like int, float, str, tuple but not with mutable objects like list, dict, set"""