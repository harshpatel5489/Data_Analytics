name = input("Enter your name :")
gender = input("Enter your gender :")
if gender =="MALE" or gender =="male" or gender =="FEMALE" or gender =="female":
    print("valid gender")
    
else:
    print("Invalid gender")
    gender =input("Enter valid gender :")
age = int(input("Enter your age :"))
print("")
product = input("Enter your product :")
gram =  int(input("Enter your gram :"))
current_gold_price = 5752 # (1 grm)
print("")
print("--------------------------------------")
gold_rate = current_gold_price*gram
print(f"TOTAL GOLD RATE : {gold_rate}")
print("")
make_charge = gram * 845
print("")
print(f"Making charges 1gram  : 845")
print(f" Total Making Charges : {make_charge} ")
print("")
print("--------------------------------------")
total_amount = gold_rate + make_charge
print(f"TOTAL AMOUNT : {total_amount}")

if gender == "MALE" or gender ==  "male":
    if age > 65:
        if total_amount > 21000 and total_amount < 31000:
            discount = 20
            print(f"DISCOUNT : 20")
        elif total_amount > 31000 and total_amount < 51000:
            discount = 30
            print(f"DISCOUNT : 30%")
        elif total_amount >= 51000:
            discount = 35
            print(f"DISCOUNT : 35%")
    else:
        if age < 65:
            if total_amount > 21000 and total_amount < 31000:
                discount = 10
                print(f"DISCOUNT : 10%")
            elif total_amount > 31000 and total_amount < 51000:
                discount = 20
                print(f"DISCOUNT : 20%")
            elif total_amount >= 51000:
                discount = 25
                print(f"DISCOUNT : 25%")
elif gender == "FEMALE" or gender == "female":
    if age > 65:
        if total_amount > 21000 and total_amount < 31000:
            discount = 25
            print(f"DISCOUNT : 25%")
        elif total_amount > 31000 and total_amount < 51000:
            discount = 35
            print(f"DISCOUNT : 35%")
        elif total_amount >= 51000:
            discount = 40
            print(f"DISCOUNT : 40%")
    else:
        if age < 65:
            if total_amount > 21000 and total_amount < 31000:
                discount = 15
                print(f"DISCOUNT : 15%")
            elif total_amount > 31000 and total_amount < 51000:
                discount = 25
                print(f"DISCOUNT : 25%")
            elif total_amount >= 51000:
                discount = 30
                print(f"DISCOUNT : 30%")
else:
    print("Invalid Gender")  

discount = total_amount*discount/100
dis_amount = total_amount - discount
print(f"DIS- AMOUNT : {discount}")     
print("----------------------------------------------------")
print(f"total net amount : {dis_amount}")