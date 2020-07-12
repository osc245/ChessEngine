from Board import Board
import Parser


def endGame(gameBoard, stalemate):
    if stalemate:
        print("Stalemate")
    elif gameBoard.whitesTurn:
        print("White wins")
    else:
        print("Black wins")


# enter all the moves given so far (unless there is an invalid one)
# returns true if the game is still going or false if it has finished
def doMoves(moves, currBoard):
    algebraicMoves = moves.split()
    moves = Parser.parseMoves(moves)
    if moves is None:
        return True
    for i in range(len(moves)):
        if not currBoard.move(moves[i]):
            print("Invalid move:", algebraicMoves[i])
            return False
        if currBoard.mate():
            endGame(currBoard, False)
            return False
        if currBoard.stalemate():
            endGame(currBoard, True)
            return False
    return True


if __name__ == "__main__":
    board = Board()
    line = input()
    while doMoves(line, board):
        print(board.toString())
        line = input()
