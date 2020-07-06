from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn


class Board:
    def __init__(self):
        self.board = [[Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True),
                       Rook(True)],
                      [Pawn(True) for x in range(8)],
                      [None] * 8, [None] * 8, [None] * 8, [None] * 8,
                      [Pawn(False) for x in range(8)],
                      [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False),
                       Knight(False), Rook(False)]]
        self.whitesTurn = True

    def toString(self):
        board = ""
        for i in range(7, -1, -1):
            board += "|"
            for j in range(8):
                if self.board[i][j] is None:
                    board += " "
                else:
                    board += self.board[i][j].toString()
                board += "|"
            board += "\n"
        return board

    # positions is a list of format: [old row, old column, new row, new column]
    # return false is the provided move in invalid
    def move(self, pos):
        pos = [int(x) for x in pos]
        if not self.checkMove(pos):
            return False
        self.board[pos[2]][pos[3]] = self.board[pos[0]][pos[1]]
        self.board[pos[0]][pos[1]] = None
        self.whitesTurn = not self.whitesTurn
        return True

    def checkMove(self, pos):
        for x in pos:  # invalid position
            if x < 0 or x > 7:
                return False
        if pos[0] == pos[2] and pos[1] == pos[3]:  # moving to the same square
            return False
        if self.board[pos[0]][pos[1]] is None:  # there is not piece in initial position
            return False
        if self.whitesTurn != self.board[pos[0]][pos[1]].isWhite:  # wrong colour moving
            return False
        return self.board[pos[0]][pos[1]].validMove(pos, self.board)

    def mated(self):
        pass
