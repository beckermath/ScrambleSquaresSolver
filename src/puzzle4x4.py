from random import shuffle

PIECES = [
    'ABab', 'aBcC', 'dcbc', 'ACdB',
    'dBaD', 'BdAc', 'bCDB', 'BbaC',
    'BCDd', 'CDbB', 'DbBC', 'dcba',
    'Bdba', 'CAcb', 'ABda', 'bADd'
]

BOTTOM, LEFT, TOP, RIGHT = 0, 1, 2, 3


SQUARE_LINKS = (
    # TOP ROW
    ((RIGHT, 1, LEFT), (BOTTOM, 4, TOP),),
    ((LEFT, 0, RIGHT), (BOTTOM, 5, TOP), (RIGHT, 2, LEFT)),
    ((LEFT, 1, RIGHT), (BOTTOM, 6, TOP), (RIGHT, 3, LEFT)),
    ((LEFT, 2, RIGHT), (BOTTOM, 7, TOP)),

    # MIDDLE ROW 1
    ((TOP, 0, BOTTOM), (RIGHT, 5, LEFT), (BOTTOM, 8, TOP),),
    ((LEFT, 4, RIGHT), (TOP, 1, BOTTOM), (RIGHT, 6, LEFT), (BOTTOM, 9, TOP)),
    ((LEFT, 5, RIGHT), (TOP, 2, BOTTOM), (RIGHT, 7, LEFT), (BOTTOM, 10, TOP)),
    ((LEFT, 6, RIGHT), (TOP, 3, BOTTOM), (BOTTOM, 11, TOP)),

    # MIDDLE ROW 2
    ((TOP, 4, BOTTOM), (RIGHT, 9, LEFT), (BOTTOM, 12, TOP),),
    ((LEFT, 8, RIGHT), (TOP, 5, BOTTOM), (RIGHT, 10, LEFT), (BOTTOM, 13, TOP)),
    ((LEFT, 9, RIGHT), (TOP, 6, BOTTOM), (RIGHT, 11, LEFT), (BOTTOM, 14, TOP)),
    ((LEFT, 10, RIGHT), (TOP, 7, BOTTOM), (BOTTOM, 15, TOP)),

    # BOTTOM ROW 
    ((TOP, 8, BOTTOM), (RIGHT, 13, LEFT)),
    ((LEFT, 12, RIGHT), (TOP, 9, BOTTOM), (RIGHT, 14, LEFT)),
    ((LEFT, 13, RIGHT), (TOP, 10, BOTTOM), (RIGHT, 15, LEFT)),
    ((LEFT, 14, RIGHT), (TOP, 11, BOTTOM)),
)

def main():    
    empty_board = [None for i in range(16)]
    shuffle(PIECES)
    print("Pieces in random order")
    print(PIECES)

    solvable, solution = solve(PIECES, empty_board)
    
    if solvable:
        print("\nbig solution is not printed nicely yet")
        print("Star = Aa, Cone = Bb, House = Cc, Face = Dd")

        print("\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n".format(
            solution[0],
            solution[1],
            solution[2],
            solution[3],
            solution[4],
            solution[5],
            solution[6],
            solution[7],
            solution[8],
            solution[9],
            solution[10],
            solution[11],
            solution[12],
            solution[13],
            solution[14],
            solution[15],
        ))
    else:
        print("provided board has no solution")

def solve(pieces, board):
    if not pieces:
        return True, board

    num = board.index(None)

    for piece_chosen, remainder in options(pieces):
        for piece in orientations(piece_chosen):
            next_board = board[0:num] + [piece] + board[num + 1:]

            piece_fits = True
            for src_dir, other, dest_dir in SQUARE_LINKS[num]:
                if board[other]:
                    edge1 = next_board[num][src_dir]
                    edge2 = next_board[other][dest_dir]
                    piece_fits &= (edge1.lower() == edge2.lower() and (edge1 == edge1.upper()) == (edge2 == edge2.lower()))

            if piece_fits:
                solved, solved_board = solve(remainder, next_board)
                if solved:
                    return True, solved_board

    return False, None 

def options(items):
    for idx, choice in enumerate(items):
        remainder = items[0:idx] + items[idx + 1:]
        yield choice, remainder

def orientations(text):
    for idx, _ in enumerate(text):
        yield text[idx:] + text[0:idx]

if __name__ == '__main__':
    main()