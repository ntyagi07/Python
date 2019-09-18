# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
number=random.randint(1,25)

print("How many games you want to play?")
games=int(input())
print("Select number between 1-25")
#response=int(input())
n=0
while n < games:
    print("Take a guess")
    guess=int(input())
    n=n+1
    if guess < number:
        print ("select higher number")
    if guess > number:
        print ("select lower number")
    if guess == number:
        break
    
if guess == number:
    n=str(n)
    print("You guessed the correct number in "+n+" guesses!")
    
if guess !=number:
    number = str(number)
    print ("Nope. The correct number is "+number)
        
  

