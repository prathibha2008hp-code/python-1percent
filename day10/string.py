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


""" name1= "prathi"
name2 = "gagany"
if name1==name2:
    print("true")
else:
    print("flase")name = "aabccc"
count ={}

 """
""" my_string ="hello"
print(id(my_string))
my_string= "jello"
print(id(my_string))
print(my_string) """
""" string = "name"
count = 0
for ch in string:
    if ch in "aeiou":
        count+=1
print(count)
 """
""" name = "string"
rev = ""
for ch in name:
    rev = ch +rev
print(rev) """
""" for ch in name:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count) """
""" phrase_sting = "never put off for tomrrow,what can you do today"
phrase_sting = phrase_sting.replace(" ","")
print(phrase_sting) """
""" phrase_sting = "never put off for tomrrow,what can you do today"
input_char = input("enter the character to find the location and character:")
for index in range(len(phrase_sting)):
    if phrase_sting[index] == input_char:
        print(f"{input_char} is found at index {index}") """
        #using enumaration
""" phrase_sting = "never put off for tomrrow,what can you do today"
input_char = input("enter the character to find the location and character:")
for index,letter in enumerate(phrase_sting):
    if input_char == letter:
        print(f"given chracter {input_char} is at the index {index} position")
 """
""" task = "this-ifun-has-to-separted-by-space"
print(task.replace("-" ," ")) """
""" college_name = "alvas@###$c%0llege#at$%moodabidri!@"
unwanted_chars = "!@#$%^&*()"
cleaned_str = " "
for char in college_name:
    if char not in unwanted_chars:
        cleaned_str+=char
print(cleaned_str) """
""" college_name = "alvas@###$c%0llege#at$%moodabidri!@"
cleaned_str = college_name.replace("%0", "o")
for ch in "@#%$!":
    cleaned_str = cleaned_str.replace(ch, " ")
cleaned_str = " ".join(cleaned_str.split())
print(cleaned_str)
 """
""" a = [2,4,5,3,2]
a = [2,4,5,3,2]
print(a ==a)
print(a is a)
 """
""" python_exam = [("manju",["python","maths","phy","AI","ML"]),
               ("rathan",["ml","dbms","python","ec","java"]),
              ("raman",["pyhton","c","c++","maths","AI","neo"]) ]
for name ,subjects in python_exam:
    if "python" in subjects:
        print(name) 
names = ["banana", "apple", "cherry"]
names.sort()
print(names)  """
nums = [5, 2, 9, 1, 3]

""" n = len(nums)

for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            # swap
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted list:", nums) """
readings = ["25.6","28.1","37.8c","error","41.1c"]







   

        


    
