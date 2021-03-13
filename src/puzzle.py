from random import shuffle
from transform import transform_board, untransform_board, spiral, unspiral
from puzzle_display import print_solution, print_big_solution
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

PIECES_TWO_BY_TWO = [
    'BCDd', 'CDbB',
    'Bdba', 'CAcb'
]

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

SQUARE_LINKS_SMALL = (
    ((RIGHT, 1, LEFT), (BOTTOM, 2, TOP)),
    ((LEFT, 0, RIGHT), (BOTTOM, 3, TOP)),
    ((TOP, 0, BOTTOM), (RIGHT, 3, LEFT)),
    ((LEFT, 2, RIGHT), (TOP, 1, BOTTOM))
)


SQUARE_LINKS_BIG = (
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

LINKS = SQUARE_LINKS_SMALL

def main():
    global PIECES
    global LINKS
    big_puzzle_select = input("Solve 4x4 puzzle instead of 3x3? (y/n)\n")

    if big_puzzle_select == "n":
        maximize_center_select = input("Organize pieces to maximize center? (y/n)\n")
        display_graph = input("Display solution graph? (y/n)\n")
    else:
        maximize_center_select = "n"
        display_graph = "n"


    PIECES = [
        'BCDd', 'CDbB',
        'Bdba', 'CAcb'
    ]
    
    num_pieces = 4
    empty_board = [None for i in range(4)]

    if big_puzzle_select == "y":
        PIECES = [
            'ABab', 'aBcC', 'dcbc', 'ACdB',
            'dBaD', 'BdAc', 'bCDB', 'BbaC',
            'BCDd', 'CDbB', 'DbBC', 'dcba',
            'Bdba', 'CAcb', 'ABda', 'bADd'
        ]
        
        LINKS = SQUARE_LINKS_BIG
        empty_board = [None for i in range(16)]
        num_pieces = 16
        maximize_center(PIECES, num_pieces)

    
    if maximize_center_select == "y":
        PIECES = maximize_center(PIECES, num_pieces)
    else:
        shuffle(PIECES)
        print("Pieces in random order")
        print(PIECES)


    if maximize_center_select == "y":
        start_time = time.time()
        solvable, solution = solve_spiral(PIECES, empty_board)
        end_time = time.time()
    else:
        start_time = time.time()
        solvable, solution = solve_normal(PIECES, empty_board)
        print(solution)
        end_time = time.time()

    # if solvable:
    #     if maximize_center_select == "y":
    #         solution = transform_board(solution)
        
    #     if big_puzzle_select == "y":
    #         print_big_solution(solution, start_time, end_time)
    #     else:
    #         print_solution(solution, start_time, end_time)

    #     if display_graph == "y":
    #         build_solution_graph(solution)
        
    # else:
    #     print("provided board is unsolvable")


def solve_spiral(pieces, board):
    if not pieces:
        return True, board

    num = board.index(None)
    num_spiral = spiral(num)

    for piece_chosen, remainder in options(pieces):
        for piece in orientations(piece_chosen):
            next_board = board[0:num] + [piece] + board[num + 1:]
            transformed_board = transform_board(next_board)

            piece_fits = True
            for src_dir, other, dest_dir in LINKS[num_spiral]:
                if transformed_board[other]:
                    edge1 = transformed_board[num_spiral][src_dir]
                    edge2 = transformed_board[other][dest_dir]
                    piece_fits &= (edge1.lower() == edge2.lower() and (edge1 == edge1.upper()) == (edge2 == edge2.lower()))

            if piece_fits:
                solved, solved_board = solve_spiral(remainder, next_board)
                if solved:
                    return True, solved_board

    return False, None 

def solve_normal(pieces, board):
    if not pieces:
        return True, board

    num = board.index(None)

    for piece_chosen, remainder in options(pieces):
        for piece in orientations(piece_chosen):
            next_board = board[0:num] + [piece] + board[num + 1:]

            piece_fits = True
            for src_dir, other, dest_dir in LINKS[num]:
                if board[other]:
                    edge1 = next_board[num][src_dir]
                    edge2 = next_board[other][dest_dir]
                    piece_fits &= (edge1.lower() == edge2.lower() and (edge1 == edge1.upper()) == (edge2 == edge2.lower()))

            if piece_fits:
                solved, solved_board = solve_normal(remainder, next_board)
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
