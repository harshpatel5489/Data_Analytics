
# 57) Write a Python program to find the highest 3 values in a dictionary 

d1 = {'a':100,'b':200,'c':20,'d':40}
d1 = list(d1.values())
print(d1)

max1 = max(d1)
d1.remove(max1)

max2 = max(d1)
d1.remove(max2)

max3 = max(d1)

print(f"{max1},{max2},{max3}")