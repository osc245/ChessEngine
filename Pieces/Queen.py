from Pieces.Piece import Piece


class Queen(Piece):

    def toString(self):
        if self.isWhite:
            return "Q"
        else:
            return "q"

    @staticmethod
    def validMove(pos, board):
        if not (Piece.validCapture(pos, board) or Piece.validMove(pos, board)):
            return False
        if pos[0] - pos[2] == 0 or pos[1] - pos[3] == 0:
            return Piece.checkClearLine(pos, board)
        else:
            return Piece.checkClearDiagonal(pos, board)

