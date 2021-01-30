#
#   DFS backtracking scramble squares puzzle solver
#
#   Author: Becker Mathie
#

from enum import Enum
from graph import add_vertex
from graph import add_edge
from graph import print_graph

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
    def __init__(self, top, right, bottom, left, key):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.key = key

        add_edge(graph, bottom, left, key)
        add_edge(graph, left, top, key)
        add_edge(graph, top, right, key)
        add_edge(graph, right, bottom, key)

#
#   Initializing graph with 8 vertiticies, representing the two sides of the 4 puzzle images
#
#   4-   3-   2-   1-
#
#   4+   3+   2+   1+
#
        
graph = {}
add_vertex(graph, edge.STAR_TOP)
add_vertex(graph, edge.STAR_BOTTOM)
add_vertex(graph, edge.CONE_TOP)
add_vertex(graph, edge.CONE_BOTTOM)
add_vertex(graph, edge.HOUSE_TOP)
add_vertex(graph, edge.HOUSE_BOTTOM)
add_vertex(graph, edge.FACE_TOP)
add_vertex(graph, edge.FACE_BOTTOM)


#Construct pieces each with a key 1-9 to act as an edge color

piece1 = piece(edge.STAR_BOTTOM, edge.FACE_TOP, edge.FACE_BOTTOM, edge.CONE_TOP, 1)
piece2 = piece(edge.STAR_TOP, edge.HOUSE_BOTTOM, edge.CONE_TOP, edge.FACE_BOTTOM, 2)
piece3 = piece(edge.FACE_TOP, edge.CONE_TOP, edge.CONE_BOTTOM, edge.HOUSE_TOP, 3)
piece4 = piece(edge.FACE_TOP, edge.FACE_BOTTOM, edge.CONE_TOP, edge.HOUSE_TOP, 4)
piece5 = piece(edge.CONE_BOTTOM, edge.CONE_TOP, edge.HOUSE_TOP, edge.FACE_TOP, 5)
piece6 = piece(edge.CONE_TOP, edge.HOUSE_TOP, edge.FACE_TOP, edge.CONE_BOTTOM, 6)
piece7 = piece(edge.CONE_BOTTOM, edge.STAR_BOTTOM, edge.CONE_TOP, edge.FACE_BOTTOM, 7)
piece8 = piece(edge.HOUSE_BOTTOM, edge.CONE_BOTTOM, edge.HOUSE_TOP, edge.STAR_TOP, 8)
piece9 = piece(edge.FACE_BOTTOM, edge.STAR_BOTTOM, edge.STAR_TOP, edge.CONE_TOP, 9)

#   Build board with pieces 
#
#   0 1 2
#   3 4 5
#   6 7 8
#

board = []
board.append(piece1)
board.append(piece2)
board.append(piece3)
board.append(piece4)
board.append(piece5)
board.append(piece6)
board.append(piece7)
board.append(piece8)
board.append(piece9)


def main():
    print("Main function")
    print("Displaying graph...")
    print_graph(graph)

if __name__ == '__main__':
    main()



