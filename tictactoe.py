#Amelia Krouse
#Instructor: Juan Arias
#3/26/18

symbol = [ " ", "x", "o" ]

def printRow(row):
    one=' '
    two=' '
    three=' '
    if row[0]==1:
        one='o'
    if row[0]==2:
        one='x'
    if row[1]==1:
        two='o'
    if row[1]==2:
        two='x'
    if row[2]==1:
        three='o'
    if row[2]==2:
        three='x'
    print("| " + one + " | " + two + " | " + three + " |")
    pass

def lining():
    print("+-----------+")
    pass

def printBoard(board):
    print(lining())
    print(printRow(board[0]))
    print(lining())
    print(printRow(board[1]))
    print(lining())
    print(printRow(board[2]))
    print(lining())
    pass

def markBoard(board, row, col, player):
    board[row][col]=player
    pass

def getPlayerMove():
    row = int(input("Please enter a row number."))
    col = int(input("Please enter a column number."))
    return (row,col)

def hasBlanks(board):
    for i in range(3):
        for k in range(3):
            if board[i][k]==0:
                return True
    return False

def main():
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn

main()

