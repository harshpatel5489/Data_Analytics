#36) Write a Python function that takes a list and returns a new list with unique elements of the first list.

def l2(a):
    a = set(l1)
    return a
l1 = [10,20,30,10,40]
print(l2(l1))