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

# Starting section
print("Welcome to the greatest tic tac toe game ever created!!!!\n")
print(""""The rules of this game are:
1: Players decide who will be 'X' and 'O'.
2: Player that will start will be randomly decided.
3: Player will determine where to place the game piece by selecting a number, the numbers will match the layout of the keyboard number pad.\n""")

location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
            'loc5': '-', 'loc6': '-', 'loc7': '-', 'loc8': '-', 'loc9': '-'}
start_player = 0
first_player = 'x'
second_player = 'x'

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

def game_start_launch():
    global start_player, first_player, second_player
    playgame = input("Would you like to play a game? (y/n):  ")
    if playgame.lower() == 'y':
        from random import random
        first_player = input("Name of first player:(this will be the 'X' person)  ")
        second_player = input("Name of second player:(this will be the 'O' person) ")
        if random() >= .5:
            start_player = 1
        if start_player == 0:
            print(f'\n{first_player} will start the game and go first')
        else:
            print(f'\n{second_player} will start the game and go first')    
        game_turn(start_player)
    elif playgame.lower() == 'n':
        print("Goodbye")
        exit() 
    else:
        print('Please select either y or n:')
        game_start_launch()      
   

def game_turn(start_player):
    #pass
    loc = input('Please select 1-9 to place your mark: ')



game_start_launch()



### location['loc1'] = "X"
#print(location)
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
