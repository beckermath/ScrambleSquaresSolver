def transform_board(board):
    transformed = [None for i in range(9)]

    transformed[0] = board[6]
    transformed[1] = board[7]
    transformed[2] = board[8]
    transformed[3] = board[5]
    transformed[4] = board[0]
    transformed[5] = board[1]
    transformed[6] = board[4]
    transformed[7] = board[3]
    transformed[8] = board[2]

    return transformed

def untransform_board(board):
    untransformed = [None for i in range(9)]

    untransformed[6] = board[0]
    untransformed[7] = board[1]
    untransformed[8] = board[2]
    untransformed[5] = board[3]
    untransformed[0] = board[4]
    untransformed[1] = board[5]
    untransformed[4] = board[6]
    untransformed[3] = board[7]
    untransformed[2] = board[8]

    return untransformed

def spiral(num):
    if num is 0:
        return 4
    if num is 1:
        return 5
    if num is 2:
        return 8
    if num is 3:
        return 7
    if num is 4:
        return 6
    if num is 5:
        return 3
    if num is 6:
        return 0
    if num is 7:
        return 1
    if num is 8:
        return 2

def unspiral(num):
    if num is 4:
        return 0
    if num is 5:
        return 1
    if num is 8:
        return 2
    if num is 7:
        return 3
    if num is 6:
        return 4
    if num is 3:
        return 5
    if num is 0:
        return 6
    if num is 1:
        return 7
    if num is 2:
        return 8