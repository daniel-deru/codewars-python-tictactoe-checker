def is_solved(board):
    if len(board) == 1:
        board = board[0]
    d1 = []
    d2 = []
    zero = []
    for i in range(len(board)):
        if board[i].count(0) > 0:
            zero.append(board[i].count(0))
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != 0:
                return board[0][i]
        elif board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != 0:
                return board[i][0]
        elif board[0][0] == board[i][i]:
            d1.append(board[i][i])
            if len(d1) > 2:
                if d1[0] != 0:
                    return d1[0]
        elif i <= 2:
            if board[0][2] == board[i][2 - i]:
                d2.append(board[i][2 - i])
            elif len(d2) > 2:
                if d2[0] != 0:
                    return d2[0]

    if len(zero) > 0:
        return -1
    else: return 0
       
       

            



board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board))