#  48) Write a Python script to sort (ascending and descending) a dictionary by value. 

d1 = {'a': 20,'b': 30,'c':40,'d':50}

asending = dict(sorted(d1.items(), key = lambda  item :item[1]))
dissending = dict(sorted(d1.items(), key = lambda  item :item[1],reverse=True))

print(f"assending : {asending}")
print(f"dissending : {dissending}")