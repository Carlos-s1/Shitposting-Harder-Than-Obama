def hangman_display(guess,secret):
    guess = guess.lower()
    secret= secret.lower() 
    output= ' '
    for i in range (len(secret)):
        if secret [i] in guess:
            output += secret [i]
        elif secret[i] == ' ':
            output += ' '
        else :
            output += "_"
    return output
        