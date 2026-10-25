print("hello world")
print(10)
print(23+90)
print("I am learning python")

#printing different data types

print(43)#int
print(3.14)#float
print(True)#boolean
print("hello world")#string

#full powers of print function
# 4 important parameters of print function
#print(*objects , sep ='',end ='\n', file=sys.std.out,flush =False)

 #sep
print("java","python","c") #output java python c
print("java","python","c",sep = ',')#output java,python,c
#note observe that if we didnot pass anything to the sep paramerter default is space
print("java","python","c",sep = '|')#output java|python|c
print(25,10,2026,sep ='-')#output 25-10-2026
#end
#by default the end has '\n' 
print("hello",end ='_')
print("this",end='_')
print("is",end ='_')
print("prathibha")
print("and see iam not using the end ='_' here so it printing to the next line ")
#output 
""" hello_this_is_prathibha
and see iam not using the end ='_' here so it printing to the next line 
 """
#file
with open("examplefileforfileparameter.txt",'w')as f:
    print("app started",file = f)
    print("user loged in",file = f)
# if we want to print the output in a file instead of screen we can  use this
# flush
#python sometimes holds output in buffer.flush = True froces it out instantly
import time
print("step 1...", flush=True)
time.sleep(1)
print("step 2...", flush=True)
time.sleep(1)
print("done!.", flush=True)
#output
"""  hello_this_is_prathibha
and see iam not using the end ='_' here so it printing to the next line 
 """
print("step 1...", flush=True)
time.sleep(1)
print("step 2...", flush=True)
print()
time.sleep(1)
print("done!.", flush=True)
#output
""" step 1...
step 2...

done!. """
print("="*34) #output ==================================
print(""" 
==================================
welcome to pyhton
==================================
""")
#repr - hidden characters in a string like \n,\t will be visible when we use repr function
text = "hello\tworld\n"
print(text) #output hello	world
print(repr(text)) #output 'hello\tworld\n'
#input function
#input function is used to take input from the user
name = input("enter your name")
#input always returns a string
age = input("enter your age")
print(type(age)) #output <class 'str'>
# so we have to do type converstion
age = int(input("enter your age"))
print(type(age)) #output <class 'int'>
#input teaches you to concept ot reciving the external data . the concept is same everywhere only source changes
#example
#terminal input
name = input("enter a name:")

#web API input
#name = request.json["name"]

#command line input
import sys
name = sys.argv[1]
print(f"hello,{name}")

""" name = sys.argv[1]
           ~~~~~~~~^^^
IndexError: list index out of range """
# we if run as it is we we end up with an error
#so pyhton3 firstcode.py prathibha
#output
#hello prathibha

#environmnet varialble input
import os
name = os.environ.get("APP_NAME")
