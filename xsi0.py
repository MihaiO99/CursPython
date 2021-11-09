board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']


def display():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def check_win_player():
    row1 = board[0] + board[1] + board[2]
    row2 = board[3] + board[4] + board[5]
    row3 = board[6] + board[7] + board[8]
    col1 = board[0] + board[3] + board[6]
    col2 = board[1] + board[4] + board[7]
    col3 = board[2] + board[5] + board[8]
    diag1 = board[0] + board[4] + board[8]
    diag2 = board[2] + board[4] + board[6]
    if row1 == 'XXX' or row2 == 'XXX' or row3 == 'XXX' or col1 == 'XXX' or col2 == 'XXX' or col3 == 'XXX' or diag1 == 'XXX' or diag2 == 'XXX':
        return True


def check_win_PC():
    row1 = board[0] + board[1] + board[2]
    row2 = board[3] + board[4] + board[5]
    row3 = board[6] + board[7] + board[8]
    col1 = board[0] + board[3] + board[6]
    col2 = board[1] + board[4] + board[7]
    col3 = board[2] + board[5] + board[8]
    diag1 = board[0] + board[4] + board[8]
    diag2 = board[2] + board[4] + board[6]
    if row1 == '000' or row2 == '000' or row3 == '000' or col1 == '000' or col2 == '000' or col3 == '000' or diag1 == '000' or diag2 == '000':
        return True


count_nr = 0
turn = 0
display()
while count_nr <= 8:
    if turn == 0:
        poz_juc = input("Indicate position (1-9): ")
        for iterator, value in enumerate(board):
            if poz_juc == value:
                board[iterator] = 'X'
                count_nr += 1
                turn = 1
        if check_win_player():
            display()
            print("Player won!")
            break
    if turn == 1:
        if board[4] == '5':
            board[4] = '0'
        elif board[0] == '1' or board[2] == '3' or board[6] == '7' or board[8] == '9':
            for iterator, value in enumerate(board):
                if value == '1':
                    board[iterator] = '0'
                    break
                elif value == '3':
                    board[iterator] = '0'
                    break
                elif value == '7':
                    board[iterator] = '0'
                    break
                elif value == '9':
                    board[iterator] = '0'
                    break
        else:
            for iterator, value in enumerate(board):
                if value == '2':
                    board[iterator] = '0'
                    break
                elif value == '4':
                    board[iterator] = '0'
                    break
                elif value == '6':
                    board[iterator] = '0'
                    break
                elif value == '8':
                    board[iterator] = '0'
                    break
        turn = 0
        count_nr += 1
        if check_win_PC():
            display()
            print("PC won!")
            break
    display()
    if count_nr == 10:
        print("Tie!")