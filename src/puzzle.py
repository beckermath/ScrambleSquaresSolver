from random import shuffle
from transform import transform_board, untransform_board, spiral, unspiral
from puzzle_display import print_solution
from graph_display import build_solution_graph
from center import maximize_center
import time
 
#
#   Star = Aa
#   Cone = Bb
#   House = Cc
#   Face = Dd
#

PIECES = [
    'dBaD', 'BdAc', 'bCDB',
    'BCDd', 'CDbB', 'DbBC',
    'Bdba', 'CAcb', 'ABda',
]

def main():
    global PIECES
    selection = input("Organize pieces to maximize center? (y/n)\n")
    display_graph = input("Display solution graph? (y/n)\n")
    
    if(selection =="y"):
        PIECES = maximize_center(PIECES)
    else:
        shuffle(PIECES)
        print("Pieces in random order")
        print(PIECES)

    empty_board = [None for i in range(9)]

    start_time = time.time()
    solvable, solution = solve(PIECES, empty_board)
    end_time = time.time()

    if(solvable):
        print_solution(transform_board(solution), start_time, end_time)
        if display_graph == "y":
            build_solution_graph(transform_board(solution))
        
    else:
        print("provided board is unsolvable")


BOTTOM, LEFT, TOP, RIGHT = 0, 1, 2, 3

SQUARE_LINKS = (
    ((RIGHT, 1, LEFT), (BOTTOM, 3, TOP)),
    ((LEFT, 0, RIGHT), (BOTTOM, 4, TOP), (RIGHT, 2, LEFT)),
    ((LEFT, 1, RIGHT), (BOTTOM, 5, TOP)),

    ((TOP, 0, BOTTOM), (RIGHT, 4, LEFT), (BOTTOM, 6, TOP)),
    ((LEFT, 3, RIGHT), (TOP, 1, BOTTOM), (RIGHT, 5, LEFT), (BOTTOM, 7, TOP)),
    ((LEFT, 4, RIGHT), (TOP, 2, BOTTOM), (BOTTOM, 8, TOP)),

    ((TOP, 3, BOTTOM), (RIGHT, 7, LEFT)),
    ((LEFT, 6, RIGHT), (TOP, 4, BOTTOM), (RIGHT, 8, LEFT)),
    ((LEFT, 7, RIGHT), (TOP, 5, BOTTOM)),
)

def solve(pieces, board):
    if not pieces:
        return True, board

    num = board.index(None)
    num_spiral = spiral(num)

    for piece_chosen, remainder in options(pieces):
        for piece in orientations(piece_chosen):
            next_board = board[0:num] + [piece] + board[num + 1:]
            transformed_board = transform_board(next_board)

            piece_fits = True
            for src_dir, other, dest_dir in SQUARE_LINKS[num_spiral]:
                if transformed_board[other]:
                    edge1 = transformed_board[num_spiral][src_dir]
                    edge2 = transformed_board[other][dest_dir]
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
