# 86) Can one block of except statements handle multiple exception? 

"""
Python mein ek hi except block ke through multiple exceptions ko handle kiya ja
sakta hai.

Iske liye hum exceptions ko tuple (brackets mein comma se separated) ke roop mein likhte hain.
Agar try block mein diye gaye kisi bhi error type ka exception aata hai, to same except block 
chalega.

try:
    # code jo error de sakta hai
except (TypeError, ValueError, ZeroDivisionError):
    print("Koi error aaya jo handle ho gaya.")


"""