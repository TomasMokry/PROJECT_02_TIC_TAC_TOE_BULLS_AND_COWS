"""
projekt_2B.py: druhý projekt do Engeto Online Python Akademie
TIC TAC TOE
author: Tomáš Mokrý
email: tomas.mokry@gmail.com
discord: Tomas M#0922

"""
import time
import os
from random import randint


def main():
    game_on = True
    game(game_on)

def game(game_on):

    start_time = time.time()
    field = create_game_board()
    player = ' X ' if random_first_player() == 1 else ' O '
    
    while game_on:
        os.system('clear')
        divider = 48 * '='
        welcome_text()
        show_board(field)
        
        position = input(f'Player {player} | Please enter your move number: ')
        if not position.isnumeric():
            print('Wrong input, please try again')
            time.sleep(1)
            continue
        elif len(position) != 1:
            print('Wrong input, please try again')
            time.sleep(1)
            continue
        elif field[(int(position)-1) // 3][(int(position)-1) % 3] != '   ':
            print('This position is already taken, please try again.')
            time.sleep(1)
            continue
        else:
            position = int(position)
        
        field = write_player_move(field, player, position)
        
        if find_winner(field, player):
            game_on = False
        
        if is_field_full(field):
            game_on = False
        
        player = switch_players(player)
    
    else:
        os.system("clear")
        game_time = time.time() - start_time
        
        if is_field_full(field):
            print(f'It is a GAME DRAW, play again. \n{divider}')
        else:
            player = switch_players(player)
            print(f'Player {player} is the WINNER! Congratulation! \n{divider}')
        
        show_board(field)
        print(
            divider,
            'Your game time:', time.strftime("%H:%M:%S",time.gmtime(game_time)),
            divider,
            sep = '\n'
            )
        

def random_first_player() ->int:
    """
    Description:
    Generates random integer 0 or 1 
    
    """
    return randint(0,1) 


def switch_players(player: str) ->str:
    """
    Description:
    Takes one string name of one player 
    and return string name of second player
    
    Example: 
    player = ' X '
    player = ' O '  
    
    Result:
    ---------
    ' O '
    ' X '
    ---------
    """
    return ' X ' if player == ' O ' else ' O '


def create_game_board() ->list:
    """
    Description:
    Creates nested list, 
    
    Result:
    ---------
    [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
    ---------
    """
    board = []
    for i in range(3):
        row=[]
        for j in range(3):
            row.append('   ')
        board.append(row)
    return board


def show_board(field: list) ->None:
    """
    Description:
    Takes list and print game board

    Example: 
    field = [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]

    Result:
    ---------
    +-----+-----+-----+
    |     |     |     |
    +-----+-----+-----+
    |     |     |     |
    +-----+-----+-----+
    |     |     |     |
    +-----+-----+-----+
    ---------
    """
    for row in field:
        print('+-----+-----+-----+')
        for item in row:
            print('|', item, end=" ")
        print('|')
    print('+-----+-----+-----+')


def welcome_text() ->None:
    """
    Description:
    Prints the welcome text

    """
    divider = 48 * '='
    divider_2 = 48 * '-'
    print(f'''
Welcome to Tic Tac Toe
{divider}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{divider}
Let's start the game
{divider_2}'''
) 


def write_player_move(field: list, player: str, position: int) ->list:
    """
    Description:
    Placing the player symbol into the list into the position
    input position number is from 1 - 9, this number
    is translated into nested list indexes
    
    Example: 
    position = 9
    position = 7
    
    Result:
    ---------
    field[2][2] = player
    field[2][0] = player
    ---------
    """
    
    index_1 = (position-1) // 3
    index_2 = (position-1) % 3
    field[index_1][index_2] = player
    return field


def is_field_full(field: list) ->bool:
    """
    Description:
    Checking if all positions in the list are filled
    if yes returns True
    if not returns False
    
    Example: 
    [[' X ',' O ',' X '],[' X ',' X ',' O '],[' O ',' X ',' X ']]
    [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
    Result:
    ---------
    True
    False
    ---------
    """ 
    full = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == '   ':
                full = False
                break
    return full


def find_winner_rows(field: list, player: str) ->bool:
    """
    Description:
    Checking if there are 3 same player symbols in nested list (rows)
    
    Example: 
    [[' X ',' X ',' X '],['   ','   ','   '],['   ','   ','   ']]
    [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
    Result:
    ---------
    True
    False
    ---------
    """
    
    for i in range(3):
        winner = True
        for j in range(3):
            if field[i][j] != player:
                winner = False
                break
        if winner:
            return winner
    return False


def find_winner_columns(field: list, player: str) ->bool:
    """
    Description:
    Checking if there are 3 same player symbols in nested list (columns)
    
    Example: 
    [[' X ','   ','   '],[' X ','   ','   '],[' X ','   ','   ']]
    [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
    Result:
    ---------
    True
    False
    ---------
    """
    
    for i in range(3):
        winner = True
        for j in range(3):
            if field[j][i] != player:
                winner = False
                break
        if winner:
            return winner
    return False


def find_winner_diagonals(field: list, player: str) ->bool: 
    """
    Description:
    Checking if there are 3 same player symbols in nested list (diagonals)
    
    Example: 
    [[' X ','   ','   '],['   ',' X ','   '],['   ','   ',' X ']]
    [['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]
    Result:
    ---------
    True
    False
    ---------
    """  
    
    winner = True
    for i in range(3):
        if field[i][i] != player:
            winner = False
            break
    if winner:
        return winner
     
    winner = True
    for i in range(3):
        if field[i][abs(i-2)] != player:
            winner = False
            break
    if winner:
        return winner
    return False


def find_winner(field: list, player: int) ->bool:
    """
    Description:
    Checking the combination of find winner functions
    find_winner_diagonals, find_winner_columns, find_winner_rows
    if just one is True - return True, else False

    Example: 
    win_row = True
    win_coll = False
    win_dia = False

    win_row = False
    win_coll = False
    win_dia = False
    Result:
    ---------
    True
    False
    ---------
    """ 
    win_row = find_winner_rows(field,player)
    win_coll = find_winner_columns(field,player)
    win_dia = find_winner_diagonals(field,player)
    return win_row or win_coll or win_dia

if __name__ == "__main__":
    main()
