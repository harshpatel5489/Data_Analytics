import random

IPL = ["MI","CSK","GT","KKR","RCB"]
menue = """
            welcome to IPL 2025

            TOP 6 TEAMS ARE :
"""
print(menue)
for ipl_team in IPL:
    print(ipl_team,end=" | ")
print()
first_team = input("Enter your Team :").upper()
opp_team = random.choice(IPL)
print(f"Your team = {first_team}")
print(f"Opp_team = {opp_team}")

while first_team == opp_team:
    opp_team = random.choice(IPL)

toss_time = input("press H for head and T for tail : ").upper()

if first_team == 'h':
    print(f"Your choice is Head")
else:
    print("Your choice is TAIL")

toss = ["Head","Tail"]
actual_toss = random.choice(toss)
if first_team == actual_toss[0]:
    print(f"{first_team} won the toss")
else:
    print(f"{opp_team} won the toss")




