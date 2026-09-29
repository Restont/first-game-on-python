import random

wins = 0
losses = 0

while True:
    my_choice = input("rock, paper, scissors: ").lower().strip()
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if my_choice not in options:
        print("I don't know that, try again")
        continue

    if my_choice == computer:
        print("Draw!")
    elif my_choice == "rock" and computer == "scissors":
        print("You win!")
        wins += 1
    elif my_choice == "paper" and computer == "rock":
        print("You win!")
        wins += 1
    elif my_choice == "scissors" and computer == "paper":
        print("You win!")
        wins += 1
    else:
        print("Computer wins!")
        losses += 1

    if wins >= 3:
        print(f"You won the game! Wins: {wins}, losses: {losses}")
        break
    if losses >= 3:
        print(f"You lost! Wins: {wins}, losses: {losses}")
        break