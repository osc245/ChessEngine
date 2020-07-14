from Board import Board
import Parser


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
        currBoard.whitesTurn = not currBoard.whitesTurn
    return True


if __name__ == "__main__":
    board = Board()
    line = input()
    while doMoves(line, board):
        print(board.toString())
        line = input()
