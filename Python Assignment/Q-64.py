# 64) Write a Python function that checks whether a passed string is 
# palindrome or not 

def name(a):
     if a[::-1] == a[:]:
         return "palindrome "
     else:
         return "Not palindrome "
char = input("Enter a palindrome name : " )
print(name(char))


