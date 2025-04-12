# 70) How will you randomize the items of a list in place? 

import random

def func(a):
    random.shuffle(a)
    return a
l1 = [10,20,30,40,50,60]
print(func(l1))