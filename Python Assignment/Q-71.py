
# 71) What is File function in python? What are keywords to create and write file. 
"""

Python me file handling ka use data ko read, write, append aur modify karne ke liye hota hai. 
File operations ke liye open(), read(), write(), close() jaise functions ka use kiya jata hai.


"r"	Read Mode (Default)
"w"	Write Mode (File create karega, agar exist karega to overwrite karega)
"a"	Append Mode (Naya data add karega bina delete kiye)
"x"	Create Mode (Agar file exist karegi to error dega)

"""

file = open("new.txt","w")    # File Create Karne Ke Liye:
file.close()

#  File Me Data Write Karne Ke Liye:

file = open("new.txt", "w")  
file.write("Hello, this is Python!")  
file.close()  

file = open("new.txt", "a")  
file.write("\nThis is new content added.") # File Me Data Append Karne Ke Liye:
file.close()  

file = open("new.txt", "r")  
print(file.read())  #File Read Karne Ke Liye:
file.close()  
