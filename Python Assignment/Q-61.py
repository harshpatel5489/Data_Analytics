# 61) Write a Python function to calculate the factorial of a number (a 
# nonnegative integer)

def factorial(num):
    fact = 1 
    for i in range(1,num+1):
        fact *= i
    return fact
number = int(input("Enter a number : "))
print(factorial(number))