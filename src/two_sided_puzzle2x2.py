from random import shuffle
from graph_display import build_solution_graph_two_sided

PIECES = [
    'BCDd', 'CDbB',
    'Bdba', 'CAcb'
]

BOTTOM, LEFT, TOP, RIGHT = 0, 1, 2, 3

SQUARE_LINKS = (
    ((RIGHT, 1, LEFT), (BOTTOM, 2, TOP)),
    ((LEFT, 0, RIGHT), (BOTTOM, 3, TOP)),
    ((TOP, 0, BOTTOM), (RIGHT, 3, LEFT)),
    ((LEFT, 2, RIGHT), (TOP, 1, BOTTOM))
)

def main():    
    empty_board = [None for i in range(4)]
    shuffle(PIECES)
    print("Pieces in random order")
    print(PIECES)

    solvable, solution = solve(PIECES, empty_board)

    if solvable:
        print("\ntwo-sided solution is not printed nicely yet")
        print("Star = Aa, Cone = Bb, House = Cc, Face = Dd")

        print("\n{} {} \n{} {}\n".format(
            solution[0],
            solution[1],
            solution[2],
            solution[3],
        ))
        build_solution_graph_two_sided(solution)
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
