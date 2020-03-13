import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets "interactive on": figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below?
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1,2,3,4,5,6])]

    for choices in range(100):
        a += [random.choice([1,2,3,4,5,6])]

    plt.hist(a)
    plt.show()