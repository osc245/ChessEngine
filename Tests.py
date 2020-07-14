import unittest
import Game
from Board import Board


def runTest(moves):
    board = Board()
    Game.doMoves(moves, board)
    return board.toString()


class Tests(unittest.TestCase):
    # trying to move in check
    def test1(self):
        moves = "e2-e3 d7-d5 Bf1-b5+ a7-a6"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|B|_|p|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|Q|K|_|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test2(self):
        moves = "e2-e3 d7-d5 Bf1-b5+ a7-a6"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|B|_|p|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|Q|K|_|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test25(self):
        moves = "d2-d4 e7-e6 a2-a4 Bf8-b4 a4-a5"
        expected = ("8|r|n|b|q|k|_|n|r|\n"
                    "7|p|p|p|p|_|p|p|p|\n"
                    "6|_|_|_|_|p|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|P|b|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|_|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # capturing
    def test3(self):
        moves = "Nb1-c3 e7-e5 a2-a3 Bf8-b4 a3-a4 Bb4xNc3"
        expected = ("8|r|n|b|q|k|_|n|r|\n"
                    "7|p|p|p|p|_|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|p|_|_|_|\n"
                    "4|P|_|_|_|_|_|_|_|\n"
                    "3|_|_|b|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|_|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test4(self):
        moves = "e2-e3 b7-b6 Qd1-f3 b6-b5 Qf3xRa8"
        expected = ("8|Q|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|p|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test5(self):
        moves = "e2-e3 b7-b6 Qd1-f3 Bc8-b7 a2-a3 Bb7xQf3"
        expected = ("8|r|n|_|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|P|_|_|_|P|b|_|_|\n"
                    "2|_|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test6(self):
        moves = "d2-d4 Ng8-f6 Bc1-g5 d7-d6 Bg5xNf6"
        expected = ("8|r|n|b|q|k|b|_|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|p|_|B|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test7(self):
        moves = "e2-e3 b7-b6 Qd1-f3 Bc8-b7 a2-a3 Bb7xQf3"
        expected = ("8|r|n|_|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|P|_|_|_|P|b|_|_|\n"
                    "2|_|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test8(self):
        moves = "d2-d4 h7-h6 Bc1-g5 h6xBg5"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|p|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test9(self):
        moves = "d2-d4 e7-e6 Bc1-g5 d7-d6 Bg5xQd8"
        expected = ("8|r|n|b|B|k|b|n|r|\n"
                    "7|p|p|p|_|_|p|p|p|\n"
                    "6|_|_|_|p|p|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test10(self):
        moves = "b2-b3 g7-g6 b3-b4 Bf8-g7 b4-b5 Bg7xRa1"
        expected = ("8|r|n|b|q|k|_|n|r|\n"
                    "7|p|p|p|p|p|p|_|p|\n"
                    "6|_|_|_|_|_|_|p|_|\n"
                    "5|_|P|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|_|P|P|P|P|P|P|\n"
                    "1|b|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test11(self):
        moves = "a2-a4 h7-h5 Ra1-a3 Rh8-h6 Ra3-d3 Rh6-g6 Rd3xd7"
        expected = ("8|r|n|b|q|k|b|n|_|\n"
                    "7|p|p|p|R|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|r|_|\n"
                    "5|_|_|_|_|_|_|_|p|\n"
                    "4|P|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|_|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # castling
    def test12(self):
        moves = "Ng1-f3 a7-a6 e2-e3 a6-a5 Bf1-e2 a5-a4 O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n" +
                    "7|_|p|p|p|p|p|p|p|\n" +
                    "6|_|_|_|_|_|_|_|_|\n" +
                    "5|_|_|_|_|_|_|_|_|\n" +
                    "4|p|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|P|N|_|_|\n" +
                    "2|P|P|P|P|B|P|P|P|\n" +
                    "1|R|N|B|Q|_|R|K|_|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test13(self):
        moves = "Nb1-c3 a7-a6 d2-d3 a6-a5 Bc1-e3 a5-a4 Qd1-d2 a4-a3 O-O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|_|p|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|p|_|N|P|B|_|_|_|\n"
                    "2|P|P|P|Q|P|P|P|P|\n"
                    "1|_|_|K|R|_|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test14(self):
        moves = "a2-a3 Nb8-c6 a3-a4 d7-d6 a4-a5 Bc8-e6 h2-h3 Qd8-d7 h3-h4 O-O-O"
        expected = ("8|_|_|k|r|_|b|n|r|\n"
                    "7|p|p|p|q|p|p|p|p|\n"
                    "6|_|_|n|p|b|_|_|_|\n"
                    "5|P|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|P|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|_|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test17(self):
        moves = "O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test18(self):
        moves = "Ng1-f3 a7-a6 e2-e3 a6-a5 Bf1-e2 a5-a4 Rh1-g1 b7-b6 Rg1-h1 a4-a3 O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|_|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|p|_|_|_|P|N|_|_|\n"
                    "2|P|P|P|P|B|P|P|P|\n"
                    "1|R|N|B|Q|K|_|_|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test19(self):
        moves = "Ng1-f3 a7-a6 e2-e3 a6-a5 Bf1-e2 a5-a4 Ke1-f1 b7-b6 Kf1-e1 a4-a3 O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|_|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|p|_|_|_|P|N|_|_|\n"
                    "2|P|P|P|P|B|P|P|P|\n"
                    "1|R|N|B|Q|K|_|_|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # en passen
    def test14(self):
        moves = "a2-a4 h7-h6 a4-a5 b7-b5 a5xb6ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|_|\n"
                    "6|_|P|_|_|_|_|_|p|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test15(self):
        moves = "a2-a4 h7-h5 a4-a5 h5-h4 g2-g4 h4xg3ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|P|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|p|_|\n"
                    "2|_|P|P|P|P|P|_|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test22(self):
        moves = "a2-a4 h7-h6 b2-b4 c7-c5 a4xb5ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|_|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|p|\n"
                    "5|_|_|p|_|_|_|_|_|\n"
                    "4|P|P|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|_|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test23(self):
        moves = "b2-b4 h7-h6 Nb1-a3 h6-h5 Na3-c4 h5-h4 b4xc5ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|P|N|_|_|_|_|p|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|_|P|P|P|P|P|P|\n"
                    "1|R|_|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test24(self):
        moves = "a2-a4 b7-b6 a4-a5 b6-b5 a5xb6ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|P|p|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test25(self):
        moves = "a2-a4 b7-b5 b2-b3 b5-b4 a4xb5ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|P|p|_|_|_|_|_|_|\n"
                    "3|_|P|_|_|_|_|_|_|\n"
                    "2|_|_|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test26(self):
        moves = "a2-a4 b7-b5 a4-a5 c7-c5 a5xc6ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|_|_|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|P|p|p|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # promotion
    def test16(self):
        moves = "a2-a4 h7-h6 a4-a5 b7-b5 a5xb6ep Nb8-c6 b6-b7 g7-g6 b7-b8=Q"
        expected = ("8|r|Q|b|q|k|b|n|r|\n" +
                    "7|p|_|p|p|p|p|_|_|\n" +
                    "6|_|_|n|_|_|_|p|p|\n" +
                    "5|_|_|_|_|_|_|_|_|\n" +
                    "4|_|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|_|_|_|_|\n" +
                    "2|_|P|P|P|P|P|P|P|\n" +
                    "1|R|N|B|Q|K|B|N|R|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test27(self):
        moves = "c2-c4 d7-d5 b2-b3 d5xc4 Bc1-a3 c4-c3 Ba3-b4 c3-c2=Q"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|B|_|_|_|_|_|_|\n"
                    "3|_|P|p|_|_|_|_|_|\n"
                    "2|P|_|_|P|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # Invalid moving
    def test20(self):
        moves = "a2-a4 c7-c6 a4-a5 Qd8-b6 h2-h3 b7-b5"
        expected = ("8|r|n|b|_|k|b|n|r|\n" +
                    "7|p|p|_|p|p|p|p|p|\n" +
                    "6|_|q|p|_|_|_|_|_|\n" +
                    "5|P|_|_|_|_|_|_|_|\n" +
                    "4|_|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|_|_|_|P|\n" +
                    "2|_|P|P|P|P|P|P|_|\n" +
                    "1|R|N|B|Q|K|B|N|R|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test21(self):
        moves = "e2-e3 d7-d5 d2-d3 Bc8-g4 Ke1-c3"
        expected = ("8|r|n|_|q|k|b|n|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|p|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|b|_|\n"
                    "3|_|_|_|P|P|_|_|_|\n"
                    "2|P|P|P|_|_|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test27(self):
        moves = "e2-e3 a7-a6 e3-e5"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|_|p|p|p|p|p|p|p|\n"
                    "6|p|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test28(self):
        moves = "e2-b4"
        expected = ("8|r|n|b|q|k|b|n|r|\n" +
                    "7|p|p|p|p|p|p|p|p|\n" +
                    "6|_|_|_|_|_|_|_|_|\n" +
                    "5|_|_|_|_|_|_|_|_|\n" +
                    "4|_|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|_|_|_|_|\n" +
                    "2|P|P|P|P|P|P|P|P|\n" +
                    "1|R|N|B|Q|K|B|N|R|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # Gioachino Greco vs Anon 1620
    def test29(self):
        moves = "e2-e4 e7-e5 Ng1-f3 Nb8-c6 Bf1-c4 Bf8-c5 c2-c3 Qd8-e7 O-O d7-d6 d2-d4 Bc5-b6 Bc1-g5 f7-f6 Bg5-h4 \
        g7-g5 Nf3xg5 f6xg5 Qd1-h5+ Ke8-f8 Bh4xg5 Qe7-e8 Qh5-f3+ Kf8-g7 Bc4xg8 Rh8xg8 Qf3-f6"
        expected = ("8|r|_|b|_|q|_|r|_|\n"
                    "7|p|p|p|_|_|_|k|p|\n"
                    "6|_|b|n|p|_|Q|_|_|\n"
                    "5|_|_|_|_|p|_|B|_|\n"
                    "4|_|_|_|P|P|_|_|_|\n"
                    "3|_|_|P|_|_|_|_|_|\n"
                    "2|P|P|_|_|_|P|P|P|\n"
                    "1|R|N|_|_|_|R|K|_|\n"
                    "  a b c d e f g h")

        self.assertEqual(runTest(moves), expected)
