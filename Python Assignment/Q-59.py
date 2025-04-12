# #  59) Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.

user = "harsh"
dic = {}

for char in user:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
print(dic)
print("------------------------------------------------")
print(len(user))