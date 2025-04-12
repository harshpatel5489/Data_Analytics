# 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_interger(a,b,c):
    if a==b or b==c or c==a:
        return 0
    else:
        return a+b+c
a = int(input("Enter first integer : "))
b = int(input("Enter second integer : "))
c = int(input("Enter third integer : "))

result =sum_interger(a,b,c)
print(f"The result is : {result}")
