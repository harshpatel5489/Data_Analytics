# 49) Write a Python script to concatenate following dictionaries to create a new one.

l1 = {"a":5,"b":6}
l2 = {"c":7,"d":8}
new_dic = {**l1,**l2}
print(f"concatenate : {new_dic}")