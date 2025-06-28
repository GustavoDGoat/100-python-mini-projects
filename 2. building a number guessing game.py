"""Beginner Enhancements:

    Difficulty Levels

        Add easy/medium/hard modes that change the range of numbers (e.g., 1-10, 1-100, 1-1000).

        Adjust the number of allowed guesses based on difficulty.

    Score System

        Award points based on how quickly the user guesses the number or how few attempts they take.

        Deduct points for wrong guesses.

    Hints

        Provide hints like "too high" or "too low" after each guess.

        Add optional hints (e.g., "the number is even" or "the number is a multiple of 5").

    Play Again Option

        Ask the user if they want to play again after finishing a round."""
        
import math
import tkinter as tk
import random
import sys

score= 100
attempts=0
max_attemepts=5

name=input('please enter your name please')
print(f'welcome {name} to the games')
print('if you want the difficulty to be easy (1-20) select 1')
print('if you want the difficulty to be medium (10-100) select 2')
print('if you want the difficulty to be imposibble (100-1000) select 3')
print('to quit the game press 4')

level=int(input('please enter your level you want'))
if level ==4:
    print(f'Good bye{name}')
    sys.exit()
if level ==1:
    number=random.randint(1,10)
    while max_attemepts> attempts:
        user_input=int(input('enter your number of choice'))
        attempts+=1
        
        if user_input==number: 
            score+=(max_attemepts-attempts)* 10
            print(f'you are correct your score: {score}')
            break
        else:
            score -= 5  # Lose 5 points for wrong guess.
            print("❌ Wrong! Try again.")

elif level ==2:
    number=random.randint(10,100)
    while max_attemepts> attempts:
        user_input=int(input ('enter the value of your number'))
        attempts+=1
        
        if user_input == number:
            score+=(max_attemepts - attempts)* 10
            print(f'you are ritght your score is {score}')
            break
        else:
            print('Wrong try again')
elif level==3:
    number=random.randint(100,1000)
    while max_attemepts > attempts:
        user_input=int(input ('enter the value of your number'))
        
else:
    print('you entered the wrong level')
    print('please try again')
    print('Please select 1, 2, 3, or 4.')
