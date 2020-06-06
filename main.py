import random

def play_again():
    answer = input('Dou you want to play again "Yes or No": ').lower()
    if answer == 'yes':
        play_game()
        print('\n\n')
    else:
        print('Thank you for playing the game, Bye.')

def get_word():

    words = ['Mongolia', 'tetris', 'python', 'classmate', 'India', 'Nepal']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    guessed = False
    letter_guessed = []
    tries = 3

    print(f'Hint: The word contains {len(word)} letters')
    print(len(word) * '_')

    while guessed == False and tries > 0:
        print(f'You have {tries} tries.')
        guess = input('Enter a letter or full word(if you got it).').lower()

        # case 1 -> Only 1 letter entered:
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a letter')
            elif guess in letter_guessed:
                print('You have already guessed that letter before.')
            elif guess not in word:
                print('Sorry letter not in word.')
                letter_guessed.append(guess)
                tries -= 1
            elif guess in word:
            #     print('Well done, letter is in the word.')
                letter_guessed.append(guess)
            else:
                print('No idea why this line is printing.')
        
        # case 2 -> User enteres the full word:
        elif len(guess) == len(word):
            if guess == word:
                print('You got the word.') 
                guessed = True
            else:
                print('Sorry you got the word wrong.')
                tries -= 1

        # case 1 -> user inputs the letter which is > than total number in the word:

        else:
            print('The entered guess is > than actual word.')

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letter_guessed:
                    status += letter
                else:
                    status += '_'
            print(status)

        if status == word:
            print('Congraluation, You won!')   
            guessed = True
        elif tries == 0:
            print('You have run out of guess.')

    play_again()

play_game()