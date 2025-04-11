
import random

def roll_dice():
    # Simulate a dice roll (values between 1 and 6)
    return random.randint(1, 6)

def game():
    player1_score = 0
    player2_score = 0
    
    # Start the game only when dice roll is 6
    print("Rolling to start the game...")
    while True: 
        # First, roll the dice
        roll = roll_dice()
        print(f"Rolled: {roll}")
        
        # Game starts if the roll is 6
        if roll == 6:
            print("Game starts! Player 1 goes first.")
            break
    
    # Game loop
    while player1_score < 100 and player2_score < 100:
        # Player 1's turn
        input("Player 1, press Enter to roll the dice.")
        roll = roll_dice()
        print(f"Player 1 rolled: {roll}")
        player1_score += roll
        print(f"Player 1's score: {player1_score}")
        
        # Check if Player 1 wins
        if player1_score >= 100:
            print("Player 1 wins with 100 points!")
            break
        
        # Player 2's turn
        input("Player 2, press Enter to roll the dice.")
        roll = roll_dice()
        print(f"Player 2 rolled: {roll}")
        player2_score += roll
        print(f"Player 2's score: {player2_score}")
        
        # Check if Player 2 wins
        if player2_score >= 100:
            print("Player 2 wins with 100 points!")
            break

# Start the game
game()

