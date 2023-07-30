import random

options = ("rock", "paper", "scissors")

# to make the game run again
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
        
    elif player == "rock" and computer == "scissors":
        print("You win :)")
        
    elif player == "paper" and computer == "rock":
        print("You win :)")
        
    elif player == "scissors" and computer == "paper":
        print("You win :)")

    else:
        print("You loose :(")
    
    play = input("Play again? (1 - yes/0 - no) : ")
    
    if play == 0 :
        running = False

print("Thanks for playing!")