# 45) Write a Python program to unzip a list of tuples into individual lists. 

t1 = [(1,"harsh"),(2,"raj")]
l1,l2 = zip(*t1)
print(list(l1))
print(list(l2))
