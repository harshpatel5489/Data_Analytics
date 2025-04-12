#  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return 
# instead of the empty string.

string = input("Enter a string : ")
if len(string) <= 2:
    string = ("")
else:
    string = string[:2] + string[-2:]
    print(string)