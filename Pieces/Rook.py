from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, isWhite):
        Piece.__init__(self, isWhite)
        self.moved = False

    def toString(self):
        if self.isWhite:
            return "R"
        else:
            return "r"

    def validMove(self, pos, board):
        if Piece.checkClearLine(pos, board):
            self.moved = True
            return True
        else:
            return False

