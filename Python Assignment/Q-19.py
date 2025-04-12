# 19) Write a Python program to count the occurrences of each word in a given sentence.

string = input("Enter a string : ")
s1 = string.split()
s2 ={}
for i in s1:
    if i  in s2:
        s2[i] +=1
    else:
        s2[i] = 1


print(s2)