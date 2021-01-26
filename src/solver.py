"""
DFS backtracking scramble squares puzzle solver

Author: Becker Mathie
"""

from enum import Enum

class edge(Enum):
    STAR_TOP = 1,
    STAR_BOTTOM = -1,
    CONE_TOP = 2,
    CONE_BOTTOM = -2,
    HOUSE_TOP = 3,
    HOUSE_BOTTOM = -3,
    FACE_TOP = 4,
    FACE_BOTTOM = -4

class piece:
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

#build board & initialize pieces

"""
0 1 2
3 4 5
6 7 8
board below is in order of solution
"""

board = []
board.append(piece(edge.STAR_BOTTOM, edge.FACE_TOP, edge.FACE_BOTTOM, edge.CONE_TOP))
board.append(piece(edge.STAR_TOP, edge.HOUSE_BOTTOM, edge.CONE_TOP, edge.FACE_BOTTOM))
board.append(piece(edge.FACE_TOP, edge.CONE_TOP, edge.CONE_BOTTOM, edge.HOUSE_TOP))
board.append(piece(edge.FACE_TOP, edge.FACE_BOTTOM, edge.CONE_TOP, edge.HOUSE_TOP))
board.append(piece(edge.CONE_BOTTOM, edge.CONE_TOP, edge.HOUSE_TOP, edge.FACE_TOP))
board.append(piece(edge.CONE_TOP, edge.HOUSE_TOP, edge.FACE_TOP, edge.CONE_BOTTOM))
board.append(piece(edge.CONE_BOTTOM, edge.STAR_BOTTOM, edge.CONE_TOP, edge.FACE_BOTTOM))
board.append(piece(edge.HOUSE_BOTTOM, edge.CONE_BOTTOM, edge.HOUSE_TOP, edge.STAR_TOP))
board.append(piece(edge.FACE_BOTTOM, edge.STAR_BOTTOM, edge.STAR_TOP, edge.CONE_TOP))


def main():
    print("Main function")

if __name__ == '__main__':
    main()



