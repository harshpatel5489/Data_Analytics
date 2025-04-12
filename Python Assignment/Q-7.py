# 7) How memory is managed in Python? 

"""
in python memory managment is a automatically,which make it easier for developer.
you dont need to manually manage a memory like in some other programming launguage (c,c++)

How Python Manages Memory:

1. Automatic memory allocation : 
when you are creating variable and object that time python automatically reserved a memory for it:

ex = 

a = 5

2 . garbage collection :

python has a built in garbage collector. this mean is automatically remove object or variable unused memory
 to free up space

ex = 
x = 10   # Memory is allocated to store the value 10
x = 20   # Memory for 10 is freed, and new memory is allocated for 20

3. Reference Counting: Python keeps track of how many references (or links) there are to an object.\
When there are no references to an object anymore, it’s automatically cleaned up by the garbage collector.

a = [1, 2, 3]   # List object is created and memory is allocated
b = a           # Now, 'a' and 'b' both reference the same list
del a           # 'a' no longer references the list, but 'b' still does


"""