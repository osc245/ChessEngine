from Board import Board


def endGame(gameBoard):
    if gameBoard.whitesTurn:
        print("White wins")
    else:
        print("Black wins")


board = Board()
while True:
    print(board.toString())
    line = input().split()
    while not board.move(line):
        line = input().split()
    if board.mated():
        endGame(board)
