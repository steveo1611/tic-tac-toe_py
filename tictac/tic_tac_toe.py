""" req:
- 2 players able to play on same computer
- board will be reprinted after each move
- accept input (move) and display symbol on board.

thoughts on steps: 
-- create game framework (play game, replay, quit game) (if fancy ask for player names)
--create board display section
-- create 'symbols' section (part of the display section)
-- create inputs section (part of the framework section)
--create unit tests for each section as needed
"""

# section for framework around the game
print("Welcome to the greatest tic tac toe game ever created!!!!")
input("Would you like to play a game??:  ")

# board display section
location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
            'loc5': '-', 'loc6': '-', 'loc7': '-', 'loc8': '-', 'loc9': '-'}


def displayGameBoard(location):
    # pass
    # clear display????
    print('   |   |   ')
    print(' ' + location['loc7'] + ' | ' +
          location['loc8'] + ' | ' + location['loc9'])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + location['loc4'] + ' | ' +
          location['loc5'] + ' | ' + location['loc6'])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + location['loc1'] + ' | ' +
          location['loc2'] + ' | ' + location['loc3'])
    print('   |   |   ')
    print('')


location['loc1'] = "X"
print(location)
displayGameBoard(location)


# test_display()
###
"""
def test_display():
    location = {'loc1': 'X', 'loc2': 'X', 'loc3': 'X', 'loc4': 'X',
                'loc5': 'X', 'loc6': 'X', 'loc7': 'X', 'loc8': 'X', 'loc9': 'X'}
    displayGameBoard(location)

    location = {'loc1': 'O', 'loc2': 'O', 'loc3': 'O', 'loc4': 'O',
                'loc5': 'O', 'loc6': 'O', 'loc7': 'O', 'loc8': 'O', 'loc9': 'O'}
    displayGameBoard(location)
"""

"""    from random import random
    x = ''
    o = ''
    for item in location:
        if random() >= .5:
            item = 'X'
            print(item)
        else:
            item = 'O'
            print(item)
    return location() 
"""
