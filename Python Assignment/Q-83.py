# 83) Explain Exception handling? What is an Error in Python? 

"""
Explain Exception handling -
Exception handling ek technique hai jiska use hum program mein hone wale unexpected errors ko handle karne ke liye karte hain.
Jab program run hota hai aur koi error aata hai, to Python ek "exception" throw karta hai.

Agar hum exception ko handle nahi karte, to program crash kar jaata hai. Isliye hum try-except
ka use karke in errors ko safely handle karte hain.
"""

"""
Error matlab program mein aayi koi galti jo program ke execution ko rok sakti hai.

Python mein mainly 3 types ke errors hote hain:

1) Syntax Error : Jab code likhne mein galti hoti hai

2) Runtime Error : Jab program chalate waqt error aata hai

3) Logical Error : Jab output galat milta hai par koi error message nahi dikhta


"""

"""
Exception Handling ka Syntax
try:
    # yaha code likhte hain jisme error aa sakta hai
except:
    # error hone par kya karna hai, ye likhte hain
else:
    # agar error nahi aata to ye part chalega
finally:
    # ye block hamesha chalega, chahe error aaye ya na aaye"""
