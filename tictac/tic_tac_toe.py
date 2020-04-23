# Starting section   V1.10
print("Welcome to the greatest tic tac toe game ever created!!!!\n")
print(""""The rules of this game are:
1: Players decide who will be 'X' and 'O'.
2: Player that will start will be randomly decided.
3: Player will determine where to place the game piece by selecting a number between 1-9, 
   the gameboard locations will match the layout of the keyboard number pad.
4: Select q to quit the game.\n""")

location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
            'loc5': '-', 'loc6': '-', 'loc7': '-', 'loc8': '-', 'loc9': '-'}            

win_combo = [('loc1','loc2','loc3'),('loc1','loc4','loc7'),('loc3','loc6','loc9'),('loc4','loc5','loc6'),('loc7','loc8','loc9'),('loc2','loc5','loc8'),('loc1','loc5','loc9'),('loc3','loc5','loc7')]

start_player = True
first_player = 'x'
second_player = 'x'

def displayGameBoard(location):
    clear_display()
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

def validate_square_not_selected_already(loc):
    if location['loc'+loc] != '-':
        print('Square is already selected, chose another square:')
        game_turn()
    else:
        return

def set_mark_board(loc, player):
    if start_player == True:
        location['loc'+loc] = 'X'
        return
    else:
        location['loc'+loc] = 'O'
        return

def game_start_launch():
    global start_player, first_player, second_player
    playgame = input('Would you like to play a game? (y/n):  ')
    if playgame.lower() == 'y':
        first_player = input("Name of first player:(this will be the 'X' person)  ")
        second_player = input("Name of second player:(this will be the 'O' person) ")
        from random import random
        if random() >= .5:
            start_player = False
        if start_player == True:
            print(f'\n{first_player} will start the game and go first')
        else:
            print(f'\n{second_player} will start the game and go first')    
        game_turn()
    elif playgame.lower() == 'n':
        print('Goodbye')
        exit() 
    else:
        print('Please select either y or n:')
        game_start_launch()      

def validate_input(loc):
    try:
        val = int(loc)
        if val == 1 or val == 2 or val == 3 or val == 4 or val == 5 or val == 6 or val == 7 or val == 8 or val == 9:
            return val
        else:
            print('You did not chose a number between 1 and 9: Please reselect')
            game_turn()  
    except ValueError:
        if loc == 'q' or loc == 'Q':
            print('Goodbye')
            exit()
        else:
            print('You did not chose a number between 1 and 9: Please reselect')
            game_turn()
    return    
       
def clear_display():
    from os import system, name
    if name == 'nt':
        _ = system('cls')
    else:
        _= system('clear')

def game_turn():
    continue_game = True
    global start_player
    if continue_game == True:
        current_player = start_player
        player_name = ''
        if current_player == True:
            player_name = first_player
        else:
            player_name = second_player
        print(f'{player_name} Turn:')    
        loc = input('Please select 1-9 to place your mark: ')
        validate_input(loc)
        validate_square_not_selected_already(loc)
        set_mark_board(loc, current_player)
        displayGameBoard(location)
        result = game_win_check(location)
        if result == 1:
            contine_game = False
            if input('Would you like to play again? ') == 'y':
                game_reset()
                game_start_launch
            else:
                print('Good-Bye')
                exit()
        else:
            current_player = not current_player
        start_player = current_player
        displayGameBoard(location)
    game_turn()

def game_win_check(location):
    chk_x = []
    chk_o = []
    count = 0
    win_combo_count = 0
    match_count = 0
    win_sub_counter = 1
    for i in location:
        if location.get(i) == 'X':
            chk_x.append(i)
        elif location.get(i) == 'O':
            chk_o.append(i)
    if len(chk_x) + len(chk_o) == 9:
        print('Game is a Draw!')
        return 1 
    while count < 8:
        if start_player == True:
            player_icon = chk_x
        else:
            player_icon = chk_o    
        for selected_square in player_icon:
            win_sub_counter += 1
            winning_subset_combo = list(win_combo[win_combo_count])
            for winner_check_item in winning_subset_combo:
                if winner_check_item in selected_square:
                    match_count += 1
                if match_count == 3:
                    print('We have a WINNER!!!!')
                    return 1
        count +=1
        match_count = 0
        win_combo_count += 1
    return 0   


def game_reset():
    global location, start_player
    start_player = True
    location = {'loc1': '-', 'loc2': '-', 'loc3': '-', 'loc4': '-',
            'loc5': '-', 'loc6': '-', 'loc7': '-', 'loc8': '-', 'loc9': '-'} 
    match_count = 0

game_start_launch()


