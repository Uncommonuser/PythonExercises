print ('Automate the Boring Stuff Chapter 5 Character Picture Grid')

#Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down. Copy the previous grid value, and write code that uses it to print the image.
#This took me far too long to think through when trying to use a loop function that would take any list of lists and do the same rather than simply use the lengths of the grid list only, in the end this only really works if the lists are the same length




grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

i = 0
for y in range(len(grid[i])):
    for x in range(len(grid)):
        print(grid[x][y], end = ' ')
    print()
