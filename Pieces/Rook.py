from Pieces.Piece import Piece


class Rook(Piece):

    def toString(self):
        if self.isWhite:
            return "R"
        else:
            return "r"

    @staticmethod
    def validMove(pos, board):
        return Piece.checkClearLine(pos, board)

