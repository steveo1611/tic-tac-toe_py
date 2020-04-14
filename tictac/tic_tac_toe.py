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

# Starting section   V1.0
'''
print("Welcome to the greatest tic tac toe game ever created!!!!\n")
print(""""The rules of this game are:
1: Players decide who will be 'X' and 'O'.
2: Player that will start will be randomly decided.
3: Player will determine where to place the game piece by selecting a number, the numbers will match the layout of the keyboard number pad.\n""")
'''
#location = {'loc1': '-', 'loc2': 'X', 'loc3': 'X', 'loc4': '-',
# 'loc5': 'X', 'loc6': 'X', 'loc7': 'X', 'loc8': '-', 'loc9': '-'}

#location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
#            'loc5': '-', 'loc6': '-', 'loc7': 'O', 'loc8': 'O', 'loc9': 'O'}

location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
            'loc5': '-', 'loc6': '-', 'loc7': '-', 'loc8': '-', 'loc9': '-'}            

win_combo = [('loc1','loc2','loc3'),('loc4','loc5','loc6'),('loc7','loc8','loc9'),('loc2','loc5','loc8'),('loc1','loc5','loc9'),('loc3','loc5','loc7')]

start_player = True
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

def set_mark_board(loc, player):
    if start_player == True:
        location['loc'+loc] = "X"
        return
    else:
        location['loc'+loc] = "O"
        return

def game_start_launch():
    global start_player, first_player, second_player
    playgame = input("Would you like to play a game? (y/n):  ")
    if playgame.lower() == 'y':
        from random import random
        first_player = input("Name of first player:(this will be the 'X' person)  ")
        second_player = input("Name of second player:(this will be the 'O' person) ")
        if random() >= .5:
            start_player = False
        if start_player == True:
            print(f'\n{first_player} will start the game and go first')
        else:
            print(f'\n{second_player} will start the game and go first')    
        game_turn()
    elif playgame.lower() == 'n':
        print("Goodbye")
        exit() 
    else:
        print('Please select either y or n:')
        game_start_launch()      

def validate_input(loc):
    try:
        val = int(loc)
        return val
    except ValueError:
        print("You did not chose a number between 1 and 9: Please reselect")
        return 
       

def game_turn():
    #pass
    continue_game = True
    global start_player
    if continue_game == True:
        current_player = start_player
        loc = input('Please select 1-9 to place your mark: ')
        validate_input(loc)
        set_mark_board(loc, current_player)
        game_win_check(location)
        if game_win_check == 1:
            print('WINNER!!!!')
            exit()
        else:
            current_player = not current_player
        start_player = current_player
        displayGameBoard(location)
    game_turn()

    #if start_player == 0:
        #pass

def game_win_check(location):
    chk_x = []
    chk_o = []
    count = 0
    count2 = 0
    match_count = 0
    win_sub_counter = 0
    
    for i in location:
        if location.get(i) == 'X':
            chk_x.append(i)
        elif location.get(i) == 'O':
            chk_o.append(i)
    while count < 6:
        #print(win_sub)
        if start_player == True:
            player_icon = chk_x
        else:
            player_icon = chk_o    
            for beep in player_icon:
                win_sub_counter += 1
                win_sub = list(win_combo[count2])
                #print(beep)
                for blah in win_sub:
                    if win_sub_counter == 3:
                        count2 += 1
                        match_count = 0
                    if blah in beep:
           # print(win_sub)
             #       print('xx')
                        match_count += 1
                        if match_count == 3:
                            print('We have a WINNER')
                            return 1
            count +=1
        return 0   



game_start_launch()

#displayGameBoard(location)


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

