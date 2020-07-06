from Pieces.Piece import Piece


class Pawn(Piece):

    def toString(self):
        if self.isWhite:
            return "P"
        else:
            return "p"

    @staticmethod
    def validMove(self, pos, board):
        dy, dx = Piece.getDiff(pos)
        if dx == 0:
            if board[pos[0] + dy//abs(dy)][pos[1]] is not None:  # square immediately in front of pawn is free
                return False
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                return True
            if (self.isWhite and dy == 2 and pos[0] == 1) or (not self.isWhite and dy == -2 and pos[0] == 6):
                if board[pos[0] + dy][pos[1]] is not None:  # square two squares in front of pawn is free
                    return False
                return True
        if abs(dx) == 1:
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                if board[pos[2]][pos[3]] is not None:  # there must be a piece on new square
                    return True
        return False
