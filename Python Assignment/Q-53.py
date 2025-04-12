# 53) Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
d1 = {
    1 : "jay",
    2 : "mit",
    3: "raj",
    4 : "jay",
    5 : "mit",
    6: "raj",
    7 : "jay",
    8 : "mit",
    9: "raj",
    10 : "jay",
    11 : "harry",
    12 : "mit",
    13: "raj",
    14 : "jay",
    15: "mit",
    16: "raj",
    17 : "harsh"
}

for key,values in d1.items():
    if key <= 15:
        print(key,":",values)
