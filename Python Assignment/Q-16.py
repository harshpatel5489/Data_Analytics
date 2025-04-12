# 16) Write a Python program to count the number of characters 
# (character frequency) in a string 


def chara(c):
    count = {}
    for char in c:
        if char in count:
            count[char] += 1
        else:
            count[char] =1
    return count
user = input("Enter a string : ")
result = chara(user)
print(result)