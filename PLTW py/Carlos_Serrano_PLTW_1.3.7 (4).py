import random
import matplotlib.pyplot as plt


plt.ion() 

def roll_hundred_pair():
    a= []
    a+=[random.choice([1,2,3,4,5,6])]
    
    for choices in range(100):
        a+= [random.choice([1,2,3,4,5,6])]
        
    plt.hist(a)
    plt.show()