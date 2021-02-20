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

    print("|{}\n|   {}   |   {}   |   {}   |\n| {}   {} | {}   {} | {}   {} |\n|   {}   |   {}   |   {}   |\n|{}\n|   {}   |   {}   |   {}   |\n| {}   {} | {}   {} | {}   {} |\n|   {}   |   {}   |   {}   |\n|{}\n|   {}   |   {}   |   {}   |\n| {}   {} | {}   {} | {}   {} |\n|   {}   |   {}   |   {}   |\n|{}\n".format(
        "-----------------------|",

        solution[0][2],
        solution[1][2],
        solution[2][2],
        solution[0][1],
        solution[0][3],
        solution[1][1],
        solution[1][3],
        solution[2][1],
        solution[2][3],
        solution[0][0],
        solution[1][0],
        solution[2][0],

        "-----------------------|",

        solution[3][2],
        solution[4][2],
        solution[5][2],
        solution[3][1],
        solution[3][3],
        solution[4][1],
        solution[4][3],
        solution[5][1],
        solution[5][3],
        solution[3][0],
        solution[4][0],
        solution[5][0],

        "-----------------------|",

        solution[6][2],
        solution[7][2],
        solution[8][2],
        solution[6][1],
        solution[6][3],
        solution[7][1],
        solution[7][3],
        solution[8][1],
        solution[8][3],
        solution[6][0],
        solution[7][0],
        solution[8][0],

        "-----------------------|"
    ))

    print("Execution time: %s seconds" % (end_time - start_time))