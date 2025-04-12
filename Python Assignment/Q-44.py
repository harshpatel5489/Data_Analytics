# 44) Write a Python program to create a tuple with different data types. 

t1 = (2,3.14,True,"harsh",(5,6,7),["harsh","patel"],{1 :("harsh")},{1,2,3})
for i in t1:
    print(f"{i} = {type(i)}")