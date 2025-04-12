# 74) Write a Python program to read first n lines of a file. 

def read_lines(file_name,n):
    with open(file_name,"r") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line,end="")

file_name = "new.txt"
n= 1
read_lines(file_name,n)