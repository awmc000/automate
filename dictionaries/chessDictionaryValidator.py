def isValidChessBoard(board):
    # Check for improper spaces
    for k in list(board.keys()):
        if k[1] not in 'abcdefgh':
            return False
        if k[0] not in '12345678':
            return False
    # Check for pieces that do not begin with 'w' or 'b'
    for v in list(board.values()):
        if v[0] not in 'wb':
            return False
        blackPieces = 0
        blackKings = 0
        blackPawns = 0

        whitePieces = 0
        whiteKings = 0
        whitePawns = 0
        if (v[0] == 'b'):
            blackPieces += 1
            if (v[1:] == 'king'):
                blackKings += 1
            elif (v[1:] == 'pawn'):
                blackPawns += 1
        elif (v[0] == 'w'):
            whitePieces += 1
            if (v[1:] == 'king'):
                whiteKings += 1
            elif (v[1:] == 'pawn'):
                whitePawns += 1
        if (blackPieces > 16) or (whitePieces > 16):
            return False
        if (blackKings > 1) or (whiteKings > 1):
            return False
        if (blackPawns > 8) or (whitePawns > 8):
            return False
    return True


chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
        '5h': 'bqueen', '3e': 'wking'}
check = isValidChessBoard(chessBoard)
badBoard = {'3z': 'gking'}
badCheck = isValidChessBoard(badBoard)
print(check)
print(badCheck)


