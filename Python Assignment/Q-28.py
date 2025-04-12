# 28) Differentiate between append () and extend () methods? 


"""
1. Append() Method:
Kaam: append() method ek single item ko list ke end mein add karta hai.

Syntax: list.append(4)
output = [1,2,3,4]

Important Point: jab ham append ke andar multiple value dalege tabhi woh list k andar multiple
 list banake ke dega 

Syntax: list.append(5,6)
output = [1,2,3,4,[5,6]]


2. Extend() Method:
Kaam: extend() method ek list ke elements ko doosri list ke elements ke saath combine karta hai. Yeh ek baar mein ek se zyada elements ko list ke end mein add karta hai.

Important Point: extend() method ko iterable object (jaise list, tuple, string) ke saath use 
karna padta hai. Yeh list ke elements ko separate items ke roop mein add karta hai.

Syntax: list.extend(5,6)
output = [1,2,3,4]

"""
