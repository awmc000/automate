board = {0: ' ', 1: ' ', 2: ' ',
         3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' '}

def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' +board[7] + '|' + board[8]) 

printBoard(board)

while True:
    print('Player 1: Enter a cell to mark.')
    choice = int(input())
    if board[choice] != 'O':
        board[choice] = 'X'
    printBoard(board)
    print('Player 2, O\'s: enter a cell to mark.')
    choice = int(input())
    if board[choice] != 'X':
        board[choice] = 'O'
    printBoard(board)
