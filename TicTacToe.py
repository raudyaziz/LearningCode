import random

def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('\n')

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def position_choice():

    position = 'X'
    within_range = False
    position_notUsed = False

    while position.isdigit() == False or within_range == False or position_notUsed == False:

        position = input('Please enter a position to place marker: ')

        if position.isdigit() == False:
            print('This is not a digit!')

        if position.isdigit() == True:
            if int(position) in list(range(1,10)):
                within_range = True
                if board[int(position)] != 'X' and board[int(position)] != 'O':
                    position_notUsed = True
                else:
                    print('Someone already placed marker on this cell!')
            else:
                print('This number is not a choice!')

    return int(position)

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, marker):

    game_over = False

    #check for lines
    for position_index in [1,4,7]:
        if board[position_index] == board[position_index + 1] == board[position_index + 2] == marker:
            game_over = True

    #check for columns
    for position_index in [1,2,3]:
        if board[position_index] == board[position_index + 3] == board[position_index + 2*3] == marker:
            game_over = True

    #Check for both diagonals
    if board[1] == board [5] == board[9] == marker or board[3] == board[5] == board[7] == marker:
        game_over = True

    return game_over

def player_starting():
    if random.randint(0,2) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

game_over = False

while game_over == False:

    board = ['#'] + [' '] * 9
    player1_marker , player2_marker = player_input()

    turn = player_starting()

    print('\n')
    print(turn + ' is starting...')
    print('\n')

    display_board(board)
    rounds = 0

    while rounds < 9 and not win_check(board, player1_marker) and not win_check(board, player2_marker):

            if turn == 'Player 1':
                place_marker(board, player1_marker, position_choice())
                display_board(board)
                turn = 'Player 2'
            else:
                place_marker(board, player2_marker, position_choice())
                display_board(board)
                turn = 'Player 1'

            rounds += 1

    if rounds == 9:
        print("Game Over! It's a tie!")

    if win_check(board, player1_marker):
        print('Player 1 won!')
    elif win_check(board, player2_marker):
        print('Player 2 won!')

    game_over = True
