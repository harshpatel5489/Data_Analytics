# 63) Write a Python function to check whether a number is perfect or not. 

def num(a):
    if a == 20:
        return "Number is perfect"
    else:
        return "Number is not Perfect"
number = int(input("Enter a number :"))
print(num(number))