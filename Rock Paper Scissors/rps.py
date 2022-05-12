import random
moves = ('rock','paper','scissors')
win = int()
loss = int()
# need constraints on user input to limit answers #
######################################################
def shoot():
    global user
    user = input('Rock-Paper-Scissors- SHOOT\nYou: ')
    global comp
    comp = random.choice(moves)
    print(f'Comp:{comp}')
    # print(f'You picked {user} computer picked {comp}')
    global games
    games -= 1
####################################################
games = int(input('how many games?: '))
shoot()

while games >= 1:
    if user == comp:
        print("\nTie\n")
        games += 1
        shoot()
    if user == 'rock' and comp == 'scissors':
        print('\nYou Win!\n')
        win += 1
        shoot()
    if user == 'paper' and comp == 'rock':
        print('\nYou Win!\n')
        win += 1
        shoot()
    if user == 'scissors' and comp == 'paper':
        print('\nYou Win!\n')
        win += 1
        shoot()
    else:
        print('\nSorry, you lose!\n')
        loss += 1
        shoot()

if win > loss:
    print(f'\nYou cheat! You won {win} to {loss}')
else:
    print(f'\nToo bad, chump! I beat you {loss} to {win}..')
