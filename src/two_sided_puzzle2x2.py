from random import shuffle
from graph_display import build_solution_graph_two_sided
import random

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
        
        temp = solution.copy()
        other_side = generate_random_other_side(solution)

        print("\n{} {} \n{} {}\n".format(
            other_side[0],
            other_side[1],
            other_side[2],
            other_side[3],
        ))

        both = True
        build_solution_graph_two_sided(temp, other_side, both)
        

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

def generate_random_other_side(solution):

    img_list = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
    img = []
    
    for i in range(4):
        img.append(random.choice(img_list))

    # gives each link a new random image on other side 
    solution[0] = solution[0][:3] + img[0] + solution[0][3+1:]
    solution[1] = solution[1][:1] + case_switch(img[0]) + solution[1][1+1:]

    solution[1] = solution[1][:0] + img[1] + solution[1][0+1:]
    solution[3] = solution[3][:2] + case_switch(img[1]) + solution[3][2+1:]

    solution[2] = solution[2][:2] + img[2] + solution[2][2+1:]
    solution[0] = solution[0][:0] + case_switch(img[2]) + solution[0][0+1:]

    solution[3] = solution[3][:1] + img[3] + solution[3][1+1:]
    solution[2] = solution[2][:3] + case_switch(img[3]) + solution[2][3+1:]

    return solution

def case_switch(img):
    
    if img.islower():
        return img.upper()
    else:
        return img.lower()

def generate_other_side(solution):
    for i in range(4):
        piece = ''
        for j in range(4):
            # img = reflect_image(solution[i][j])
            img = solution[i][j]
            if img.islower():
                img.upper()
            else:
                img.lower()
            piece += img
        solution[i] = piece
    
    return solution
            
def reflect_image(img):
    if img == 'A':
        return 'd'
    elif img == 'B':
        return 'c'
    elif img == 'C':
        return 'b'
    elif img == 'D':
        return 'a'
    elif img == 'a':
        return 'D'
    elif img == 'b':
        return 'C'
    elif img == 'c':
        return 'B'
    elif img == 'd':
        return 'A'

def options(items):
    for idx, choice in enumerate(items):
        remainder = items[0:idx] + items[idx + 1:]
        yield choice, remainder

def orientations(text):
    for idx, _ in enumerate(text):
        yield text[idx:] + text[0:idx]

if __name__ == '__main__':
    main()
