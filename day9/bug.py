#zero division error
result = 10 / 0  # ZeroDivisionError
#float_division = 10 / 3  # 3.3333333333333335
if 0.1 + 0.2 == 0.3:  # This will NOT execute
    print("Equal")
#integer division
if abs((0.1 + 0.2) - 0.3) < 0.0001:
    print("Close enough")
    age = input("Enter age: ")  # This is a string
    #mixing types unknowingly can lead to errors. For example, if you try to add an integer to a string, you'll get a TypeError.
age = int(age)  # Convert the string to an integer
print(age + 1)  # This will now work correctly