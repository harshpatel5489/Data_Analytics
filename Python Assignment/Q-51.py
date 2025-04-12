# 51) How Do You Traverse Through a Dictionary Object in Python?

d1 =  {"a":555,"b":666,"C":777,"D":888}
for k in d1.keys():
    print(k)
print("-----------------------")
for v in d1.values():
    print(v)
print("-----------------------")

for k,v in d1.items():
    print(f"{k} = {v}")