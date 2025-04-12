# 87) When is the finally block executed? 


"""finally block hamesha execute hota hai — chahe try block mein exception aaye ya na aaye.

Iska use hota hai cleanup operations ke liye: jaise file close karna, database connection 
band karna, etc.

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("0 se divide nahi kar sakte")
finally:
    print("Program khatam ho gaya (finally block)")


"""