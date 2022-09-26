from random import *
player_score = 0
computer_score = 0
def hangedman(hangman):
    graphic=[
        """
        +-------+
        |
        |
        |
        |
        |
        ==============
        """,
        """
        +-------+
        |       |
        |       0
        |
        |
        |
        ==============
        """,
        """
         +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
        ==============
        """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
        ==============
        """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
        ==============
        """,
        """
         +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
        ==============
        """,
        """
        +-------+
        |       |
        |       0
        |      -|-
        |      / \
        |
        ==============
        """]
    print (graphic[hangman])
    return
def start():
    print('lets play a game of linux hangman')
    while game():
        pass
    scores()

def game():
    dictionary=['gnu','kernel','linux','magela','pengin','ubuntu']
    word=choice(dictionary)
    word_length=len(word)
    clue=word_length*['_']
    tries=6
    letters_tried=""
    guesses=0
    letters_right=0
    letters_wrong=0
    global computer_score,player_score

    while(letters_wrong!=tries) and("".join(clue)!=word):
        letter=guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) !=-1:
                print('you have already picked ', letter)
            else:
                letters_tried=letters_tried+letter
                first_index=word.find(letter)
                if first_index==-1:
                    letters_wrong+=1
                    print('sorry wrong letter')
                else:
                    print('congratulation',letter,'is correct')
                    for i in range(word_length):
                        if letter==word[i]:
                            clue[i]=letter

        else:
            print('choose another')

        hangedman(letters_wrong)
        print("".join(clue))
        print('guesses',letters_tried)

        if letters_wrong==tries:
            print('game over')
            print('the word was',word)
            computer_score+=1
            break
        if "".join(clue)==word:
            print('you win')
            print('the word was',word)
            player_score+=1
            break
        return play_again()

def guess_letter():
    print
    letter=raw_input('take a guess of the mystry word: ')
    letter.strip()
    letter.lower()
    print
    return letter

def play_again():
    answer=raw_input('would like play again? y/n: ')
    if answer in ('y','Y','yes','Yes','of course'):
        return answer
    else:
        print('thanks for playing. tll next time')

def score():
    global player_score,computer_score
    print("HIGH SCORES")
    print("player: ",player_score)
    print("computer: ",computer_score)

    if __name__=='__main__':
        start()

