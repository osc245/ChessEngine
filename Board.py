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

    # updates board with given move, if possible and returns True or False depending on whether the move could be made
    def move(self, pos):
        for i in range(4):
            pos[i] = int(pos[i])
        if self.checkMove(pos):
            self.tryMove(pos)
            return True
        else:
            return False

    # checks whether the move is valid and the player is not in check after making it
    def checkMove(self, pos):
        if not self.validMovement(pos):
            return False
        tempBoard = copy.deepcopy(self)
        tempBoard.tryMove(pos)
        if tempBoard.inCheck(self.whitesTurn):
            return False
        return True

    # checks whether the proposed movement is valid
    def validMovement(self, pos):
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

    # checks whether the player specified by the parameter is in check
    def inCheck(self, white):
        self.whitesTurn = not white
        pieces = self.getPieces(not white)
        king = self.getKing(white)
        for x in pieces:
            if self.validMovement(x + king + [""]):
                return True
        return False

    # will update the board with a given move
    def tryMove(self, pos):
        self.board[pos[2]][pos[3]] = self.board[pos[0]][pos[1]]
        self.board[pos[0]][pos[1]] = None
        if pos[4] == "ep":
            self.board[pos[0]][pos[3]] = None
        if pos[4] == "kc" or pos[4] == "qc":
            row = 0 if self.whitesTurn else 7
            if pos[4] == "kc":
                self.board[row][5] = self.board[row][7]
                self.board[row][7] = None
            else:
                self.board[row][3] = self.board[row][0]
                self.board[row][0] = None
        if pos[4] in ["N", "B", "R", "Q"]:
            if pos[4] == "N":
                self.board[pos[2]][pos[3]] = Knight(self.whitesTurn)
            elif pos[4] == "B":
                self.board[pos[2]][pos[3]] = Bishop(self.whitesTurn)
            elif pos[4] == "R":
                self.board[pos[2]][pos[3]] = Rook(self.whitesTurn)
            elif pos[4] == "Q":
                self.board[pos[2]][pos[3]] = Queen(self.whitesTurn)
        return self

    def getPieces(self, white):
        return [[i, j] for i in range(8) for j in range(8) if self.board[i][j] is not None and
                not isinstance(self.board[i][j], King) and self.board[i][j].isWhite == white]

    def getKing(self, white):
        return [[i, j] for i in range(8) for j in range(8) if isinstance(self.board[i][j], King) and
                self.board[i][j].isWhite == white][0]




