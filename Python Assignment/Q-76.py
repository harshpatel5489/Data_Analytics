# 76) Write a Python program to read a file line by line and store it into a list 
def l1(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

file_name = 'new.txt'
lines = l1(file_name)
print(lines)
