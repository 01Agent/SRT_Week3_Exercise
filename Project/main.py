import math_operations 
from string_operations.concatenation import concat
from string_operations.case_conversion import to_lowercase,to_uppercase

x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))

print (f'the sum of 2 number is: {math_operations.add(x,y)}')

print (f'the subtration of 2 number is: {math_operations.subtract(x,y)}')

print (f'the multiplication of 2 number is: {math_operations.multiply(x,y)}')

print (f'the division of 2 number is: {math_operations.divide(x,y)}')

String1 = input("\nEnter the String 1: ")
String2 = input("Enter the string 2: ")

print (f'The concate String is: {concat(String1,String2)}')

Uppercase = input("\nEnter the string you want to uppercase: ")
print(f'The new Uppercase string is: {to_uppercase(Uppercase)}')

Lowercase = input("\nEnter the String you want to lower case:")
print(f'The new lowercase string is: {to_lowercase(Lowercase)}')