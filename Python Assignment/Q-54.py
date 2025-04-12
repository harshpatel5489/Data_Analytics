# 54) Write a Python program to check multiple keys exists in a dictionary

d1 = {
    1 : "jay",
    2 : "mit",
    3: "raj",
    4 : "jay",
    5 : "mit",
    6: "raj"
}
d2 = [2,3,4]

if all(key in d1 for key in d2):
    print("keys exist in the dictionary.")
else:
    print("One or more keys do not exist in the dictionary.")