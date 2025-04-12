# Write a Python program that will return true if the two given 
# integer values are equal or their sum or difference is 5. 

def check(a,b):
    if a == b or a + b == 5 or abs(a-b) == 5:
        return True
    return False
a=4
b = 8
print(check(a,b))