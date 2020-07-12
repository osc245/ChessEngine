toNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


# converts a list of moves in long algebraic form to moves of format [oldRow, oldCol, newRow, newCol]
def parseMoves(coOrdinates):
    moves = []
    moveList = coOrdinates.split()
    whitesTurn = True
    for x in moveList:
        move = []
        backRank = 0 if whitesTurn else 7
        if x[0:5] == "O-O-O":
            move.extend([backRank, 4, backRank, 2, "qc"])
        elif x[0:3] == "O-O":
            move.extend([backRank, 4, backRank, 6, "kc"])
        else:
            counter = 0
            counter = parsePosition(move, x, counter)
            if not (x[counter] == "-" or x[counter] == "x"):
                fail(x)
            counter += 1
            counter = parsePosition(move, x, counter)
            if len(x) == counter + 2:
                if x[counter] == "=" and x[counter + 1] in ["N", "B", "R", "Q"]:
                    move.append(x[counter + 1])
                elif x[counter:counter + 2] == "ep":
                    move.append("ep")
            else:
                move.append("")
        if not move:
            fail(x)
        moves.append(move)
        whitesTurn = not whitesTurn
    return moves


def parsePosition(move, x, counter):
    if x[counter] in ["K", "N", "B", "R", "Q"]:
        counter += 1
    if not (x[counter] in toNum and 1 <= int(x[counter + 1]) <= 8):
        fail(x)
    move.extend([int(x[counter + 1]) - 1, int(toNum[x[counter]])])
    counter += 2
    return counter


def fail(move):
    print("Invalid notation", move)
    return None

