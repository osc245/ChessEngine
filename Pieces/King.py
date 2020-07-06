from Pieces.Piece import Piece


class King(Piece):

    def toString(self):
        if self.isWhite:
            return "K"
        else:
            return "k"

    @staticmethod
    def validMove(pos):
        dy, dx = Piece.getDiff(pos)
        return abs(dx) <= 1 and abs(dy) <= 1
