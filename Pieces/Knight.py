from Pieces.Piece import Piece


class Knight(Piece):

    def toString(self):
        if self.isWhite:
            return "N"
        else:
            return "n"

    @staticmethod
    def validMove(pos, board):
        if not (Piece.validCapture(pos, board) or Piece.validMove(pos, board)):
            return False
        dy, dx = Piece.getDiff(pos)
        return (abs(dy) == 1 and abs(dx) == 2) or (abs(dy) == 2 and abs(dx) == 1)
