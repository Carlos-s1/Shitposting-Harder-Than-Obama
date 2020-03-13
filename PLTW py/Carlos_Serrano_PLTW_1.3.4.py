def food_id(food):
    fruits=['apple','banana','orange']
    citrus =['orange']
    starchy =['banana','potato']
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'Not Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, Not Fruit'
        else:
            return 'Not Starchy, Not Fruit'
            
def food_id_test():
    works= True
    if food_id('orange') != 'Citrus, Fruit':
        works=False
        print('orange bug in food id()')
    if food_id('banana') != 'Not Citrus, Fruit':
        works= False
        print('banana bug in food_id()')
    if works:
        print ('food_id passed all tests')
        return works
def f(x):
    if int(x) ==x:
        if x % 2 == 0:
            if x % 3 == 0:
                print ('the number is a multiple of 6')
            else:
                print ( 'the number is odd')
        else:
            print(' the number is not an integer')
            
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