import random
import logo
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low ")  
        return attempts-1
    elif guessed_number > answer:
        print("Your guess is too High")
        return attempts-1
    else:
        print(f"Your guess is right...the answer was {answer}")       
def game(): 
    print(logo.logo)
    print("Let me think between 1 to 50.")
    answer=random.randint(1,50)
    #print(answer)
    level=input("Choose the level  of dificulty...Type 'easy' or 'hard': \n")
    attempts=set_difficulty(level)
    gussed_number=0
    while gussed_number!=answer:
        print(f" You have {attempts} remaining to guess the number.")
        gussed_number=int(input("Guss a number : "))
        attempts=check_answer(gussed_number,answer,attempts)
        if attempts==0:
            print("You are out of attempts! You lost")
            return 
        elif gussed_number!=answer:
            print("Guess again")
game()