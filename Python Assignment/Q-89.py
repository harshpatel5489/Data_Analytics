#  89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding 
# snippets.

"""
try: Yahan wo code likhte hain jo error de sakta hai.

except: Agar error aata hai to usse yahan handle kiya jaata hai.

finally: Yeh block hamesha execute hota hai — chahe error aaye ya na aaye.
"""

""" 
try: Yahan wo code likhte hain jo error de sakta hai.

except: Agar error aata hai to usse yahan handle kiya jaata hai.

finally: Yeh block hamesha execute hota hai — chahe error aaye ya na aaye.

"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("0 se divide nahi kar sakte")
except ValueError:
    print("Sirf number daalo")
finally:
    print("Try-Except-Block khatam ho gaya")
