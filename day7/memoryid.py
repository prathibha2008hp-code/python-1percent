a=12
b=12

print(id(a)) #o/p 140712345678912
print(id(b)) #o/p 140712345678912
c=[1,2,3]
d=[1,2,3]
print(id(a)) #o/p 2150560684672

print(id(b)) #o/p 2150562317248
#note: The id of a and b are different because they are list objects and each list object has its own unique id.
#  However, the id of a and b are the same
#  because they are both integers with the same value, and Python caches small integers for performance reasons.
print(a is b) #o/p True
print(c is d) #o/p False
print(a == b) #o/p True
print(c == d) #o/p True

a = [1, 2, 3]

b = a

b.append(4)

print(a)#o/p [1, 2, 3, 4]
print(b)#o/p [1, 2, 3, 4]
a = [1, 2, 3]
b = a

print(a is b) #o/p True
print(id(a) == id(b))#o/p True

a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)#o/p [1, 2, 3]
print(b)#o/p [1, 2, 3, 4]

print(a is b)#o/p False
print(id(a) == id(b))#o/p False
