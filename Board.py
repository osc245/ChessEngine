from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn
import copy


class Board:
    def __init__(self):
        self.board = [[Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True),
                       Rook(True)],
                      [Pawn(True) for x in range(8)],
                      [None] * 8, [None] * 8, [None] * 8, [None] * 8,
                      [Pawn(False) for x in range(8)],
                      [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False),
                       Knight(False), Rook(False)]]
        self.whitePieces = [[i, j] for i in range(2) for j in range(8) if i != 0 or j != 4]
        self.blackPieces = [[i, j] for i in range(6, 8) for j in range(8) if i != 7 or j != 4]
        self.whiteKing = [0, 4]
        self.blackKing = [7, 4]
        self.whitesTurn = True

    def toString(self):
        board = ""
        for i in range(7, -1, -1):
            board += str(i + 1) + "|"
            for j in range(8):
                if self.board[i][j] is None:
                    board += "_"
                else:
                    board += self.board[i][j].toString()
                board += "|"
            board += "\n"
        board += "  a b c d e f g h"
        return board

    """
    pos is a list of format: [old row, old column, new row, new column, specialMove]
    special move is left blank if regular move or capture but is otherwise: enPassen, castle or piece to promote to
    return false is the provided move in invalid
    """
    def move(self, pos):
        for i in range(4):
            pos[i] = int(pos[i])
        if not self.checkMove(pos):
            return False
        tempBoard = self.tryMove(pos)
        if tempBoard.inCheck():
            return False
        self.board = tempBoard.board
        self.whitesTurn = not self.whitesTurn
        return True

    def checkMove(self, pos):
        for x in pos[:4]:  # invalid position
            if x < 0 or x > 7:
                return False
        if pos[0] == pos[2] and pos[1] == pos[3]:  # moving to the same square
            return False
        if self.board[pos[0]][pos[1]] is None:  # there is not piece in initial position
            return False
        if self.whitesTurn != self.board[pos[0]][pos[1]].isWhite:  # wrong colour moving
            return False
        return self.board[pos[0]][pos[1]].validMove(pos, self.board)

    # checks whether player would be in check if they made proposed move
    def inCheck(self):
        self.whitesTurn = not self.whitesTurn
        pieces = self.getPieces()
        king = self.getKing()
        for x in pieces:
            if self.checkMove(x + king):
                return True
        return False

    def tryMove(self, pos):
        temp = copy.deepcopy(self)
        temp.board[pos[2]][pos[3]] = temp.board[pos[0]][pos[1]]
        temp.board[pos[0]][pos[1]] = None
        if pos[4] == "ep":
            temp.board[pos[0]][pos[3]] = None
        if pos[4] == "kc" or pos[4] == "qc":
            row = 0 if self.whitesTurn else 7
            if pos[4] == "kc":
                print(True)
                temp.board[row][5] = temp.board[row][7]
                temp.board[row][7] = None
            else:
                temp.board[row][3] = temp.board[row][0]
                temp.board[row][0] = None
        if pos[4] in ["N", "B", "R", "Q"]:
            if pos[4] == "N":
                temp.board[pos[2]][pos[3]] = Knight(self.whitesTurn)
            elif pos[4] == "B":
                temp.board[pos[2]][pos[3]] = Bishop(self.whitesTurn)
            elif pos[4] == "R":
                temp.board[pos[2]][pos[3]] = Rook(self.whitesTurn)
            elif pos[4] == "Q":
                temp.board[pos[2]][pos[3]] = Queen(self.whitesTurn)
        return temp

    # returns the positions of the pieces of the player who's turn it is not
    def getPieces(self):
        return [[i, j] for i in range(8) for j in range(8) if self.board[i][j] is not None and
                self.board[i][j].isWhite == self.whitesTurn]

    # returns the position of the king of the player who's turn it is
    def getKing(self):
        return [[i, j] for i in range(8) for j in range(8) if isinstance(self.board[i][j], King) and
                self.board[i][j].isWhite != self.whitesTurn][0]

    def mate(self):
        pass

    def stalemate(self):
        pass


