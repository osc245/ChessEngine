from Pieces.Piece import Piece
from Pieces.Rook import Rook


class King(Piece):

    def __init__(self, isWhite):
        Piece.__init__(self, isWhite)
        self.moved = False

    def toString(self):
        if self.isWhite:
            return "K"
        else:
            return "k"

    def validMove(self, pos, board):
        if not (Piece.validCapture(pos, board) or Piece.validMove(pos, board)):
            return False
        dy, dx = Piece.getDiff(pos)
        if abs(dx) <= 1 and abs(dy) <= 1:
            self.moved = True
            return True
        if not self.moved:  # castling
            if abs(dx) != 2 or dy != 0:
                return False
            row = 0 if self.isWhite else 7
            column = 0 if dx == -2 else 7
            if not isinstance(board[row][column], Rook) or board[row][column].moved:
                return False
            move = [pos[0], pos[1], row, column]
            if Piece.checkClearLine(move, board):
                return True
        return False

