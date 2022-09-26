from operator import index
import random

difficulty= input('choose difficulty(type 1,2 or 3):\n 1 easy\n 2 normal \n 3 hard\n')
difficulty=int(difficulty)
if difficulty==1:
    lives=12
elif difficulty==2:
    lives =9
else:
    lives=6

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter' ,'plane']
secret_word = random.choice(words)
print(secret_word)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False


def update_clue(guessed_letter,secret_word,clue):
    index=0
    
    while index<len(secret_word):
        if guessed_letter==secret_word[index]:
            clue[index]=guessed_letter
        index=index+1

while lives > 0:
    print(clue)
    print('lives left: '+ heart_symbol*lives)
    guess= input('guess a letter of the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('incorrect. You loose a life')
        lives=lives-1
    

if guessed_word_correctly:
    print('you won! The secret word was '+ secret_word)
else:
    print('you lost1 The secret word was'+ secret_word)