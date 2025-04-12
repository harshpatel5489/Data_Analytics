# Write a python program to sum of the first n positive integers.
def number(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

n = int(input("Enter a number : "))
print(number(n)) 