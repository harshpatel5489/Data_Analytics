# 82) Write a Python program to copy the contents of a file to another file. 


def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            dest.write(src.read())

# Example usage
source_file = 'Q-82.2.txt'
destination_file = 'Q-82.txt'
copy_file(source_file, destination_file)
