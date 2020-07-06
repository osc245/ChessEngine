from Pieces.Piece import Piece


class Bishop(Piece):

    def toString(self):
        if self.isWhite:
            return "B"
        else:
            return "b"

    @staticmethod
    def validMove(pos, board):
        return Piece.checkClearDiagonal(pos, board)


