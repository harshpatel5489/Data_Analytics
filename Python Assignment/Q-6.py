# 6) Write a Python program to get the  Fibonacci series of given range. 

n = int(input("Enter a number : "))
a,b= 0,1
print(a,end=" ")
print(b,end=" ")

for j in range (2,n):
    a,b = b,a+b
    print(b,end=" ")