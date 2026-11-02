#strings are immutable
string = "python"
#print(string[0]="J") #TypeError: 'str' object does not support item assignment
string = "python"
print(string[-1]) #n
print(string[-6]) #p
#string slicing
print(string[0:3]) #pyt
print(string[3:6]) #hon
print(string[0:6:2]) #pto
print(string[::2]) #pto
print(string[0:6:1]) #python
print(string[::-1]) #nohtyp
#string slicing creates a new object
word = "incredible"
after_slicing = word[0:5] #incred
print(id(after_slicing) is id(word)) #False
print(id(after_slicing == id(word))) #False

# length function
print(len(word)) #9
#fstring
a = "asdas"
b = 3
print(f"{a} divided by {b} is {a / b}")
# 10 divided by 3 is 3.3333333333333335
#formating string
price = 49.99
tax = price * 0.18
total = price + tax

print(f"Price: {price:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {total:.2f}")
#Padding and alignment
print(f"Price: {price:>10.2f}")
print(f"Tax: {tax:>10.2f}")
print(f"Total: {total:>10.2f}")
last = "centDev"
full = first + last
print(full)  # OnePercentDev
#string methods
name = "  OnePercentDev  "
cleaned = name.strip()

print(name)     # "  OnePercentDev  " (unchanged)
print(cleaned)  # "OnePercentDev"     (new string)
#case conversion
text = "python for 1% developers"

print(text.upper())       # PYTHON FOR 1% DEVELOPERS
print(text.lower())       # python for 1% developers
print(text.title())       # Python For 1% Developers
print(text.capitalize())  # Python for 1% developers
