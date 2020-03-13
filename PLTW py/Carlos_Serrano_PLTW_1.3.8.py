from __future__ import print_function
import random
 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
  
    winner = random.choice(players) 

   
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    guesses = 1 
    while input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
    
def goguess():
    a=1
    b= 20
    c=random.randint(a,b)
    guesess=1
    print ('I have a number between' ,a, 'and' ,b, 'inclusive')
    while True:
       d=float(input("Guess: ")) 
       if  (d>c):
         print("Your guess is too high") 
       elif (d<c):
        print('Your guess is too high')
       else:
           print('Right! My number is ',c,'! You guessed in ',  guesess,'!')
           break
       guesess+=1
goguess()
    
        


