# 35) Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30. 

square =[i**2 for i in range(1,30)]
sq1 = square[:5]
sq2 = square[-5:]
result = sq1+sq2
print(result)


