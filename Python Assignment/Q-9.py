"""a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
temp = a
a = b
b = temp
print(f"first number a : {a}",)
print(f"second number b : {b}",)"""

a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))

a = a+b
b = a-b
a = a-b
print(f"first number a : {a}",)
print(f"second number b : {b}",)