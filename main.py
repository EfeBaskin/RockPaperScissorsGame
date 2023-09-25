#rock/paper/scissors game with python
import random
while True:
    chances = ["scissors", "rock", "paper"]
    computer_guess = random.choice(chances)
    user_guess = str(input("choose among rock,paper,scissors : "))
    if user_guess=="rock":
        if computer_guess=="paper":
            print(f"you lost computer : {computer_guess}, you : {user_guess}")
        elif computer_guess=="scissors":
            print(f"you won computer : {computer_guess}, you : {user_guess}")
        else:
            print("tie")
    if user_guess=="paper":
        if computer_guess == "scissors":
            print(f"you lost computer : {computer_guess}, you : {user_guess}")
        elif computer_guess == "rock":
            print(f"you won computer : {computer_guess}, you : {user_guess}")
        else:
            print("tie")
    if user_guess == "scissors":
        if computer_guess == "rock":
            print(f"you lost computer : {computer_guess}, you : {user_guess}")
        elif computer_guess == "paper":
            print(f"you won computer : {computer_guess}, you : {user_guess}")
        else:
            print("tie")
    answer = input("do you wanna continue : ")
    if answer == "yes":
        continue
    else:
        print("goodbye")
    break
