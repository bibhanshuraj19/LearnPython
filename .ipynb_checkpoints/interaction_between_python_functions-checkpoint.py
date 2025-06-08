from random import shuffle

mylist = ['','0','']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list(mylist))


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = (input('Guess a number : '))
    return int(guess)
print(player_guess())

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct Guess')
    else:
        print('Wrong Guess')
        print(mylist)

