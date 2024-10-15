""" Rules:
Rock wins against scissors
scissors win against papers
paper wins against rock

0--rock,1--paper,2--scissors

users choice      computers choice
0                 0--draw
0                 1--computer wins
0                 2--user wins
1                 0--user wins
1                 1--draw
1                 2--computer wins
2                 0--computer wins
2                 1--user wins
2                 2--draw
"""
import random
user_choice=int(input("Enter your choice: Type 0 or Type 1 or Type 2: "))

if user_choice>3 or user_choice<0:
    print("You entered invalid number, You lost")
else:
    computer_choice=random.randint(0,2)
    print("Computer Choice: ",computer_choice)
    if user_choice==computer_choice:
        print("The Game is Draw")
        
    elif computer_choice < user_choice:
        print(" Hurrayyy!! You Won!!!")
    elif computer_choice > user_choice:
        print("Computer Wins Better Luck Next Time :(")
        
    elif user_choice==0 and computer_choice==2:
        print("Hurrayy! You Won!!!")
    else:
        print("Computer Wins Better Luck Next Time :( ")