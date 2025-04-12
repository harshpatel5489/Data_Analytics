# 41) Write a Python program to check whether a list contains a sub list

def lis(l1,l2):
    for i in l2:
        if i in l1:
            return True
            
        else:
            return False

l1 = [10,20,30,40,50]
l2 = [10,20]
print(lis(l1,l2))