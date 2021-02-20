# Deliverable 2

The idea of maximizing the center is to identify pieces that are most
likely to be middle pieces and check those pieces first, solving the
puzzle in a spiral pattern.

7 8 9\
6 1 2\
5 4 3

Determining which pieces have the most potential to be the middle piece
I used this method:

1.  Count the number of times each picture occurs. This is the index of
    the picture.

2.  Assign a value index to each piece by summing the indices of the
    COMPLEMENTS of the pictures appearing on the piece.

3.  Place the piece with the HIGHEST value index in the middle.

Now when considering the pieces:

PIECES = \[ 'dBaD', 'BdAc', 'bCDB', 'BCDd', 'CDbB', 'DbBC', 'Bdba',
'CAcb', 'ABda' ,\]

We can reorder them with their value index:

PIECES = \[('Bdba', 21), ('bCDB', 20), ('CDbB', 20), ('DbBC', 20), ('dBaD', 18), ('BdAc', 18), ('CAcb', 18), ('BCDd', 17), ('ABda', 16)\]

Pieces with the higher value index have a higher chance of being the
middle piece and allow the algorithm to finish slightly faster compared
to a random arrangement of the pieces which usually doesn't come across
the middle piece as quickly.

I then needed to measure the execution time of the algorithm to compare
ordering the pieces by potential to be the middle and random order. For
this I used time library and took the difference of the start and end
time and displayed the result. Taking the average of 5 test runs for
both arranging the pieces by potential to be middle piece and random
order, here are the results:

**Ordering by middle piece potential:**\
0.03665\
0.03701\
0.03738\
0.03754\
Average: 0.04123

**Random order:**\
0.05226\
0.00350\
0.05193\
0.05546\
Average: 0.04219

Looking at the results, ordering by middle piece did just barely beat
the random ordering, but the results are not that impressive. You can
see the third trial taken with random ordering was very fast. This was a
result of the shuffling of the pieces actually putting the middle piece
is the first slot by chance. This beats the middle piece ordering since
the the middle piece is actually the third in the order when using the
method of ordering by potential to be middle piece. This results in the
ordering by middle piece being very consistently good, but at least for
my puzzle occasionally beaten by random shuffling.

One of the main challenges of this deliverable was getting the board to
solve in a spiral rather than left to right, this was needed since the
middle piece is the first places when solving in a spiral. I also did
work to make the terminal selection better, you can now select whether
you want to order by potential to be middle piece or have them randomly
ordered. You then get to select whether or not you want to generate the
solution graph from deliverable 1, and the puzzle is displayed in a much
more helpful grid format along with the execution time of the run.
