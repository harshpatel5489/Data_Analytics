# 29) Write a Python function to get the largest number, smallest num 
# and sum of all from a list. 


def number(a):
    largest = max(a)
    smallest = min(a)
    sum1 =sum(a)
    return largest,smallest,sum1
num = [10,20,30,40,50]
print(number(num))