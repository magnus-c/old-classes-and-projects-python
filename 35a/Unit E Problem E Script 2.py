'''
Magnus Chiu
CIS 41A Spring 2022
Unit E, Problem E Script 2
'''
import random

#this generates a random int from 1-100, inclusive
secretNum = random.randint(1,100)

print("Welcome the guessesing game.");
print("You need to guess a number from 1 to 100.");
guess = int();
turn = int();
while guess != secretNum:
    guess = int(input("What is your guess? "));
    if guess < secretNum:
        print("Guess is too low.");
        turn +=1;
    elif guess > secretNum:
        print("Guess is too high.");
        turn +=1;
    else:
        print("Congratulations!");
        print("You guessed the secret number in", turn,"guesses!");
            
'''
Execution results:
Welcome the guessesing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too low.
What is your guess? 75
Guess is too low.
What is your guess? 87
Guess is too high.
What is your guess? 81
Guess is too high.
What is your guess? 84
Guess is too high.
What is your guess? 85
Guess is too high.
What is your guess? 77
Guess is too low.
What is your guess? 79
Congratulations!
You guessed the secret number in 7 guesses!
'''