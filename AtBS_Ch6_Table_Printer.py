#Automate the Boring Stuff: Chapter 6 Practice Project - Table Printer


# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0]*len(table)
    finaltable = []
    for i in range(len(table)):
        for j in table[i]:
            if len(j) > int(colWidths[i]):
                colWidths[i] = len(j)
    for i in range(len(table[0])):
        tracker = 0
        for j in table:
            finaltable.append(' '+j[i].rjust(colWidths[tracker]))
            tracker = tracker + 1
        finaltable.append('\n')
    print(''.join(finaltable))


printTable(tableData)
