# 75) Write a Python program to read last n lines of a file. 

def read_lines(file_name, n):
    with open(file_name, 'r') as file:
        return ''.join(file.readlines()[-1])

file_name = 'new.txt'
n = 5
print(read_lines(file_name, n))
