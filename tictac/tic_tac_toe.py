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

#### section for framework around the game



### board display section
location = {'loc1':'-', 'loc2': '-','loc3':'-', 'loc4': '-','loc5':'-', 'loc6': '-','loc7':'-', 'loc8': '-','loc9':'-'}
def displayGameBoard():
    #pass
    
    print('   |   |   ')
    print(' '+ location['loc7'] + ' | '  + location['loc8'] + ' | ' + location['loc9'] )
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+ location['loc4'] + ' | '  + location['loc5'] + ' | ' + location['loc6'] )
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+ location['loc1'] + ' | '  + location['loc2'] + ' | ' + location['loc3'] )
    print('   |   |   ')

displayGameBoard()

### 