print ('Automate the Boring Stuff Chapter 5 Chess Dictionary Validator')

#In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid
#Chess pieces: 8 wpawn, 2 wknight, 2 wbishop,  2 wrook, 1 wqueen, 1wking; 8 bpawn, 2 bknight, 2 bbishop, 2brook, 1 bqueen, 1bking
#Chess dimensions: '1a' to '8h'


def isValidChessBoard(checkboard):
    checkpos = []
    checkpce = []
    chesspiecelist = ['wpawn', 'wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wknight', 'wknight','wbishop','wbishop', 'wrook', 'wrook', 'wqueen', 'wking', 'bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn', 'bknight','bknight', 'bbishop', 'bbishop', 'brook','brook', 'bqueen', 'bking']
    chessboardlist = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',  '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',  '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h', '5a', '5b', '5c', '5d', '5e', '5f', '15g', '5h', '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',  '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',  '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    validchecker = True
    for k in checkboard.keys():
        looplist = chessboardlist
        if k in chessboardlist:
            looplist.remove(k)
            #print(k)
        else:
            validchecker = False
            print('Invalid chess position', k)
    for v in checkboard.values():
        looplist = chesspiecelist
        if v in chesspiecelist:
            looplist.remove(v)
            #print(v)
        else:
            validchecker = False
            print('Invalid chess piece', v)
    if validchecker == True:
        print('Valid chessboard')
        return True
    else:
        print('Improper chessboard')
        return False

print('First list')
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'})
print('Second list')
isValidChessBoard({'12': 'bking', '6c': 'wsdfueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'})
print('Third list')
isValidChessBoard({'6c': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'wqueen', '3e': 'wking'})
print('Fourth list')
isValidChessBoard({'1h': 'bpawn', '6c': 'bpawn', '2g': 'bpawn', '5h': 'bqueen', '3e': 'wking'})
