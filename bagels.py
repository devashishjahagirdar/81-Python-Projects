#Bagels, a detective logic game. 
# #1 exercise from the Book 'The Big Book of Small Python Projects'

import random

#Game options
max_guess = 10 #maximum guesses
num_digits = 3 #guessing game digits

#print game instructions
print('I am thinking of a {}-digit number. Try to guess what it is.'.format(num_digits))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

#defining secret number function
def get_secret_num():
    nums = list('123456789')
    random.shuffle(nums)
    #print(nums)

    secret_num = ''
    for i in range(num_digits):
        secret_num += nums[i]
    
    return secret_num

#define clues function
def get_clues(guess, secret_num):

    if guess == secret_num:             
        return 'You got it right!'      #correct answer return

    clue = []
    for i in range(num_digits):
        if guess[i] == secret_num[i]:   
            clue.append('Fermi')
        elif guess[i] in secret_num:    
            clue.append('Pico')

    if len(clue) == 0:                  #bagels condition return
        return 'Bagels!'
    
    clue.sort()
    return ' '.join(clue)               #Fermi and Pico condition return

#user interface

#main loop
while True:

    secret_num = get_secret_num()
    print('I have thought of a number.')
    print('You have {} chances to guess it'.format(max_guess))
    
    print(secret_num) #testing

    guess_num = 1
    
    #game loop
    while guess_num <= max_guess:
        
        guess = ''
        
        #temporary loop to check for correct input
        while len(guess) != num_digits or not guess.isdecimal():
            guess = str(input('Guess #{}:\n> '.format(guess_num)))
            
        clues = get_clues(guess, secret_num)
        print(clues)

        guess_num += 1

        #break out of game loop
        if guess_num > max_guess:
            print('You ran out of guesses')
            print('The answer was {}'.format(secret_num))
            break 
    
        if guess == secret_num:
            print('You won the game!')
            break 
    
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break #break out of main loop

print('Thanks for playing!') #end of game