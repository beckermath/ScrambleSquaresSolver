# Deliverable 1

I implemented the backtracking solution following the algorithm given in the first research paper mentioned in the README.md

https://www.cs.umb.edu/~eb/sam/maccabees/backtrackingPaper.pdf

I represented pieces in my program using Uppercase->Lowercase letters to represent the split tops and bottoms of pictures

  Star = Aa<br/>
  Cone = Bb<br/>
  House = Cc<br/>
  Face = Dd<br/>
 
The solution ordered the pieces as follows

  1 2 3<br/>
  4 5 6<br/>
  7 8 9<br/>
 
  and gives the rotation of the piece following bottom->left->top->right
 
  Orientation<br/>

  0: bottom edge of piece <br/>
  1: left edge of piece<br/>
  2: top edge of piece<br/>
  3: right edge of piece<br/>
  
  Example: Piece in solution - dBaD<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;top edge<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a<br/>
left edge  B &nbsp; D  right edge <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bottom edge<br/>
         
When running puzzle.py the output given in this form:

  Star = Aa, Cone = Bb, House = Cc, Face = Dd<br/>
  bottom:0 left:1 top:2 right:3<br/>

  1 2 3<br/>
  4 5 6<br/>
  7 8 9<br/>

  dBaD   BdAc   bCDB<br/>
  BCDd   CDbB   DbBC<br/>
  Bdba   CAcb   ABda<br/>
  
Arranging the pieces matching them with their position and orientation in accordance with the example above will build the solution.

With the solution I then represented teh solution with the solution graph modeled in the second research paper in the README

  http://users.wfu.edu/masonsk/scramblesquares.pdf (examples of solution graphs for a 2x2 puzzle on pgs. 5-6

I made use of networkx to display the solution graph for the solution found by the program. The code in graph_display.py will open up a window with the graph figure. The solution graph for the solution shown in the README looks like this:

![](images/example_graph.png)

The nodes represent split patterns or pictures, and the edge colors are matched with a piece given in the legend. corner pieces have only one edge contributing to the solution, while center outside pieces contribute 2 edges to the solution and the middle piece has 4 edges contributing to the solution. 

Feel free to uncomment the line that shuffles the PIECES at the beginning of the main function in puzzle.py, this will reveal a few alternate solutions as the cards are regarded in a different order by the algorithm
  
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

