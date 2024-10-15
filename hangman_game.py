import random
import hangman_stages
word_list=["apple","beautiful","potato","orange","banana","goods","services","hello","welcome"]
lives=6
choosen_word=random.choice(word_list)
print("The length of the word will be:",len(choosen_word))
display=[]
for i in range(len(choosen_word)): #potato
    display += "_"
print(display)
game_over=False
while not game_over:
    guess=input("Guess the letter: ") #r
    for position in range(len(choosen_word)):  #0 1 2 3 4
        letter=choosen_word[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if guess not in choosen_word:
        lives -=1
        if lives == 0:
            game_over=True
            print("You lost")
    if "_" not in display:
        game_over=True
        print("You Won!!!")
    print(hangman_stages.stages[lives])
    
