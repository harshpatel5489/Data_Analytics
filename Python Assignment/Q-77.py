# 77) Write a Python program to read a file line by line store it into a variable. 

def variable(file_name):
    with open(file_name, 'r') as file:
        return ' '.join([line.strip() for line in file])  # Join lines into a single string without newlines

file_name = 'new.txt'
content = variable(file_name)
print(content)
