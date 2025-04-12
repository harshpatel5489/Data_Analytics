# 79) Write a Python program to count the number of lines in a text file. 

def count_lines(file_name):
    with open(file_name, 'r') as file:
        return len(file.readlines())


file_name = 'new.txt'
print(count_lines(file_name))
