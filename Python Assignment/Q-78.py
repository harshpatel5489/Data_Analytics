# 78) Write a python program to find the longest words. 
def long(a):
    max_len = max(len(word)for word in a)
    long_word = [word for word in a if len(word) == max_len]
    return long_word

l1 = ["harsh","jay","het"]
print(long(l1))