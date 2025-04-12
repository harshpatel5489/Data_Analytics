#  Write a Python function to reverses a string if its length is a multiple of 4.

def rev(mit):
    if len(mit) % 4 == 0:
        return mit[::-1]
    else:
        return mit
print(rev("jaya"))


