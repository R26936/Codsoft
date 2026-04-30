import random

def game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0

    while True:
        user = input("Enter rock/paper/scissors (or quit): ").lower()

        if user == "quit":
            print("Final Score -> You:", user_score, "| Computer:", comp_score)
            break

        if user not in choices:
            print("Invalid choice!")
            continue

        comp = random.choice(choices)
        print("Computer chose:", comp)

        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            comp_score += 1

game()
