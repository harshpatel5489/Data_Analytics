# 62) Write a Python function to check whether a number is in a given range 

def check(a):
    if a > 0 and a <= 10:
        return "In range"
    else:
        return "out of range"

number = int(input("Enter a number : "))
print(check(number))