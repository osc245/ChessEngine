from Pieces.Piece import Piece


class Pawn(Piece):

    # enPassen field indicates whether the opponent can en passen capture it
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite)
        self.enPassen = False

    def toString(self):
        if self.isWhite:
            return "P"
        else:
            return "p"

    def validMove(self, pos, board):
        dy, dx = Piece.getDiff(pos)
        if dx == 0:
            if board[pos[0] + dy//abs(dy)][pos[1]] is not None:  # square immediately in front of pawn is free
                return False
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                self.enPassen = False
                return True
            if (self.isWhite and dy == 2 and pos[0] == 1) or (not self.isWhite and dy == -2 and pos[0] == 6):
                if board[pos[0] + dy][pos[1]] is None:  # square two squares in front of pawn is free
                    self.enPassen = True
                    return True
        if abs(dx) == 1:
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                if board[pos[2]][pos[3]] is not None and Piece.validCapture(pos, board):  # capturing regularly
                    self.enPassen = False
                    return True
                if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):  # capturing en passen
                    if isinstance(board[pos[0]][pos[3]], Pawn) and board[pos[0]][pos[3]].enPassen\
                            and board[pos[0]][pos[3]].isWhite != board[pos[0]][pos[1]].isWhite:
                        return True
        return False
