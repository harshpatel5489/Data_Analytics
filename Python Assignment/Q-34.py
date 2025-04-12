# 34) Write a Python function that takes two lists and returns true if they 
# have at least one common member. 

def l1(a,b):
    for i in a:
        if i in b:
            return True
        else:
            return False
a = [10,20]
b = [1,50]
print(l1(a,b))