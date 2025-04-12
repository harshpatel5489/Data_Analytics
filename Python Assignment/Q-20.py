#Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string. 

def string(str1,str2):
    string1 = str2[:2] + str1[2:]
    string2 = str1[:2] + str2[2:]
    return string1+" "+string2
str1 = input("Enter a string : ")
str2 = input("Enter a string : ")
result = string(str1,str2)
print(result)