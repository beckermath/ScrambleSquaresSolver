'''
Method of Maximizing the Center

(1) Count the number of times each picture occurs. This is the
index of the picture.
(2) Assign a value index to each piece by summing the indices of
the COMPLEMENTS of the pictures appearing on the piece.
(3) Place the piece with the HIGHEST value index in the middle.
'''

def maximize_center(pieces):
    indicies = {
        "A": 0,
        "a": 0,
        "B": 0,
        "b": 0,
        "C": 0,
        "c": 0,
        "D": 0,
        "d": 0,
    }

    # Count the number of times each picture occurs in the puzzle
    for i in range(16):
        indicies["A"] = indicies["A"] + pieces[i].count('A')
        indicies["a"] = indicies["a"] + pieces[i].count('a')
        indicies["B"] = indicies["B"] + pieces[i].count('B')
        indicies["b"] = indicies["b"] + pieces[i].count('b')
        indicies["C"] = indicies["C"] + pieces[i].count('C')
        indicies["c"] = indicies["c"] + pieces[i].count('c')
        indicies["D"] = indicies["D"] + pieces[i].count('D')
        indicies["d"] = indicies["d"] + pieces[i].count('d')

    # Assign a value index to each piece equal to the sum of all the indicies given to the pieces pictures complements
    value_indicies = {}

    for i in range(16):
        value_indicies[pieces[i]] = sum_complement_indicies(pieces[i], indicies)

    # Pieces sorted in order of their potential to be the middle piece, based on number paired with them
    sorted_value_indicies = sorted(value_indicies.items(), key=lambda x: x[1], reverse=True)
    print("\nPieces sorted in order of potential to be middle piece (paired with value index)")
    print(sorted_value_indicies)
    
    new_pieces = []
    for i in range(16):
        new_pieces.append(sorted_value_indicies[i][0])

    return new_pieces


def sum_complement_indicies(piece, indicies):
    complement_sum = 0

    # Look at each picture on the piece and get the index of the complement
    for i in range(4):
        picture = piece[i]
        complement = get_complement(picture)
        complement_sum = complement_sum + indicies[complement]

    #return sum of the complement indicies
    return complement_sum

def get_complement(picture):
    if picture.islower():
        return picture.upper()
    else:
        return picture.lower()
