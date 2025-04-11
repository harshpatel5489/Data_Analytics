import random

def game(user,computer):
    print(f"user choice : {user_choice}")
    print(f"computer choice : {computer_choice}")
    if user_choice == computer_choice:
        return "**** TIE ****"
    elif user_choice == "ROCK" and computer_choice == "PAPER":
        return "**** COMPUTER WON THE MATCH ****"
    elif user_choice == "ROCK" and computer_choice == "SCISSOR":
        return "**** USER WON THE MATCH ****"
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        return "**** USER WON THE MATCH ****"
    
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        return "**** USER WON THE MATCH ****"
    elif user_choice == "PAPER" and computer_choice == "SCISSOR":
        return "**** COMPUTER WON THE MATCH ****"
    elif user_choice == "SCISSOR" and computer_choice == "ROCK":
        return "**** COMPUTER WON THE MATCH ****"
    elif user_choice == "SCISSOR" and computer_choice == "PAPER":
        return "**** USER WON THE MATCH ****"
    

game_list = ["ROCK","PAPER","SCISSOR"]

menue = """
             MENU

            ROCK
            PAPER
            SCISSOR


"""

status = True
while status:
    print(menue)

    user_choice = input("Enter your choice :").upper()
    computer_choice = random.choice(game_list)

    result = game(user_choice,computer_choice)
    print(f"Result : {result} \n ")

    game_choice = input("Do you want to play again press 'y' for yes and press 'n' for ")
    if game_choice == "y" or game_choice == "yes":
        status = True
    else:
        status = False