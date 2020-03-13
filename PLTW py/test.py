import random

def goGuess():
   a=2
   b=random.randint(1,a)
   d=1
   print("I have a number between 1 and", a, "inclusive.")
   while True:
       c=int(input("Guess: "))
       if(c < b):
           print(c," is too low.")
       elif(c > b):
           print(c," is too high.")
       else:
           print("Right! My number is", b, "! You guessed in", d, "guesses!")
           break
       d+=1
     
goGuess()