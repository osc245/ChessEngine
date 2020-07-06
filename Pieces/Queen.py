from Pieces.Piece import Piece


class Queen(Piece):

    def toString(self):
        if self.isWhite:
            return "Q"
        else:
            return "q"

    @staticmethod
    def validMove(pos, board):
        return Piece.checkClearLine(pos, board) and Piece.checkClearDiagonal(pos, board)

