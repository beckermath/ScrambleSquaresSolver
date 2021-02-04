from graph import add_vertex, add_edge, print_graph
from random import shuffle

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

graph = {}
add_vertex(graph, 'A')
add_vertex(graph, 'a')
add_vertex(graph, 'B')
add_vertex(graph, 'b')
add_vertex(graph, 'C')
add_vertex(graph, 'c')
add_vertex(graph, 'D')
add_vertex(graph, 'd')

def main():
    shuffle(PIECES)
    empty_board = [None for i in range(9)]
    solvable, solution = solve(PIECES, empty_board)

    if(solvable):
        print_solution(solution)
        build_solution_graph(solution)

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

def print_solution(solution):
    print("Star = Aa, Cone = Bb, House = Cc, Face = Dd")
    print("bottom left top right\n")
    print("{}   {}   {}\n{}   {}   {}\n{}   {}   {}".format(
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

def build_solution_graph(solution):
    print("build solution graphs")

if __name__ == '__main__':
    main()
