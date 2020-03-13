def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
        
def letter_in_word(guess,word):
    if guess in word:
        return True
    else:
        return False 
def hint(guess,secret):
    if guess in secret:
        return 'the color Is In the sequence'
    else:
        return 'the color is not in the color sequence'