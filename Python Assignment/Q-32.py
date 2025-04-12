# 32) Write a Python program to remove duplicates from a list. 

l1 = [11,12,11,13,14,15]
new_list = []
[new_list.append(item)for item in l1 if item not in new_list]
print(new_list)