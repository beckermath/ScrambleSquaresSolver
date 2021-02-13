from random import shuffle
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

#
#   Initializing graph with 8 vertiticies, representing the two sides of the 4 puzzle images
#
#   A   B   C   D
#
#   a   c   c   d
#

def main():
    # If you choose to not shuffle, solution found will be the current order of PIECES
    # matching solution in images/puzzle.png with graph representation in images/example_graph.png

    shuffle(PIECES)
    empty_board = [None for i in range(9)]

    # sorts the pieces in order of their potential to be the middle piece
    CENTER_MAXIMIZED_PIECES = maximize_center(PIECES)

    start_time = time.time()
    solvable, solution = solve(PIECES, empty_board)
    end_time = time.time()

    if(solvable):
        print_solution(solution, start_time, end_time)
        build_solution_graph(solution)
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


    # spiral function transforms the index to start with the middle piece
    # 7 8 9
    # 6 1 2 
    # 5 4 3

    num = board.index(None)
    num_spiral = spiral(num)

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

def spiral(num):

    #
    #  1 2 3    7 8 9
    #  4 5 6 -> 6 1 2 
    #  7 8 9    5 4 3
    #
    # programmed the lazy way
    
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


def print_solution(solution, start_time, end_time):

    print("Star = Aa, Cone = Bb, House = Cc, Face = Dd")
    print("bottom:0 left:1 top:2 right:3\n")
    print("1 2 3\n4 5 6\n7 8 9\n")
    print("{}   {}   {}\n{}   {}   {}\n{}   {}   {}\n".format(
        solution[0],
        solution[1],
        solution[2],
        solution[3],
        solution[4],
        solution[5],
        solution[6],
        solution[7],
        solution[8],
    ))

    print("Execution time: %s seconds" % (end_time - start_time))


if __name__ == '__main__':
    main()
