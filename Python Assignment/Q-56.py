#56) Write a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1 ={'a': 400, 'b': 400}
d2 = {'d': 400, 'c': 300}
d1.update(d2)
print(d1)