from Pieces.Piece import Piece


class Bishop(Piece):

    def toString(self):
        if self.isWhite:
            return "B"
        else:
            return "b"

    @staticmethod
    def validMove(pos, board):
        if not (Piece.validCapture(pos, board) or Piece.validMove(pos, board)):
            return False
        return Piece.checkClearDiagonal(pos, board)


