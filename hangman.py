#Python game - Hangman

import random

words = 'BATMAN'
user = None
turn = 6
your_word = '_ ' * len(words)
your_guess = your_word[0:len(your_word)-1]
list1 = your_guess.split()


while user == None:
    print(your_word)
    print(your_guess)
    print(list1)
    user = input('Enter the character you guess:').upper()
    if len(user) != 1:
        print('Please enter one character')
        user = None
    for i in range(0, len(words)):
        if words[i] == user:
            list1[i] = user
    your_guess = ''.join(list1)
    print('Your guess is: {}'.format(your_guess))
    if your_guess==words:
      print("You win")
      break
    turn -= 1
    print('You have {} chances left to guess'.format(turn))
    if turn == 0:
        if your_guess == words:
            print('You win')
        else:
            print('You fail')
        break
    else:
        user = None
