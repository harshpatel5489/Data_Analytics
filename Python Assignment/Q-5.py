# 5) Write a Python program to get the Factorial number of given numbers. 

num = int(input("Enter a number : "))
factorils = 1
for i in range(1,num+1):
    factorils *=i
print(f"{num} factorial is {factorils}")