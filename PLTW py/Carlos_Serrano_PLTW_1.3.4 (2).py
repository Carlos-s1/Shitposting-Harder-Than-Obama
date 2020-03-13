from __future__ import print_function
import random

def guess_once():
        secret = random.randint(1,4)
        print('I have a number between 1 and 4.')
        guess = int(input('Guess'))
        if guess !=secret:
            print ('Wrong, my number is ',secret, "." , sep='')
        else:
            print ('Right, my number is', guess, end='!\n')
            
            
def quiz_decimal(low,high):
    print ( 'type  number between',low ,'and' ,high)
    number = int(input('number'))
    if number >= high:
        print ('No,', number,'is greater than', high)
    if number<= low:
         print ('No,', number,'is lesser than', low)
    if low < number < high:
        print ('Good,', low, '<' ,number,'<', high)
        