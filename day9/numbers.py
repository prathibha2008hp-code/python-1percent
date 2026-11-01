print(0.2+0.1) # 0.30000000000000004
print(round(0.2+0.1,2)) # 0.3
#round of 0.5 is 0 and round of 1.5 is 2. This is because python uses round half to even strategy.
print(round(0.5))   # 0  (not 1!)
print(round(1.5))   # 2
print(round(2.5))   # 2  (not 3!)
print(round(3.5))   # 4
#here we are using round function to round the value to 2 decimal places.
#for financial applications, we can use the decimal module to avoid floating point errors.
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
#float division
print(5/2)  # 2.5
#even if both the numbers are integers, the result will be a float.
#floar division
print(7 // 2)    # 3
print(-7 // 2)   # -4 (rounds toward negative infinity, not toward zero)
print(7/3)# 2.3333333333333335
#modulus operator
print(10 % 3)    # 1
print(15 % 5)    # 0
#agmented assignment operators


x += 3     # same as x = x + 3  → x is now 13
x -= 2     # same as x = x - 2  → x is now 11
x *= 4     # same as x = x * 4  → x is now 44
x /= 2     # same as x = x / 2  → x is now 22.0
#abs() function
print(abs(-10))    # 10
print(abs(10))     # 10
print(abs(-3.5))   # 3.5
print(abs(0))      # 0
#built in numeric functions
list_of_numbers = [1, 2, 3, 4, 5]
print(max(list_of_numbers))  # 5
print(min(list_of_numbers))  # 1
print(sum(list_of_numbers))  # 15
